#!/usr/bin/env python3
"""PROPOSTA VISUAL (escurecimento suave localizado atras do bloco inferior e do titulo, texto a esquerda). Anterior: PROPOSTA VISUAL (fora da skill, nao fixa nada): base do Modelo A escolhido por Eri (traco divisor de largura total, blocos mais baixos)
com tres tratamentos do nome da serie. Fontes OFL de outras skills de Eri (EB Garamond, Archivo Black); usar uma na skill exigiria incluir fonte e OFL.txt.
Uso: compor_modeloA_escurecimento.py E1|E2|E3 SAIDA"""
import sys, tempfile, json
sys.dont_write_bytecode = True
sys.path.insert(0, "../../v0.2/o-que-ninguem-legenda-piloto/scripts"); sys.path.insert(0, "../../v0.2/o-que-ninguem-legenda-piloto/testes")
import test_piloto as tp, registro_numeracao as rn, compor_story as cs
from PIL import ImageDraw, ImageFont
SK = "/root/.claude/skills/synced/06aac802-b122-40e2-960e-127d5e3b16cd_36b41c7c-fc7e-475b-bb5b-ea538a08b930/"
GAR = SK + "permissao-do-dia/assets/EBGaramond-Italic.ttf"; ARCH = SK + "cartaz-ironico/assets/ArchivoBlack-Regular.ttf"
VAR = "T3"; ESC = sys.argv[1]
from PIL import Image, ImageChops, ImageFilter
P = {"E1": dict(b=0.42, t=0.36, fade=False), "E2": dict(b=0.30, t=0.26, fade=False), "E3": dict(b=0.50, t=0.46, fade=True)}[ESC]
Y0 = [None]
cs.PERFIS["MA"] = dict(cs.PERFIS["C"], fora_base_y=1466, assinatura_y=1526, grad_base_ini=1080)
L = cs.PERFIS["MA"]; W, H = 1080, 1920
class D2(ImageDraw.ImageDraw):
    def line(self, xy, fill=None, width=0, joint=None):
        (x0, y0), (x1, y1) = xy
        if x1 - x0 == 64: x1 = W - L["margem"]; fill = (255, 255, 255, 175); width = 2   # traço divisor de largura total (Modelo A)
        return super().line([(x0, y0), (x1, y1)], fill=fill, width=width)
cs.ImageDraw.Draw = lambda im, mode=None: D2(im, mode)
def trk_draw(d, x, y, txt, f, fill, trk):
    x0 = x
    for c in txt:
        d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + trk
    return x - trk
_o = cs.texto_trk
def t(d, xy, txt, f, fill, trk=0, ancora="l"):
    if txt == "001" and ancora == "l":
        fs = cs.fonte("Medium", L["assinatura_px"]); x = L["margem"] + cs.largura(d, "@", fs, L["assinatura_trk"]) + L["assinatura_trk"]
        return _o(d, (x, xy[1]), txt, f, fill, trk, ancora)
    if txt == "O QUE NINGUÉM LEGENDA":
        m, y = L["margem"], L["titulo_y"]; B = (255, 255, 255, 255)
        if VAR == "T1":
            f1 = ImageFont.truetype(GAR, 66); x1 = trk_draw(d, m, y - 6, txt, f1, B, 3); return (m, y, x1, y + 70)
        if VAR == "T2":
            f1 = ImageFont.truetype(ARCH, 40); x1 = trk_draw(d, m, y, txt, f1, B, 4); return (m, y, x1, y + 50)
        fa = cs.fonte("SemiBold", 27); xa = trk_draw(d, m, y, "O QUE NINGUÉM", fa, (255, 255, 255, 235), 9)
        fb = ImageFont.truetype(GAR, 104); xb = trk_draw(d, m - 4, y + 22, "LEGENDA", fb, B, 4); return (m, y, max(xa, xb), y + 150)
    return _o(d, xy, txt, f, fill, trk, ancora)
cs.texto_trk = t

def hfade(lo):
    g = Image.linear_gradient("L").rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT).resize((W, H))  # 255 na esquerda -> 0 na direita
    return g.point(lambda v: int(255 * (lo + (1 - lo) * v / 255)))
def painel(box, alpha, raio, feather, fade):
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rounded_rectangle(box, raio, fill=int(255 * alpha))
    m = m.filter(ImageFilter.GaussianBlur(feather))
    if fade: m = ImageChops.multiply(m, hfade(0.25))
    return m
def degrade_novo(base, Lp):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); px = ov.load()
    for y in range(min(H, Lp["grad_topo_fim"])):
        v = int(255 * Lp["grad_topo_max"] * (1 - y / Lp["grad_topo_fim"]) ** 1.4)
        for x in range(W): px[x, y] = (0, 0, 0, v)
    img = Image.alpha_composite(base.convert("RGBA"), ov)
    yt = Y0[0] - 50
    for box, a in (((40, 236, W - 40, 486), P["t"]), ((40, yt, W - 40, 1612), P["b"])):
        m = painel(box, a, 40, 30, P["fade"]); camada = Image.new("RGBA", (W, H), (0, 0, 0, 0)); camada.putalpha(m)
        img = Image.alpha_composite(img, camada)
    return img
cs.degrade = degrade_novo
T = tempfile.mkdtemp(); reg = f"{T}/r.csv"
tp.escrever(reg, [tp.linha("LAB-001", "TEXTO_APROVADO", na_foto="a", fora_do_enquadramento="b c")]); rn.main(["reservar", "--id", "LAB-001", "--registro", reg])
args = ("foto_real_L8CFD_chatgpt_v14_tratada.png", "Um guarda-chuva aberto secando no corredor.", "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar.", "001")
Y0[0] = 1100
r0 = cs.compor(*args, f"{T}/pre.png", perfil="MA", registro=reg, id_="LAB-001"); Y0[0] = r0["medidas"]["y_inicio_blocos"]
r = cs.compor(*args, sys.argv[2], perfil="MA", registro=reg, id_="LAB-001")
print(ESC, "y_blocos", Y0[0], r["aprovacao_tecnica"], r["falhas"], r["avisos"]); print(json.dumps(r["contraste"], ensure_ascii=False))
