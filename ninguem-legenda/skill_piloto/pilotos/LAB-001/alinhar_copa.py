#!/usr/bin/env python3
"""Alinha copa e haste de uma foto de guarda-chuva (CÓPIA; o original nunca é alterado).
Gira a copa no plano da imagem em torno do cubo, mantém a haste, preenche o que fica descoberto por inpainting.
Edição maior que o tratamento do piso: pixels do fundo descoberto são reconstruídos (inventados). Fica fora da skill.
Uso: alinhar_copa.py ENTRADA SAIDA ANGULO_GRAUS_HORARIO TX"""
import sys, json, hashlib
import numpy as np, cv2
from PIL import Image, ImageDraw

POLI = [(145,433),(200,367),(253,307),(300,267),(360,217),(400,187),(493,163),(587,137),(667,150),(767,183),(833,213),(873,248),
        (867,273),(853,353),(848,373),(787,440),(755,499),(660,527),(547,557),(453,548),(360,543),(280,515),(199,489)]
CUBO = (607, 225)
# banda da haste dentro da copa (do cubo até abaixo da borda inferior), preservada na posição original
def faixa_haste(meia=8):
    # eixo da haste visível: x = X0 + K*(y - 560); medido nos pixels (topo à direita)
    X0, K = 573.0, -0.098
    ya, yb = 222, 640
    xa, xb = X0 + K*(ya-560), X0 + K*(yb-560)
    return [(xa-meia,ya),(xa+meia,ya),(xb+meia,yb),(xb-meia,yb)]
HASTE = faixa_haste()

def mascara(pontos, W, H, dil=0):
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon(pontos, fill=255)
    m = np.asarray(m)
    if dil > 0: m = cv2.dilate(m, np.ones((2*dil+1, 2*dil+1), np.uint8))
    if dil < 0: m = cv2.erode(m, np.ones((2*-dil+1, 2*-dil+1), np.uint8))
    return m

def preencher_vertical(bgr, buraco):
    """Preenche o buraco coluna a coluna por interpolação linear vertical entre o fundo acima e abaixo, com grão."""
    H, W = buraco.shape; out = bgr.astype(np.float32).copy(); rng = np.random.default_rng(7)
    for x in range(W):
        col = buraco[:, x] > 0; ys = np.where(col)[0]
        if len(ys) == 0: continue
        # segmentos contíguos
        cortes = np.where(np.diff(ys) > 1)[0]; ini = np.r_[ys[0], ys[cortes + 1]]; fim = np.r_[ys[cortes], ys[-1]]
        for y0, y1 in zip(ini, fim):
            ta, tb = max(y0 - 7, 0), max(y0 - 1, 1); ba, bb = min(y1 + 2, H - 1), min(y1 + 8, H)
            xa, xb = max(x - 1, 0), min(x + 2, W)
            top = out[ta:tb, xa:xb].reshape(-1, 3).mean(0); bot = out[ba:bb, xa:xb].reshape(-1, 3).mean(0)
            n = y1 - y0 + 1; t = (np.arange(n) / max(n - 1, 1))[:, None]
            out[y0:y1 + 1, x] = top * (1 - t) + bot * t
    # suaviza horizontalmente só dentro do buraco e devolve grão
    bl = cv2.GaussianBlur(out, (0, 0), sigmaX=4, sigmaY=1.2)
    m = cv2.GaussianBlur((buraco > 0).astype(np.float32), (0, 0), 2)[..., None]
    out = out * (1 - m) + bl * m
    out = out + rng.normal(0, 2.2, out.shape).astype(np.float32) * m
    return np.clip(out, 0, 255).astype(np.uint8)

def alinhar(entrada, saida, ang, tx):
    bgr = cv2.imread(entrada); H, W = bgr.shape[:2]
    poli = mascara(POLI, W, H, 2); haste = mascara(HASTE, W, H, 0)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    m0 = ((poli > 0) & (gray < 105)).astype(np.uint8) * 255
    m0 = cv2.morphologyEx(m0, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m0); maior = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    copa = (lab == maior).astype(np.uint8) * 255
    inv = cv2.bitwise_not(copa); ff = inv.copy(); cv2.floodFill(ff, None, (0, 0), 0)   # buracos internos
    copa = cv2.bitwise_or(copa, cv2.bitwise_and(inv, ff))
    copa = cv2.erode(copa, np.ones((3, 3), np.uint8))
    # 1) fundo: reconstrói toda a área antiga da copa (inclui a haste, que será recolada depois)
    buraco = cv2.dilate(cv2.bitwise_or(copa, mascara(POLI, W, H, 0)), np.ones((11, 11), np.uint8))
    fundo = preencher_vertical(bgr, buraco)
    # textura de reboco na parede da direita: alta frequência copiada de um trecho de parede abaixo, baixa frequência da interpolação
    fb = fundo.astype(np.float32); src = bgr.astype(np.float32)
    dy = 260; alta = src - cv2.GaussianBlur(src, (0, 0), 5)
    alta_desl = np.zeros_like(alta); alta_desl[:H-dy] = alta[dy:]
    zona = np.zeros((H, W), np.float32); zona[:, 780:] = 1; zona = zona * (buraco > 0)
    zona = cv2.GaussianBlur(zona, (0, 0), 3)[..., None]
    fundo = np.clip(fb + alta_desl * zona * 1.0, 0, 255).astype(np.uint8)
    # 2) copa inteira, com a haste interna apagada (preenchida com a própria copa) antes de girar
    banda = cv2.dilate(haste, np.ones((5, 5), np.uint8))
    copa_img = cv2.inpaint(bgr, banda, 5, cv2.INPAINT_TELEA)
    a = cv2.GaussianBlur(copa, (0, 0), 1.2).astype(np.float32) / 255
    pm = np.dstack([copa_img.astype(np.float32) * a[..., None], a])
    M = cv2.getRotationMatrix2D(CUBO, -ang, 1.0); M[0, 2] += tx   # ângulo negativo = sentido horário
    rot = cv2.warpAffine(pm, M, (W, H), flags=cv2.INTER_CUBIC, borderValue=0)
    ar = np.clip(rot[..., 3:4], 0, 1)
    comp = fundo.astype(np.float32) * (1 - ar) + rot[..., :3]
    # 3) recola a haste original por cima (borda suave), contínua com o trecho de baixo
    h = cv2.GaussianBlur(haste, (0, 0), 1.0).astype(np.float32)[..., None] / 255
    comp = comp * (1 - h) + bgr.astype(np.float32) * h
    out = np.clip(comp, 0, 255).astype(np.uint8); cv2.imwrite(saida, out)
    return dict(entrada=entrada, saida=saida, angulo_horario=ang, deslocamento_x=tx, cubo=CUBO, saida_sha256=hashlib.sha256(open(saida, "rb").read()).hexdigest())

if __name__ == "__main__":
    print(json.dumps(alinhar(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])), ensure_ascii=False))
