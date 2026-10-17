#!/usr/bin/env python3
"""Story 1080x1920 da frase (replica do cartao do Threads com fundo da mesma cor, sem moldura).
Uso: gerar_story_frase.py --conta surtodelucidez|eri_costta --frase "texto" --out arquivo.png [--aspas] [--bandeira]
Dimensoes medidas a partir do print do Story ajustado por Eri (editor do Instagram, 16/10/2026)."""
import argparse, os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(BASE, "assets")
W, H = 1080, 1920
LEFT, RIGHT = 173, 904          # bloco de conteudo (largura 731)
AV_Y, AV_D = 840, 70            # avatar
PITCH = 46.5                   # distancia entre linhas (px)
ICON_Y = 1049
FONT_BODY = os.path.join(A, "fonts", "roboto-latin-400-normal.woff")
FONT_BOLD = os.path.join(A, "fonts", "roboto-latin-700-normal.woff")
FONT_EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
TEXT_COLOR = (10, 10, 10)
BODY_SIZE = 30.3   # calibrado pela largura da linha medida no print de Eri

def circ(img, d):
    img = img.convert("RGB").resize((d*4, d*4), Image.LANCZOS)
    m = Image.new("L", (d*4, d*4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, d*4-1, d*4-1), fill=255)
    out = Image.new("RGB", (d*4, d*4), (255, 255, 255)); out.paste(img, (0, 0), m)
    return out.resize((d, d), Image.LANCZOS)

def wrap(draw, text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw: cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def gerar(conta, frase, out, aspas=None, bandeira=None, body_size=BODY_SIZE, bold_size=None):
    # Padrao de escrita por conta (definido por Eri): as duas contas usam "frase." entre aspas;
    # so o @eri_costta leva espaco + bandeira do Brasil no fim; @surtodelucidez nao leva bandeira.
    if aspas is None: aspas = True
    if bandeira is None: bandeira = (conta == "eri_costta")
    canvas = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(canvas)
    body = ImageFont.truetype(FONT_BODY, body_size)
    bold = ImageFont.truetype(FONT_BOLD, bold_size or body_size)
    t = frase.strip()
    if aspas: t = f'"{t}"'
    lines = wrap(d, t, body, RIGHT - LEFT)
    dy = -round((len(lines) - 2) * PITCH / 2)      # bloco continua centralizado (referencia: 2 linhas)
    AV_Y_ = AV_Y + dy
    # avatar
    av = Image.open(os.path.join(A, f"avatar_{conta}.png"))
    canvas.paste(circ(av, AV_D), (LEFT, AV_Y_))
    # nome
    cy = AV_Y_ + AV_D/2
    d.text((260.6, cy), conta, font=bold, fill=TEXT_COLOR, anchor="lm")
    # logo Threads
    logo = Image.open(os.path.join(A, "threads_logo.png")).convert("RGB")
    canvas.paste(logo, (RIGHT - logo.size[0] + 3, int(cy - logo.size[1]/2)))
    # texto
    base = 925 + dy + (-body.getbbox('"Mh', anchor="ls")[1])    # linha 1 alinhada ao topo medido
    for i, ln in enumerate(lines):
        y = base + i*PITCH
        d.text((LEFT, y), ln, font=body, fill=TEXT_COLOR, anchor="ls")
        if bandeira and i == len(lines)-1:
            x = LEFT + d.textlength(ln + " ", font=body)
            em = ImageFont.truetype(FONT_EMOJI, 109)
            tmp = Image.new("RGBA", (136, 128), (255, 255, 255, 0))
            ImageDraw.Draw(tmp).text((0, 0), "\U0001F1E7\U0001F1F7", font=em, embedded_color=True)
            tmp = tmp.resize((int(136*0.27), int(128*0.27)), Image.LANCZOS)
            canvas.paste(tmp, (int(x), int(y - tmp.size[1]*0.86)), tmp)
    # icones
    icons = Image.open(os.path.join(A, "icones_threads.png")).convert("RGB")
    iy = ICON_Y + dy + round((len(lines) - 2) * PITCH)
    canvas.paste(icons, (LEFT - 1, iy - 3))
    canvas.save(out, "PNG")
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--conta", required=True, choices=["surtodelucidez", "eri_costta"])
    ap.add_argument("--frase", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--aspas", action="store_true", default=None)
    ap.add_argument("--bandeira", action="store_true", default=None)
    a = ap.parse_args()
    print(gerar(a.conta, a.frase, a.out, a.aspas, a.bandeira))
