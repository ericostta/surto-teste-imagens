#!/usr/bin/env python3
"""Composição do Story 1080x1920 de O QUE NINGUÉM LEGENDA (PILOTO MANUAL v0.1, layout PROVISÓRIO, não homologado).

Uso:
  python3 compor_story.py --foto FOTO.png --na-foto "..." --fora "..." --numero LAB-001 --saida story.png
  python3 compor_story.py --simulacao --na-foto "..." --fora "..." --numero LAB-001 --saida sim.png
  acrescente --guias para desenhar zonas de segurança e margens (versão de conferência, nunca para publicar)

--simulacao usa um fundo neutro de marcação e carimba SIMULAÇÃO VISUAL; nunca é arte aprovada.
--numero: LAB-001 (teste) ou 001 (público; só depois de reservado e confirmado por Eri).
Todas as medidas ficam em LAYOUT e são provisórias.
"""
import argparse, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = Path(__file__).resolve().parent
FONTS = AQUI.parent / "assets" / "fonts"
W, H = 1080, 1920
LAYOUT = {
    "zona_topo": 250, "zona_base": 340,          # zonas de interface do Instagram (provisório, a verificar)
    "margem": 84,                                 # margem lateral
    "titulo_y": 292, "titulo_px": 30, "titulo_trk": 7,
    "numero_px": 30, "numero_trk": 4,
    "rotulo_px": 27, "rotulo_trk": 6,
    "na_foto_px": 46, "na_foto_max_linhas": 3,
    "fora_px": 56, "fora_max_linhas": 5, "fora_min_px": 44,
    "entrelinha": 1.27,
    "gap_blocos": 58, "gap_rotulo": 20,
    "fora_base_y": 1462,                          # base do bloco FORA (acima da zona inferior)
    "assinatura_y": 1522, "assinatura_px": 27, "assinatura_trk": 5,
    "grad_base_ini": 960, "grad_base_max": 0.80,  # degradê inferior
    "grad_topo_fim": 420, "grad_topo_max": 0.42,  # degradê superior
}
BRANCO = (255, 255, 255)


def fonte(nome, px):
    return ImageFont.truetype(str(FONTS / f"Inter-{nome}.otf"), px)


def largura(d, txt, f, trk=0):
    return sum(d.textlength(c, font=f) + trk for c in txt) - (trk if txt else 0)


def texto_trk(d, xy, txt, f, fill, trk=0, ancora="l"):
    x, y = xy
    if ancora == "r":
        x -= largura(d, txt, f, trk)
    for c in txt:
        d.text((x, y), c, font=f, fill=fill)
        x += d.textlength(c, font=f) + trk
    return x


def quebrar(d, txt, f, larg):
    """Quebra gulosa e depois equilibra: menor largura que mantém o mesmo número de linhas; evita viúva de uma palavra."""
    pal = txt.split()
    def guloso(lmax):
        linhas, atual = [], ""
        for p in pal:
            t = (atual + " " + p).strip()
            if d.textlength(t, font=f) <= lmax or not atual:
                atual = t
            else:
                linhas.append(atual); atual = p
        linhas.append(atual)
        return linhas
    base = guloso(larg)
    n = len(base)
    lo, hi = int(larg * 0.55), larg
    melhor = base
    while lo < hi:
        meio = (lo + hi) // 2
        l = guloso(meio)
        if len(l) <= n:
            melhor, hi = l, meio
        else:
            lo = meio + 1
    if len(melhor[-1].split()) == 1 and len(melhor) > 1 and len(melhor[-2].split()) > 2:
        pal2 = melhor[-2].split()
        melhor[-2] = " ".join(pal2[:-1]); melhor[-1] = pal2[-1] + " " + melhor[-1]
    return melhor


def ajustar(d, txt, nome, px, min_px, max_linhas, larg):
    while True:
        f = fonte(nome, px)
        linhas = quebrar(d, txt, f, larg)
        if len(linhas) <= max_linhas or px <= min_px:
            return f, linhas, px, len(linhas) > max_linhas
        px -= 2


def fundo_foto(caminho):
    im = Image.open(caminho).convert("RGB")
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))


def fundo_simulacao():
    im = Image.new("RGB", (W, H))
    px = im.load()
    for y in range(H):
        t = y / H
        c = (int(150 - 40 * t), int(156 - 42 * t), int(162 - 44 * t))
        for x in range(W):
            px[x, y] = c
    d = ImageDraw.Draw(im)
    for i in range(0, W + H, 90):
        d.line([(i, 0), (i - H, H)], fill=(168, 174, 180), width=2)
    d.rectangle([200, 540, 880, 900], outline=(210, 214, 218), width=4)
    d.text((540, 690), "ÁREA DA FOTO 9:16", font=fonte("SemiBold", 44), fill=(225, 228, 232), anchor="mm")
    d.text((540, 750), "(gerada manualmente no Gemini)", font=fonte("Medium", 34), fill=(225, 228, 232), anchor="mm")
    return im


def degrade(base):
    L = LAYOUT
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = ov.load()
    for y in range(H):
        a = 0.0
        if y < L["grad_topo_fim"]:
            a = L["grad_topo_max"] * (1 - y / L["grad_topo_fim"]) ** 1.4
        if y > L["grad_base_ini"]:
            t = min(1, (y - L["grad_base_ini"]) / (L["fora_base_y"] - 120 - L["grad_base_ini"]))
            a = max(a, L["grad_base_max"] * t ** 1.3)
            if y > L["fora_base_y"]:  # abaixo dos blocos o degradê alivia, para a foto continuar presente
                a = L["grad_base_max"] - (L["grad_base_max"] - 0.62) * (y - L["fora_base_y"]) / (H - L["fora_base_y"])
        v = int(255 * min(1, a))
        for x in range(W):
            px[x, y] = (0, 0, 0, v)
    return Image.alpha_composite(base.convert("RGBA"), ov)


