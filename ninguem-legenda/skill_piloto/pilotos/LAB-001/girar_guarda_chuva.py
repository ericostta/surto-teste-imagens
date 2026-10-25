"""Gira o guarda-chuva inteiro da foto v8 em torno do ponto de contato da copa com a parede.
Fundo descoberto: copiado das versões v7 e v6 (mesmo cenário, alinhado) onde elas não têm guarda-chuva; resto por inpaint + grão.
Poça e cabo acompanham o objeto. Uso: girar_guarda_chuva.py SAIDA ANGULO_HORARIO
Registro: pixels reconstruídos (divulgar)."""
import sys, cv2, numpy as np
saida, TH = sys.argv[1], float(sys.argv[2])
L = lambda k: cv2.imread(f"foto_real_L8CFD_chatgpt_{k}_original.png")
v8, v7, v6 = L("v8"), L("v7"), L("v6"); H, W = v8.shape[:2]
C = (535.0, 350.0)                       # cubo da copa (v8): giro rígido do objeto em torno dele
FOOT = (600.0, 835.0)
CONTORNO = np.array([(165,475),(230,370),(300,290),(350,250),(400,215),(440,185),(520,158),(580,150),(640,152),(700,170),(770,205),(830,250),(868,285),(858,300),(835,360),(795,400),(750,440),(700,475),(630,500),(560,520),(500,535),(420,535),(330,535),(240,530),(175,500)], np.int32)
def umb_mask(im, folga=0):
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(int); b = im[...,0].astype(int); r = im[...,2].astype(int)
    pm = np.zeros((H, W), np.uint8)
    cv2.fillPoly(pm, [np.array([(140,150),(900,150),(900,520),(640,520),(640,860),(560,860),(540,560),(140,560)], np.int32)], 255)
    m = ((g < 80) & ((r-b) < 14) & (pm > 0)).astype(np.uint8)*255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9,9), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m); k = 1 + int(np.argmax(st[1:,4])); m = (lab==k).astype(np.uint8)*255
    inv = cv2.bitwise_not(m); ff = inv.copy(); cv2.floodFill(ff, None, (0,0), 0); m = cv2.bitwise_or(m, cv2.bitwise_and(inv, ff))
    return cv2.dilate(m, np.ones((folga*2+1,)*2, np.uint8)) if folga else m
