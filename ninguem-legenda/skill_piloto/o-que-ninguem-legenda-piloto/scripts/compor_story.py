#!/usr/bin/env python3
"""Composição do Story 1080x1920 de O QUE NINGUÉM LEGENDA (PILOTO MANUAL v0.1.1; layout PROVISÓRIO, não homologado).

Uso:
  python3 compor_story.py --foto FOTO.png --na-foto "..." --fora "..." --numero LAB-001 --saida story.png [--perfil A|B]
  python3 compor_story.py --simulacao [--foto MARCADOR.png] ...    carimba SIMULAÇÃO VISUAL (nunca é arte aprovada)
  --guias    desenha zonas de segurança e margens (conferência; nunca para publicar)
  --registro registro_piloto.csv --id LAB-001    obrigatório para número público (001, 002...): o número precisa estar RESERVADO

Perfis (hipóteses de layout, ambas provisórias): A = referência do v0.1; B = degradê mais leve, FORA mais moderado, assinatura mais afastada.

APROVAÇÃO TÉCNICA: a arte só é gravada se não houver falha. Falhas: texto que não cabe nos limites de linhas no corpo mínimo,
elemento fora das zonas de segurança ou das margens, número público sem reserva. O texto das histórias NUNCA é alterado aqui:
se não couber, a peça fica bloqueada e a decisão editorial é de Eri. Sempre grava <saida>.checagem.json. Código de saída 2 = bloqueio
técnico; 3 = numeração. --rascunho grava mesmo com falha, com a faixa NÃO APTA TECNICAMENTE.
"""
import argparse, hashlib, json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = Path(__file__).resolve().parent
FONTS = AQUI.parent / "assets" / "fonts"
W, H = 1080, 1920
BASE = {
    "zona_topo": 250, "zona_base": 340,          # zonas de interface do Instagram (provisório, a verificar)
    "margem": 84,
    "titulo_y": 292, "titulo_px": 30, "titulo_trk": 7,
    "numero_px": 30, "numero_trk": 4,
    "rotulo_px": 27, "rotulo_trk": 6, "rotulo_alpha": 170,
    "na_foto_px": 46, "na_foto_min_px": 36, "na_foto_max_linhas": 3, "na_foto_alpha": 225,
    "fora_px": 56, "fora_min_px": 44, "fora_max_linhas": 5, "fora_alpha": 255, "fora_peso": "Medium",
    "entrelinha": 1.27, "gap_blocos": 58, "gap_rotulo": 20,
    "fora_base_y": 1462,
    "assinatura_y": 1522, "assinatura_px": 27, "assinatura_trk": 5, "assinatura_alpha": 165,
    "grad_base_ini": 960, "grad_base_max": 0.80, "grad_base_fim": 0.62,
    "grad_topo_fim": 420, "grad_topo_max": 0.42,
    "sombra": 0.0,
}
PERFIS = {
    "A": dict(BASE),
    "B": dict(BASE, fora_px=50, fora_min_px=42, fora_peso="Regular", fora_alpha=245, na_foto_px=44, na_foto_alpha=215, rotulo_px=26,
              gap_blocos=52, fora_base_y=1396, assinatura_y=1456,
              grad_base_ini=1010, grad_base_max=0.56, grad_base_fim=0.30, grad_topo_max=0.34, sombra=0.55),
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
    x0 = x
    for c in txt:
        d.text((x, y), c, font=f, fill=fill)
        x += d.textlength(c, font=f) + trk
    return (x0, y, x - trk, y + int(f.size * 1.2))


def quebrar(d, txt, f, larg):
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
        p2 = melhor[-2].split()
        melhor[-2] = " ".join(p2[:-1]); melhor[-1] = p2[-1] + " " + melhor[-1]
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


def fundo_neutro():
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


def degrade(base, L):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = ov.load()
    for y in range(H):
        a = 0.0
        if y < L["grad_topo_fim"]:
            a = L["grad_topo_max"] * (1 - y / L["grad_topo_fim"]) ** 1.4
        if y > L["grad_base_ini"]:
            t = min(1, (y - L["grad_base_ini"]) / (L["fora_base_y"] - 120 - L["grad_base_ini"]))
            a = max(a, L["grad_base_max"] * t ** 1.3)
            if y > L["fora_base_y"]:
                a = L["grad_base_max"] - (L["grad_base_max"] - L["grad_base_fim"]) * (y - L["fora_base_y"]) / (H - L["fora_base_y"])
        v = int(255 * min(1, a))
        for x in range(W):
            px[x, y] = (0, 0, 0, v)
    return Image.alpha_composite(base.convert("RGBA"), ov)


def checar_numero(numero, registro, id_):
    """Número público exige reserva no registro do piloto. LAB- é livre. Devolve lista de falhas de numeração."""
    if numero.startswith("LAB-"):
        return []
    if not (registro and id_):
        return [f"número público {numero} exige --registro e --id (o número precisa estar RESERVADO antes da composição)"]
    sys.path.insert(0, str(AQUI))
    from registro_numeracao import ler, achar, Erro, verificar
    from filtros import normalizar_estado
    try:
        linhas, _ = ler(registro)
        l = achar(linhas, id_)
    except (Erro, OSError) as e:
        return [f"registro: {e}"]
    f = []
    if normalizar_estado(l.get("estado")) != "RESERVADO":
        f.append(f"{id_} está em {normalizar_estado(l.get('estado'))}; o número só pode ser usado se estiver RESERVADO")
    if str(l.get("numero", "")).strip() != numero:
        f.append(f"número {numero} difere do reservado para {id_} ('{l.get('numero')}')")
    f += [f"registro inconsistente: {x}" for x in verificar(registro)]
    return f


def compor(foto, na_foto, fora, numero, saida, perfil="A", simulacao=False, guias=False, carimbo=None, rascunho=False, registro=None, id_=None):
    L = PERFIS[perfil]
    falhas, avisos = [], []
    if "—" in na_foto + fora:
        falhas.append("travessão no texto (reescrever é decisão editorial de Eri)")
    num_falhas = checar_numero(numero, registro, id_)
    base = fundo_foto(foto) if foto else fundo_neutro()
    img = degrade(base, L)
    d0 = ImageDraw.Draw(img)
    larg = W - 2 * L["margem"]
    caixas = {}
    # medidas e ajuste de corpo (sem alterar o texto)
    fr = fonte("SemiBold", L["rotulo_px"])
    ff, lf, pxf, estf = ajustar(d0, fora, L["fora_peso"], L["fora_px"], L["fora_min_px"], L["fora_max_linhas"], larg)
    fn_, ln, pxn, estn = ajustar(d0, na_foto, "Regular", L["na_foto_px"], L["na_foto_min_px"], L["na_foto_max_linhas"], larg)
    if estf: falhas.append(f"FORA não cabe em {L['fora_max_linhas']} linhas no corpo mínimo ({L['fora_min_px']} px)")
    if estn: falhas.append(f"NA FOTO não cabe em {L['na_foto_max_linhas']} linhas no corpo mínimo ({L['na_foto_min_px']} px)")
    if pxf < L["fora_px"] or pxn < L["na_foto_px"]:
        avisos.append(f"corpo reduzido para caber (NA FOTO {pxn} px, FORA {pxf} px); a hierarquia visual mudou")
    hf = int(pxf * L["entrelinha"]) * len(lf); hn = int(pxn * L["entrelinha"]) * len(ln)
    y_f_txt = L["fora_base_y"] - hf
    y_f_rot = y_f_txt - L["gap_rotulo"] - L["rotulo_px"]
    y_n_txt = y_f_rot - L["gap_blocos"] - hn
    y_n_rot = y_n_txt - L["gap_rotulo"] - L["rotulo_px"]
    # camada de texto (para sombra opcional)
    tl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(tl)
    ft, fnum = fonte("SemiBold", L["titulo_px"]), fonte("Medium", L["numero_px"])
    caixas["titulo"] = texto_trk(d, (L["margem"], L["titulo_y"]), "O QUE NINGUÉM LEGENDA", ft, BRANCO + (240,), L["titulo_trk"])
    rot_num = numero if numero.startswith("LAB") else f"Nº {numero}"
    caixas["numero"] = texto_trk(d, (W - L["margem"], L["titulo_y"]), rot_num, fnum, BRANCO + (225,), L["numero_trk"], "r")
    caixas["rotulo_na_foto"] = texto_trk(d, (L["margem"], y_n_rot), "NA FOTO", fr, BRANCO + (L["rotulo_alpha"],), L["rotulo_trk"])
    for i, l in enumerate(ln):
        y = y_n_txt + i * int(pxn * L["entrelinha"])
        d.text((L["margem"], y), l, font=fn_, fill=BRANCO + (L["na_foto_alpha"],))
        caixas[f"na_foto_{i+1}"] = (L["margem"], y, L["margem"] + d.textlength(l, font=fn_), y + int(pxn * 1.2))
    d.line([(L["margem"], y_f_rot - L["gap_blocos"] // 2), (L["margem"] + 64, y_f_rot - L["gap_blocos"] // 2)], fill=BRANCO + (150,), width=3)
    caixas["rotulo_fora"] = texto_trk(d, (L["margem"], y_f_rot), "FORA DO ENQUADRAMENTO", fr, BRANCO + (L["rotulo_alpha"],), L["rotulo_trk"])
    for i, l in enumerate(lf):
        y = y_f_txt + i * int(pxf * L["entrelinha"])
        d.text((L["margem"], y), l, font=ff, fill=BRANCO + (L["fora_alpha"],))
        caixas[f"fora_{i+1}"] = (L["margem"], y, L["margem"] + d.textlength(l, font=ff), y + int(pxf * 1.2))
    caixas["assinatura"] = texto_trk(d, (L["margem"], L["assinatura_y"]), "@surtodelucidez", fonte("Medium", L["assinatura_px"]), BRANCO + (L["assinatura_alpha"],), L["assinatura_trk"])
    # zonas de segurança e margens
    for nome, (x0, y0, x1, y1) in caixas.items():
        if y0 < L["zona_topo"]: falhas.append(f"{nome} invade a zona de segurança superior ({L['zona_topo']} px)")
        if y1 > H - L["zona_base"]: falhas.append(f"{nome} invade a zona de segurança inferior (começa em {H - L['zona_base']} px)")
        if x0 < L["margem"] - 2 or x1 > W - L["margem"] + 2: falhas.append(f"{nome} excede as margens laterais")
    if y_n_rot < L["zona_topo"] + 400:
        avisos.append("blocos de texto muito altos: ocupam a área central da foto")
    if L["sombra"]:
        sh = tl.split()[3].filter(ImageFilter.GaussianBlur(9)).point(lambda v: int(v * L["sombra"]))
        sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sombra.putalpha(sh)
        img = Image.alpha_composite(img, sombra)
    img = Image.alpha_composite(img, tl)
    d = ImageDraw.Draw(img)
    if simulacao:
        d.rectangle([0, 430, W, 498], fill=(190, 30, 30, 235))
        d.text((W // 2, 464), carimbo or "SIMULAÇÃO VISUAL · NÃO É ARTE APROVADA", font=fonte("SemiBold", 32), fill=BRANCO, anchor="mm")
    todas = falhas + num_falhas
    if todas and rascunho:
        d.rectangle([0, 1620, W, 1688], fill=(120, 0, 120, 235))
        d.text((W // 2, 1654), "NÃO APTA TECNICAMENTE · RASCUNHO", font=fonte("SemiBold", 32), fill=BRANCO, anchor="mm")
    if guias:
        g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        gd.rectangle([0, 0, W, L["zona_topo"]], fill=(255, 0, 0, 70)); gd.rectangle([0, H - L["zona_base"], W, H], fill=(255, 0, 0, 70))
        gd.rectangle([L["margem"], L["zona_topo"], W - L["margem"], H - L["zona_base"]], outline=(0, 255, 255, 200), width=2)
        gd.text((10, 10), f"zona topo {L['zona_topo']} px (provisória)", font=fonte("Medium", 24), fill=(255, 255, 255, 255))
        gd.text((10, H - L["zona_base"] + 10), f"zona base {L['zona_base']} px (provisória)", font=fonte("Medium", 24), fill=(255, 255, 255, 255))
        img = Image.alpha_composite(img, g)
    relatorio = {"perfil": perfil, "numero": numero, "aprovacao_tecnica": not todas, "falhas": falhas, "falhas_numeracao": num_falhas, "avisos": avisos,
                 "texto_alterado": False, "medidas": {"linhas_na_foto": len(ln), "linhas_fora": len(lf), "px_na_foto": pxn, "px_fora": pxf, "y_inicio_blocos": y_n_rot, "y_assinatura": L["assinatura_y"]},
                 "simulacao": simulacao, "aprovacao_visual": "pendente de Eri (a skill nunca aprova arte)"}
    if not todas or rascunho:
        img.convert("RGB").save(saida)
        relatorio["png_sha256"] = hashlib.sha256(Path(saida).read_bytes()).hexdigest()
    Path(str(saida) + ".checagem.json").write_text(json.dumps(relatorio, ensure_ascii=False, indent=1), encoding="utf-8")
    return relatorio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--foto"); ap.add_argument("--na-foto", required=True); ap.add_argument("--fora", required=True)
    ap.add_argument("--numero", required=True); ap.add_argument("--saida", required=True)
    ap.add_argument("--perfil", choices=list(PERFIS), default="A")
    ap.add_argument("--simulacao", action="store_true"); ap.add_argument("--guias", action="store_true"); ap.add_argument("--rascunho", action="store_true")
    ap.add_argument("--carimbo"); ap.add_argument("--registro"); ap.add_argument("--id")
    a = ap.parse_args()
    if not a.simulacao and not a.foto:
        sys.exit("informe --foto ou use --simulacao")
    r = compor(a.foto, a.na_foto, a.fora, a.numero, a.saida, a.perfil, a.simulacao, a.guias, a.carimbo, a.rascunho, a.registro, a.id)
    print(json.dumps(r["medidas"], ensure_ascii=False))
    for v in r["avisos"]: print("AVISO:", v)
    if r["aprovacao_tecnica"]:
        print("APROVAÇÃO TÉCNICA: SIM (a aprovação visual continua sendo de Eri)")
        return 0
    for v in r["falhas"] + r["falhas_numeracao"]: print("BLOQUEIO:", v, file=sys.stderr)
    print("APROVAÇÃO TÉCNICA: NÃO" + ("" if a.rascunho else "; arte não gravada"), file=sys.stderr)
    return 3 if r["falhas_numeracao"] else 2


if __name__ == "__main__":
    sys.exit(main())