def compor(foto, na_foto, fora, numero, saida, simulacao=False, guias=False):
    L = LAYOUT
    base = fundo_simulacao() if simulacao else fundo_foto(foto)
    img = degrade(base)
    d = ImageDraw.Draw(img)
    larg = W - 2 * L["margem"]
    avisos = []
    # topo
    ft, fn = fonte("SemiBold", L["titulo_px"]), fonte("Medium", L["numero_px"])
    texto_trk(d, (L["margem"], L["titulo_y"]), "O QUE NINGUÉM LEGENDA", ft, BRANCO + (240,), L["titulo_trk"])
    texto_trk(d, (W - L["margem"], L["titulo_y"]), numero if numero.startswith("LAB") else f"Nº {numero}", fn, BRANCO + (225,), L["numero_trk"], "r")
    # blocos, empilhados de baixo para cima
    fr = fonte("SemiBold", L["rotulo_px"])
    ff, lf, pxf, estf = ajustar(d, fora, "Medium", L["fora_px"], L["fora_min_px"], L["fora_max_linhas"], larg)
    fn_, ln, pxn, estn = ajustar(d, na_foto, "Regular", L["na_foto_px"], 36, L["na_foto_max_linhas"], larg)
    if estf: avisos.append("FORA excede o máximo de linhas no tamanho mínimo")
    if estn: avisos.append("NA FOTO excede o máximo de linhas no tamanho mínimo")
    hf = int(pxf * L["entrelinha"]) * len(lf)
    hn = int(pxn * L["entrelinha"]) * len(ln)
    y_f_txt = L["fora_base_y"] - hf
    y_f_rot = y_f_txt - L["gap_rotulo"] - L["rotulo_px"]
    y_n_txt = y_f_rot - L["gap_blocos"] - hn
    y_n_rot = y_n_txt - L["gap_rotulo"] - L["rotulo_px"]
    texto_trk(d, (L["margem"], y_n_rot), "NA FOTO", fr, BRANCO + (170,), L["rotulo_trk"])
    for i, l in enumerate(ln):
        d.text((L["margem"], y_n_txt + i * int(pxn * L["entrelinha"])), l, font=fn_, fill=BRANCO + (225,))
    d.line([(L["margem"], y_f_rot - L["gap_blocos"] // 2), (L["margem"] + 64, y_f_rot - L["gap_blocos"] // 2)], fill=BRANCO + (150,), width=3)
    texto_trk(d, (L["margem"], y_f_rot), "FORA DO ENQUADRAMENTO", fr, BRANCO + (170,), L["rotulo_trk"])
    for i, l in enumerate(lf):
        d.text((L["margem"], y_f_txt + i * int(pxf * L["entrelinha"])), l, font=ff, fill=BRANCO + (255,))
    # assinatura
    texto_trk(d, (L["margem"], L["assinatura_y"]), "@surtodelucidez", fonte("Medium", L["assinatura_px"]), BRANCO + (165,), L["assinatura_trk"])
    if y_n_rot < L["zona_topo"] + 400:
        avisos.append("blocos de texto muito altos: invadem a área central da foto")
    if simulacao:
        d.rectangle([0, 430, W, 498], fill=(190, 30, 30, 235))
        d.text((W // 2, 464), "SIMULAÇÃO VISUAL · NÃO É ARTE APROVADA", font=fonte("SemiBold", 34), fill=BRANCO, anchor="mm")
    if guias:
        g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        gd.rectangle([0, 0, W, L["zona_topo"]], fill=(255, 0, 0, 70)); gd.rectangle([0, H - L["zona_base"], W, H], fill=(255, 0, 0, 70))
        gd.rectangle([L["margem"], L["zona_topo"], W - L["margem"], H - L["zona_base"]], outline=(0, 255, 255, 200), width=2)
        gd.text((10, 10), f"zona topo {L['zona_topo']} px (provisória)", font=fonte("Medium", 24), fill=(255, 255, 255, 255))
        gd.text((10, H - L["zona_base"] + 10), f"zona base {L['zona_base']} px (provisória)", font=fonte("Medium", 24), fill=(255, 255, 255, 255))
        img = Image.alpha_composite(img, g)
    img.convert("RGB").save(saida)
    return avisos, {"linhas_na_foto": len(ln), "linhas_fora": len(lf), "px_na_foto": pxn, "px_fora": pxf, "y_inicio_blocos": y_n_rot}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--foto"); ap.add_argument("--na-foto", required=True); ap.add_argument("--fora", required=True)
    ap.add_argument("--numero", required=True); ap.add_argument("--saida", required=True)
    ap.add_argument("--simulacao", action="store_true"); ap.add_argument("--guias", action="store_true")
    a = ap.parse_args()
    if not a.simulacao and not a.foto:
        sys.exit("informe --foto ou use --simulacao")
    if "—" in a.na_foto + a.fora:
        sys.exit("travessão no texto: reescreva sem travessão no meio de frases")
    avisos, info = compor(a.foto, a.na_foto, a.fora, a.numero, a.saida, a.simulacao, a.guias)
    print(info)
    for v in avisos: print("AVISO:", v)


if __name__ == "__main__":
    main()