# máscara do objeto na v8: copa = contorno desenhado; haste e cabo = limiar
m8 = umb_mask(v8)
cp = np.zeros((H, W), np.uint8); cv2.fillPoly(cp, [CONTORNO], 255)
copa8 = cv2.bitwise_and(cp, cv2.dilate(m8, np.ones((15,15), np.uint8)))
g8 = cv2.cvtColor(v8, cv2.COLOR_BGR2GRAY).astype(int); neutro = ((g8 < 100) & ((v8[...,2].astype(int) - v8[...,0].astype(int)) < 16)).astype(np.uint8)*255
copa8 = cv2.bitwise_or(cv2.bitwise_and(cv2.erode(cp, np.ones((5,5), np.uint8)), neutro), cv2.bitwise_and(cp, m8))
copa8 = cv2.morphologyEx(copa8, cv2.MORPH_CLOSE, np.ones((9,9), np.uint8))
n_, lab_, st_, _ = cv2.connectedComponentsWithStats(copa8); copa8 = (lab_ == 1 + int(np.argmax(st_[1:,4]))).astype(np.uint8)*255
inv_ = cv2.bitwise_not(copa8); ff_ = inv_.copy(); cv2.floodFill(ff_, None, (0,0), 0); copa8 = cv2.bitwise_or(copa8, cv2.bitwise_and(inv_, ff_))
band = np.zeros((H, W), np.uint8)   # faixa estreita em torno da haste e do cabo (eixo medido: x = 561,5 + 0,1706*(y-500))
cv2.fillPoly(band, [np.array([(561.5+0.1706*(340-500)-24,340),(561.5+0.1706*(340-500)+24,340),(561.5+0.1706*(850-500)+24,850),(561.5+0.1706*(850-500)-24,850)], np.int32)], 255)
haste = cv2.bitwise_and(cv2.bitwise_and(m8, cv2.bitwise_not(cp)), band)
objeto = cv2.bitwise_or(copa8, haste)
objeto = cv2.morphologyEx(objeto, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
# poça (anéis) a levar junto
poca = np.zeros((H, W), np.float32); cv2.ellipse(poca, (610, 838), (165, 40), 0, 0, 360, 1.0, -1)
poca = cv2.GaussianBlur(poca, (0,0), 6)
# --- fundo limpo ---
hole = cv2.dilate(cv2.bitwise_or(cv2.bitwise_or(objeto, m8), cv2.dilate(cp, np.ones((9,9), np.uint8))), np.ones((13,13), np.uint8))
hole = cv2.bitwise_or(hole, (poca > 0.02).astype(np.uint8)*255)
hole = cv2.bitwise_or(hole, np.where(np.arange(H)[:,None] > 0, 0, 0).astype(np.uint8) + (cv2.dilate(haste, np.ones((1,1),np.uint8))*0))
bg = v8.copy(); rest = hole.copy(); fonte = np.zeros((H, W), np.uint8)
for nome, src in (("v7", v7), ("v6", v6)):
    ms = umb_mask(src, 7); ms = cv2.bitwise_or(ms, (poca > 0.02).astype(np.uint8)*255)  # poça tb existe nelas
    ok = cv2.bitwise_and(rest, cv2.bitwise_not(ms)); ok[:540] = 0   # só abaixo da copa (haste, cabo, poça, piso)
    ring = cv2.bitwise_and(cv2.dilate(hole, np.ones((41,41), np.uint8)), cv2.bitwise_not(cv2.bitwise_or(hole, ms)))
    off = (v8.astype(np.float32) - src.astype(np.float32))[ring > 0].mean(0)
    sel = ok > 0
    bg[sel] = np.clip(src[sel].astype(np.float32) + off, 0, 255).astype(np.uint8)
    rest = cv2.bitwise_and(rest, cv2.bitwise_not(ok)); fonte[sel] = 1 if nome == "v7" else 2
# restante: só o que fica visível depois do giro (o que a nova copa cobre não precisa de fundo)
Rm = cv2.getRotationMatrix2D(C, -TH, 1.0)
novo = cv2.dilate(cv2.warpAffine(objeto, Rm, (W, H), flags=cv2.INTER_LINEAR), np.ones((7,7), np.uint8))
rest_all = rest.copy()   # buraco inteiro (a fonte do inpaint nunca deve ser pixel do guarda-chuva antigo)
rest = cv2.bitwise_and(rest, cv2.bitwise_not(novo))
rest = cv2.morphologyEx(rest, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
def preencher_vertical(bgr, buraco):
    out = bgr.astype(np.float32).copy(); rng = np.random.default_rng(7)
    for x in range(W):
        ys = np.where(buraco[:, x] > 0)[0]
        if len(ys) == 0: continue
        cortes = np.where(np.diff(ys) > 1)[0]; ini = np.r_[ys[0], ys[cortes + 1]]; fim = np.r_[ys[cortes], ys[-1]]
        for y0, y1 in zip(ini, fim):
            ta, tb = max(y0-7, 0), max(y0-1, 1); ba, bb = min(y1+2, H-1), min(y1+8, H)
            xa, xb = max(x-1, 0), min(x+2, W)
            top = out[ta:tb, xa:xb].reshape(-1,3).mean(0); bot = out[ba:bb, xa:xb].reshape(-1,3).mean(0)
            n = y1-y0+1; t = (np.arange(n)/max(n-1,1))[:, None]
            out[y0:y1+1, x] = top*(1-t) + bot*t
    bl = cv2.GaussianBlur(out, (0,0), sigmaX=4, sigmaY=1.2)
    m = cv2.GaussianBlur((buraco > 0).astype(np.float32), (0,0), 2)[..., None]
    out = out*(1-m) + bl*m + rng.normal(0, 2.2, out.shape).astype(np.float32)*m
    return np.clip(out, 0, 255).astype(np.uint8)
if rest.sum():
    rd = cv2.dilate(rest, np.ones((5,5), np.uint8))
    ip = cv2.inpaint(bg, cv2.dilate(rest_all, np.ones((5,5), np.uint8)), 21, cv2.INPAINT_TELEA)
    ip = cv2.GaussianBlur(ip, (0,0), 5)
    m = cv2.GaussianBlur((rd > 0).astype(np.float32), (0,0), 3)[..., None]
    g = np.random.default_rng(3).normal(0, 2.2, bg.shape).astype(np.float32)
    bg = np.clip(bg.astype(np.float32)*(1-m) + (ip.astype(np.float32)+g)*m, 0, 255).astype(np.uint8)
print("pixels do buraco:", int((hole>0).sum()), "v7:", int((fonte==1).sum()), "v6:", int((fonte==2).sum()), "inpaint:", int((rest>0).sum()))
# --- camada do objeto (RGBA pré-multiplicada) e da poça ---
a = cv2.GaussianBlur(objeto, (0,0), 1.0).astype(np.float32)/255
cam = np.dstack([v8.astype(np.float32)*a[...,None], a])
Rm = cv2.getRotationMatrix2D(C, -TH, 1.0)
rot = cv2.warpAffine(cam, Rm, (W, H), flags=cv2.INTER_CUBIC, borderValue=0)
ra = np.clip(rot[...,3:4], 0, 1); rrgb = rot[..., :3] / np.maximum(ra, 1e-4)
fx, fy = Rm @ np.array([FOOT[0], FOOT[1], 1.0]); dx, dy = fx-FOOT[0], fy-FOOT[1]
print("pé novo:", round(fx), round(fy))
# poça movida para o novo pé
T = np.float32([[1,0,dx],[0,1,dy]])
pv = cv2.warpAffine(v8, T, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
pa = cv2.warpAffine(poca, T, (W, H), flags=cv2.INTER_LINEAR)[..., None]
out = bg.astype(np.float32)
out = out*(1-pa) + pv.astype(np.float32)*pa
out = out*(1-ra) + rrgb*ra
cv2.imwrite(saida, np.clip(out, 0, 255).astype(np.uint8))
cv2.imwrite(saida + ".mascara.png", objeto)
