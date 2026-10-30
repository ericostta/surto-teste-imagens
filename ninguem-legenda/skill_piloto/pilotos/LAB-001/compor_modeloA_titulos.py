#!/usr/bin/env python3
"""PROPOSTA VISUAL (fora da skill, nao fixa nada): base do Modelo A escolhido por Eri (traco divisor de largura total, blocos mais baixos)
com tres tratamentos do nome da serie. Fontes OFL de outras skills de Eri (EB Garamond, Archivo Black); usar uma na skill exigiria incluir fonte e OFL.txt.
Uso: compor_modeloA_titulos.py T1|T2|T3 SAIDA"""
import sys, tempfile
sys.dont_write_bytecode = True
sys.path.insert(0, "../../v0.2/o-que-ninguem-legenda-piloto/scripts"); sys.path.insert(0, "../../v0.2/o-que-ninguem-legenda-piloto/testes")
import test_piloto as tp, registro_numeracao as rn, compor_story as cs
from PIL import ImageDraw, ImageFont
SK = "/root/.claude/skills/synced/06aac802-b122-40e2-960e-127d5e3b16cd_36b41c7c-fc7e-475b-bb5b-ea538a08b930/"
GAR = SK + "permissao-do-dia/assets/EBGaramond-Italic.ttf"; ARCH = SK + "cartaz-ironico/assets/ArchivoBlack-Regular.ttf"
VAR = sys.argv[1]
cs.PERFIS["MA"] = dict(cs.PERFIS["C"], fora_base_y=1466, assinatura_y=1526, grad_base_ini=1080)
L = cs.PERFIS["MA"]; W = 1080
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
T = tempfile.mkdtemp(); reg = f"{T}/r.csv"
tp.escrever(reg, [tp.linha("LAB-001", "TEXTO_APROVADO", na_foto="a", fora_do_enquadramento="b c")]); rn.main(["reservar", "--id", "LAB-001", "--registro", reg])
r = cs.compor("foto_real_L8CFD_chatgpt_v14_tratada.png", "Um guarda-chuva aberto secando no corredor.", "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar.", "001", sys.argv[2], perfil="MA", registro=reg, id_="LAB-001")
print(VAR, r["aprovacao_tecnica"], r["falhas"], r["avisos"], r["caixas"]["titulo"], r["contraste"]["titulo"], r["caixas"]["numero"])
