#!/usr/bin/env python3
"""Composição do Story 1080x1920 de O QUE NINGUÉM LEGENDA (PILOTO MANUAL v0.2.1; layout PROVISÓRIO, não homologado).

Uso:
  python3 compor_story.py --foto FOTO.png --na-foto "..." --fora "..." --numero LAB-001 --saida story.png [--perfil A|B|C|D]
  python3 compor_story.py --simulacao [--foto MARCADOR.png] ...    carimba SIMULAÇÃO VISUAL (nunca é arte aprovada)
  --guias    desenha zonas de segurança e margens (conferência; nunca para publicar)
  --registro registro_piloto.csv --id LAB-001    obrigatório para número público (001, 002...): o número precisa estar RESERVADO

Perfis (hipóteses de layout, todas provisórias): A = referência do v0.1; B = degradê mais leve, FORA mais moderado, assinatura mais afastada;
C (padrão da v0.2) = B com as decisões de Eri de 24 a 30/10/2026: rótulos em alfa 215, degradê do topo reforçado, assinatura em 22 px e número
discreto ("001", sem "Nº") abaixo da assinatura, alinhado à esquerda. Aprovação de assinatura e número não aprova o layout inteiro.
D (padrão da v0.2.1) = C com a rodada visual de 30/10/2026 (escolhas de Eri, provisórias): blocos mais baixos, traço divisor de largura total, "001" sob o S e o U,
escurecimento suave localizado (mancha esfumada) atrás do título e do bloco inferior, título em duas linhas (O QUE NINGUÉM pequeno; LEGENDA em serifa reta).
A arte reporta o contraste efetivo do texto (aproximado, sem a sombra do texto); abaixo do limite provisório gera AVISO, nunca bloqueio.

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
    "numero_posicao": "topo_direita", "numero_alpha": 225, "numero_gap": 8,
}
PERFIS = {
    "A": dict(BASE),
    "B": dict(BASE, fora_px=50, fora_min_px=42, fora_peso="Regular", fora_alpha=245, na_foto_px=44, na_foto_alpha=215, rotulo_px=26,
              gap_blocos=52, fora_base_y=1396, assinatura_y=1456,
              grad_base_ini=1010, grad_base_max=0.56, grad_base_fim=0.30, grad_topo_max=0.34, sombra=0.55),
}
PERFIS["C"] = dict(PERFIS["B"], rotulo_alpha=215, grad_topo_max=0.65, grad_topo_fim=480, assinatura_px=22, assinatura_trk=4,
                   numero_posicao="abaixo_assinatura", numero_px=11, numero_trk=3, numero_alpha=165, numero_gap=8)
# Perfil D (v0.2.1): layout escolhido por Eri na rodada visual de 30/10/2026 (Modelo A + escurecimento E1 + titulo N4). Provisório, não homologado.
# Texto à esquerda; blocos cerca de 70 px mais baixos que o C (limitado pela zona inferior provisória de 340 px); traço divisor de largura total;
# "001" sob o S e o U de @surtodelucidez; escurecimento suave localizado (mancha com contorno esfumado) atrás do título e do bloco inferior, sem degradê inferior.
PERFIS["D"] = dict(PERFIS["C"], fora_base_y=1466, assinatura_y=1526, grad_base_ini=1080,
                   numero_posicao="sob_su", divisor="largura_total", divisor_alpha=175, divisor_w=2,
                   titulo_estilo="duas_linhas_serifa", titulo_l1_px=27, titulo_l1_trk=9, titulo_l1_alpha=235,
                   titulo_l2_fonte="EBGaramond-SemiBold.ttf", titulo_l2_px=108, titulo_l2_trk=6, titulo_l2_dx=-4, titulo_l2_dy=18, titulo_altura=150,
                   escurecimento="mancha", mancha_titulo=0.36, mancha_base=0.42, mancha_raio=40, mancha_esfumado=30, mancha_x=40,
                   mancha_titulo_y=(236, 486), mancha_base_acima=50, mancha_base_fim=1612)
PERFIL_PADRAO = "D"
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
    d.text((540, 750), "(gerada manualmente por Eri)", font=fonte("Medium", 34), fill=(225, 228, 232), anchor="mm")
    return im


def mancha(img, box, alpha, raio, esfumado):
    """Escurecimento suave localizado: retângulo de cantos arredondados com contorno esfumado (preto, opacidade alpha)."""
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).rounded_rectangle(box, raio, fill=int(255 * alpha))
    cam = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cam.putalpha(m.filter(ImageFilter.GaussianBlur(esfumado)))
    return Image.alpha_composite(img, cam)


def degrade(base, L, y_topo_bloco=None):
    if L.get("escurecimento") == "mancha":
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); px = ov.load()
        for y in range(min(H, L["grad_topo_fim"])):
            v = int(255 * L["grad_topo_max"] * (1 - y / L["grad_topo_fim"]) ** 1.4)
            for x in range(W): px[x, y] = (0, 0, 0, v)
        img = Image.alpha_composite(base.convert("RGBA"), ov)
        x0, x1 = L["mancha_x"], W - L["mancha_x"]
        img = mancha(img, (x0, L["mancha_titulo_y"][0], x1, L["mancha_titulo_y"][1]), L["mancha_titulo"], L["mancha_raio"], L["mancha_esfumado"])
        return mancha(img, (x0, y_topo_bloco - L["mancha_base_acima"], x1, L["mancha_base_fim"]), L["mancha_base"], L["mancha_raio"], L["mancha_esfumado"])
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


LIMITES_CONTRASTE_PADRAO = {"blocos_media": 4.5, "blocos_pior_decil": 3.0, "discretos_media": 3.0}


def _limites_contraste():
    try:
        return json.loads((AQUI / "config.json").read_text(encoding="utf-8"))["padrao_fotografico"]["contraste_limites_provisorios"]
    except (OSError, KeyError, ValueError):
        return LIMITES_CONTRASTE_PADRAO


def _lum(r, g, b):
    def c(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * c(r) + 0.7152 * c(g) + 0.0722 * c(b)


def medir_contraste(bg, caixas, L, avisos):
    """Contraste efetivo APROXIMADO (relação de luminância WCAG) do texto branco com a transparência real sobre a foto já com degradê,
    sem a sombra do texto (limitação). Limiares provisórios e não homologados: abaixo deles só gera AVISO."""
    lim = _limites_contraste()
    grupos = {"titulo": (["titulo"], 240, "discreto"), "numero": (["numero"], L["numero_alpha"], "discreto"),
              "rotulo NA FOTO": (["rotulo_na_foto"], L["rotulo_alpha"], "bloco"), "NA FOTO texto": ([k for k in caixas if k.startswith("na_foto_")], L["na_foto_alpha"], "bloco"),
              "rotulo FORA": (["rotulo_fora"], L["rotulo_alpha"], "bloco"), "FORA texto": ([k for k in caixas if k.startswith("fora_")], L["fora_alpha"], "bloco"),
              "assinatura": (["assinatura"], L["assinatura_alpha"], "discreto")}
    res = {}
    for nome, (chaves, alfa, tipo) in grupos.items():
        a = alfa / 255
        razoes = []
        for k in chaves:
            x0, y0, x1, y1 = (int(round(v)) for v in caixas[k])
            h = y1 - y0
            reg = bg.crop((max(x0, 0), max(y0 + int(0.2 * h), 0), min(x1, W), min(y1 - int(0.05 * h), H)))
            for r, g, b in reg.getdata():
                lb = _lum(r, g, b)
                lt = _lum(*(round(255 * (a + (1 - a) * v / 255)) for v in (r, g, b)))
                razoes.append((lt + 0.05) / (lb + 0.05))
        if not razoes:
            continue
        razoes.sort()
        media = sum(razoes) / len(razoes); p10 = razoes[int(0.10 * (len(razoes) - 1))]
        item = {"media": round(media, 2), "pior_decil": round(p10, 2)}
        if tipo == "bloco":
            item["abaixo_do_limite"] = media < lim["blocos_media"] or p10 < lim["blocos_pior_decil"]
        else:
            item["abaixo_do_limite"] = media < lim["discretos_media"]
        if item["abaixo_do_limite"]:
            avisos.append(f"contraste efetivo de '{nome}' abaixo do limite provisório (média {item['media']}, pior decil {item['pior_decil']}); limiar não homologado, avaliar a legibilidade")
        res[nome] = item
    return res


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


def compor(foto, na_foto, fora, numero, saida, perfil=PERFIL_PADRAO, simulacao=False, guias=False, carimbo=None, rascunho=False, registro=None, id_=None):
    L = PERFIS[perfil]
    falhas, avisos = [], []
    if "—" in na_foto + fora:
        falhas.append("travessão no texto (reescrever é decisão editorial de Eri)")
    num_falhas = checar_numero(numero, registro, id_)
    base = fundo_foto(foto) if foto else fundo_neutro()
    d0 = ImageDraw.Draw(Image.new("RGBA", (W, H)))   # só para medir texto; o degradê depende da posição dos blocos
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
    img = degrade(base, L, y_n_rot)
    bg_rgb = img.convert("RGB") if foto else None
    # camada de texto (para sombra opcional)
    tl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(tl)
    ft, fnum = fonte("SemiBold", L["titulo_px"]), fonte("Medium", L["numero_px"])
    if L.get("titulo_estilo") == "duas_linhas_serifa":
        # "O QUE NINGUÉM" pequeno e espaçado (Inter SemiBold) sobre "LEGENDA" grande em serifa reta (EB Garamond SemiBold, sem itálico)
        b1 = texto_trk(d, (L["margem"], L["titulo_y"]), "O QUE NINGUÉM", fonte("SemiBold", L["titulo_l1_px"]), BRANCO + (L["titulo_l1_alpha"],), L["titulo_l1_trk"])
        f2 = ImageFont.truetype(str(FONTS / L["titulo_l2_fonte"]), L["titulo_l2_px"])
        b2 = texto_trk(d, (L["margem"] + L["titulo_l2_dx"], L["titulo_y"] + L["titulo_l2_dy"]), "LEGENDA", f2, BRANCO + (255,), L["titulo_l2_trk"])
        caixas["titulo"] = (L["margem"], L["titulo_y"], max(b1[2], b2[2]), L["titulo_y"] + L["titulo_altura"])
    else:
        caixas["titulo"] = texto_trk(d, (L["margem"], L["titulo_y"]), "O QUE NINGUÉM LEGENDA", ft, BRANCO + (240,), L["titulo_trk"])
    # o número é exibido como está (001, sem prefixo); peças de teste exibem LAB-001
    if L["numero_posicao"] == "sob_su":
        fs_ = fonte("Medium", L["assinatura_px"])   # começa depois do "@": fica sob o S e o U de surtodelucidez
        x_su = L["margem"] + largura(d, "@", fs_, L["assinatura_trk"]) + L["assinatura_trk"]
        caixas["numero"] = texto_trk(d, (x_su, L["assinatura_y"] + L["assinatura_px"] + L["numero_gap"]), numero, fnum, BRANCO + (L["numero_alpha"],), L["numero_trk"])
    elif L["numero_posicao"] == "abaixo_assinatura":
        caixas["numero"] = texto_trk(d, (L["margem"], L["assinatura_y"] + L["assinatura_px"] + L["numero_gap"]), numero, fnum, BRANCO + (L["numero_alpha"],), L["numero_trk"])
    else:
        caixas["numero"] = texto_trk(d, (W - L["margem"], L["titulo_y"]), numero, fnum, BRANCO + (L["numero_alpha"],), L["numero_trk"], "r")
    caixas["rotulo_na_foto"] = texto_trk(d, (L["margem"], y_n_rot), "NA FOTO", fr, BRANCO + (L["rotulo_alpha"],), L["rotulo_trk"])
    for i, l in enumerate(ln):
        y = y_n_txt + i * int(pxn * L["entrelinha"])
        d.text((L["margem"], y), l, font=fn_, fill=BRANCO + (L["na_foto_alpha"],))
        caixas[f"na_foto_{i+1}"] = (L["margem"], y, L["margem"] + d.textlength(l, font=fn_), y + int(pxn * 1.2))
    if L.get("divisor") == "largura_total":
        d.line([(L["margem"], y_f_rot - L["gap_blocos"] // 2), (W - L["margem"], y_f_rot - L["gap_blocos"] // 2)], fill=BRANCO + (L["divisor_alpha"],), width=L["divisor_w"])
    else:
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
    contraste = medir_contraste(bg_rgb, caixas, L, avisos) if bg_rgb else None
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
                 "texto_alterado": False, "numero_exibido": numero, "contraste": contraste, "caixas": {k: [round(float(v), 1) for v in c] for k, c in caixas.items() if k in ("titulo", "numero", "assinatura")}, "medidas": {"linhas_na_foto": len(ln), "linhas_fora": len(lf), "px_na_foto": pxn, "px_fora": pxf, "y_inicio_blocos": y_n_rot, "y_assinatura": L["assinatura_y"]},
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
    ap.add_argument("--perfil", choices=list(PERFIS), default=PERFIL_PADRAO)
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
