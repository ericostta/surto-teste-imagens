#!/usr/bin/env python3
"""Compositor da CENA CORTADA (@surtodelucidez). Molde v0.1 reconstruido da arte da edicao 001.
Uso: python3 compor_cena_cortada.py --edicao 2 --titulo "..." --cena "..." --esq a.png --meio b.png --dir c.png --saida out.png
Nunca regenera a arte por gerador: so troca titulo, texto, 3 fotos e numeracao."""
import argparse, json, os, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(HERE, 'config.json')))
INK = (13, 13, 13)
FONT = lambda n, s: ImageFont.truetype(os.path.join(HERE, 'fonts', n + '.otf'), s)
# parametros tipograficos calibrados contra a arte 001 (1080x1920)
BODY_FONT, BODY_SIZE, BODY_X, BODY_MAXW, BODY_LH, BODY_BASE = 'NotoSerif-SemiBold', 27.8, 176, 731, 49.3, 1051
TITLE_FONT, TITLE_SIZE, TITLE_X, TITLE_BASE = 'NotoSerif-Bold', 60, 176, 985
CX = 541

def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if font.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    return lines

def cover_crop(img, aspect):
    h, w = img.shape[:2]
    if w / h > aspect:
        nw = int(h * aspect); x = (w - nw) // 2; return img[:, x:x + nw]
    nh = int(w / aspect); y = (h - nh) // 2; return img[y:y + nh, :]

def window_mask(name, ss=4):
    q = np.array(CFG['windows'][name], np.float32)
    m = np.zeros((1920 * 1, 1080), np.uint8)
    big = np.zeros((1920 * ss // 2 if False else 1920, 1080), np.float32)
    mk = np.zeros((1920 * ss, 1080 * ss), np.uint8) if False else None
    m = np.zeros((1920, 1080), np.uint8)
    cv2.fillConvexPoly(m, np.int32(np.round(q * 8)), 255, shift=3, lineType=cv2.LINE_AA)
    mf = m.astype(np.float32) / 255
    if name == 'meio':
        y0 = CFG['tear_y0']; tx = np.array(CFG['tear_x'], np.float32)
        xs = np.arange(1080, dtype=np.float32)[None, :]
        lim = np.full(1920, 1e9, np.float32)
        lim[y0:y0 + len(tx)] = tx
        mf = mf * np.clip(lim[:, None] - xs + 0.5, 0, 1)
    return mf

def place_photo(canvas, photo_path, name, gloss=True):
    q = np.array(CFG['windows'][name], np.float32)
    qw = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
    qh = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
    ph = cv2.imread(photo_path)
    if ph is None: raise SystemExit('foto nao encontrada: ' + photo_path)
    ph = cover_crop(ph, qw / qh)
    tw = int(qw * 2.2)
    ph = cv2.resize(ph, (tw, int(tw * qh / qw)), interpolation=cv2.INTER_AREA)
    h, w = ph.shape[:2]
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), q)
    warped = cv2.warpPerspective(ph, M, (1080, 1920), flags=cv2.INTER_LINEAR).astype(np.float32)
    m = window_mask(name)
    if gloss:
        d = cv2.distanceTransform((m > 0.5).astype(np.uint8), cv2.DIST_L2, 3)
        shade = np.exp(-d / 5.0) * 0.30
        warped *= (1 - shade)[..., None]
        ys, xs = np.mgrid[0:1920, 0:1080].astype(np.float32)
        x0, y0 = q[:, 0].min(), q[:, 1].min()
        u = (xs - x0) / (q[:, 0].max() - x0); v = (ys - y0) / (q[:, 1].max() - y0)
        band = np.exp(-(((u + 0.35 * v) - 0.62) / 0.10) ** 2) * 0.10
        warped = warped + (255 - warped) * band[..., None]
    mm = m[..., None]
    return canvas * (1 - mm) + warped * mm

def draw_number(canvas, txt, name, main):
    n = CFG['numbers'][name]
    f = FONT('Inter-Medium', CFG['num_size'])
    tr = CFG['num_track']
    widths = [f.getlength(c) for c in txt]
    tw = int(sum(widths) + tr * (len(txt) - 1)) + 8
    lay = Image.new('RGBA', (tw + 20, 60), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    col = tuple(CFG['num_color_main' if main else 'num_color_side']) + (255,)
    x = 10
    for c, w in zip(txt, widths):
        d.text((x, 30), c, font=f, fill=col, anchor='lm'); x += w + tr
    lay = lay.rotate(-n['ang'], resample=Image.BICUBIC, expand=True)
    a = np.array(lay).astype(np.float32)
    h, w = a.shape[:2]
    cx, cy = n['c']; x0, y0 = int(round(cx - w / 2)), int(round(cy - h / 2))
    al = a[..., 3:4] / 255 * (1.0 if main else 0.92)
    reg = canvas[y0:y0 + h, x0:x0 + w]
    canvas[y0:y0 + h, x0:x0 + w] = reg * (1 - al) + a[..., :3][..., ::-1] * al
    return canvas

def draw_text(canvas, titulo, cena):
    """Texto desenhado em 4x numa janela do papel e reduzido (serrilhado suave, peso fino ajustavel)."""
    SS = 4; RX0, RY0, RX1, RY1 = 100, 900, 1000, 1520
    lay = Image.new('RGBA', ((RX1 - RX0) * SS, (RY1 - RY0) * SS), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    T = lambda x, y: ((x - RX0) * SS, (y - RY0) * SS)
    d.text(T(TITLE_X, TITLE_BASE), titulo, font=FONT(TITLE_FONT, TITLE_SIZE * SS), fill=INK + (255,), anchor='ls', stroke_width=int(0.9 * SS), stroke_fill=INK + (255,))
    bf = FONT(BODY_FONT, BODY_SIZE * SS); bf1 = FONT(BODY_FONT, BODY_SIZE)
    lines = wrap(cena, bf1, BODY_MAXW)
    for i, ln in enumerate(lines):
        d.text(T(BODY_X, BODY_BASE + i * BODY_LH), ln, font=bf, fill=INK + (255,), anchor='ls', stroke_width=int(0.35 * SS), stroke_fill=INK + (255,))
    d.line([T(458, 1394), T(622, 1394)], fill=INK + (235,), width=2 * SS)
    sf = FONT('Inter-Bold', 30 * SS); word = 'CENA CORTADA'; tr = 6.2 * SS
    ws = [sf.getlength(c) for c in word]; tot = sum(ws) + tr * (len(word) - 1); x = T(CX, 0)[0] - tot / 2
    for c, w in zip(word, ws):
        d.text((x, T(0, 1452)[1]), c, font=sf, fill=INK + (255,), anchor='ls'); x += w + tr
    d.text(T(CX, 1494), '@surtodelucidez', font=FONT('NotoSerif-SemiBold', 25 * SS), fill=INK + (255,), anchor='ms', stroke_width=int(0.3 * SS), stroke_fill=INK + (255,))
    lay = lay.resize((RX1 - RX0, RY1 - RY0), Image.LANCZOS)
    a = np.array(lay).astype(np.float32)
    al = (a[..., 3:4] / 255) * 0.95
    reg = canvas[RY0:RY1, RX0:RX1]
    canvas[RY0:RY1, RX0:RX1] = reg * (1 - al) + np.array([INK[2], INK[1], INK[0]], np.float32) * al
    return canvas, lines

def aspas(t):
    import re
    t = re.sub(r'(^|[\s(])"', lambda m: m.group(1) + '\u201c', t)
    return t.replace('"', '\u201d')

def compor(edicao, titulo, cena, esq, meio, dir_, saida, gloss=True):
    titulo, cena = aspas(titulo), aspas(cena)
    canvas = cv2.imread(os.path.join(HERE, 'base_clean.png')).astype(np.float32)
    for nm, p in (('esq', esq), ('meio', meio), ('dir', dir_)):
        canvas = place_photo(canvas, p, nm, gloss)
    for nm, k in (('esq', edicao - 1), ('meio', edicao), ('dir', edicao + 1)):
        canvas = draw_number(canvas, f'{k:03d}', nm, nm == 'meio')
    canvas, lines = draw_text(canvas, titulo, cena)
    out = np.clip(canvas, 0, 255).astype(np.uint8)
    assert out.shape[:2] == (1920, 1080)
    cv2.imwrite(saida, out)
    return lines

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--edicao', type=int, required=True)
    ap.add_argument('--titulo', required=True); ap.add_argument('--cena', required=True)
    ap.add_argument('--esq', required=True); ap.add_argument('--meio', required=True); ap.add_argument('--dir', required=True)
    ap.add_argument('--saida', required=True); ap.add_argument('--sem-brilho', action='store_true')
    a = ap.parse_args()
    n = len(a.cena.split())
    if not 55 <= n <= 80: print(f'AVISO: cena com {n} palavras (faixa 55 a 80)', file=sys.stderr)
    ls = compor(a.edicao, a.titulo, a.cena, a.esq, a.meio, a.dir, a.saida, not a.sem_brilho)
    print('linhas:', len(ls)); [print(' ', l) for l in ls]
