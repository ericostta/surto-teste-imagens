#!/usr/bin/env python3
"""Filtros determinísticos e comparação com histórico (O QUE NINGUÉM LEGENDA, Fase A).
CÓPIA para o piloto manual v0.1; o original do laboratório (filtros.py) não foi alterado. Única mudança: o histórico vem de registro_piloto.csv ou de --registro ARQ.

Uso:
    python3 filtros.py CANDIDATAS.json [--saida RESULTADO.json]

CANDIDATAS.json: lista de objetos com os campos
    id, tema, situacao, mecanismo (M01..M12), emocao, tipo_contraste,
    na_foto, fora, conceito_foto, rosto (bool)

Saída: para cada candidata, "falhas" (eliminam) e "alertas" (apenas sinalizam).
Não há verificação ortográfica aqui (fica com o Auditor). Não há nota de qualidade.
"""
import csv
import json
import re
import sys
import unicodedata
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CONFIG = json.loads((AQUI / "config.json").read_text(encoding="utf-8"))
TAXO = json.loads((AQUI / "taxonomia.json").read_text(encoding="utf-8"))
REGISTRO = AQUI / "registro_piloto.csv"  # CÓPIA do piloto v0.1: histórico em registro_piloto.csv (ou --registro ARQ)


def norm(texto: str) -> str:
    """minúsculas, sem acento, só letras/números/espaço."""
    t = unicodedata.normalize("NFD", texto.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def palavras(texto: str) -> list:
    return norm(texto).split()


STOP = set("""
a o as os um uma uns umas de do da dos das em no na nos nas por para com sem sobre ate
e ou mas que se como mais menos muito pouco ja so ainda ate nem nao sim ele ela eles elas
seu sua seus suas dele dela isso isto esse essa este esta estao esta foi era ser ter tem
ha vez quem qual onde quando todo toda todos todas cada outro outra nunca sempre antes depois
""".split())


def palavras_conteudo(texto: str) -> list:
    """Palavras com mais de 3 letras e fora da lista de palavras vazias."""
    return [p for p in palavras(texto) if len(p) > 3 and p not in STOP]


def jaccard(a: list, b: list) -> float:
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb) if sa and sb else 0.0


def similaridade_texto(a: str, b: str) -> float:
    """Similaridade sobre palavras de conteúdo (ignora palavras vazias):
    máximo entre Jaccard e razão de sequência."""
    ca, cb = palavras_conteudo(a), palavras_conteudo(b)
    if not ca or not cb:
        return 0.0
    return max(jaccard(ca, cb), SequenceMatcher(None, " ".join(ca), " ".join(cb)).ratio())


def contem_termo(texto_norm: str, termo: str, palavra_inteira: bool = False) -> bool:
    t = norm(termo)
    if not t:
        return False
    # por padrão, termos casam por prefixo de palavra (ex.: "suicid" casa "suicidio")
    padrao = r"\b" + re.escape(t) + (r"\b" if palavra_inteira else "")
    return re.search(padrao, texto_norm) is not None


def mencao_afirmativa(texto_norm: str, termo: str) -> bool:
    """Termo como palavra inteira e NÃO negado ('sem texto', 'nem logotipo', 'nenhum texto')."""
    t = norm(termo)
    for m in re.finditer(r"\b" + re.escape(t) + r"\b", texto_norm):
        antes = texto_norm[: m.start()].split()[-4:]
        if not any(p in ("sem", "nem", "nenhum", "nenhuma") for p in antes):
            return True
    return False


def carregar_historico() -> list:
    if not REGISTRO.exists():
        return []
    with REGISTRO.open(encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f) if r.get("estado") in ("TEXTO_APROVADO", "ARTE_VALIDADA", "NA_FILA", "PUBLICADA")]


def avaliar(c: dict, historico: list, lote: list) -> dict:
    falhas, alertas = [], []
    # uma candidata não se compara com o próprio registro nem com a versão que está revisando
    # (ids de revisão têm sufixo -r1, -r2...; a base é o id sem o sufixo)
    base_id = re.sub(r"-r\d+$", "", c.get("id", ""))
    historico = [h for h in historico if h.get("id") not in (c.get("id"), base_id)]
    lote = [o for o in lote if re.sub(r"-r\d+$", "", o.get("id", "")) != base_id]
    lim = CONFIG["limites_texto"]
    hist_cfg = CONFIG["historico"]

    na_foto, fora = c.get("na_foto", ""), c.get("fora", "")
    conceito = c.get("conceito_foto", "")
    texto_publico = f"{na_foto} {fora}"
    tn = norm(texto_publico)

    # 1. estrutura e tamanho
    for campo in ("id", "tema", "mecanismo", "emocao", "na_foto", "fora", "conceito_foto"):
        if not c.get(campo):
            falhas.append(f"campo ausente: {campo}")
    n_nf, n_fora = len(palavras(na_foto)), len(palavras(fora))
    if n_nf > lim["na_foto_max_palavras"]:
        falhas.append(f"NA FOTO com {n_nf} palavras (máx {lim['na_foto_max_palavras']})")
    if n_fora > lim["fora_max_palavras"]:
        falhas.append(f"FORA DO ENQUADRAMENTO com {n_fora} palavras (máx {lim['fora_max_palavras']})")
    if 0 < n_fora < lim["fora_min_palavras"]:
        alertas.append(f"FORA DO ENQUADRAMENTO muito curto ({n_fora} palavras)")
    if c.get("mecanismo") and c["mecanismo"] not in TAXO["mecanismos"]:
        falhas.append(f"mecanismo fora da taxonomia: {c['mecanismo']}")
    if c.get("emocao") and c["emocao"] not in TAXO["emocoes"]:
        falhas.append(f"emoção fora da taxonomia: {c['emocao']}")

    # 2. pontuação proibida pelo estilo de Eri (travessão no meio de frases)
    if "—" in texto_publico or "–" in texto_publico:
        falhas.append("travessão no texto público")
    if re.search(r"\s{2,}", texto_publico):
        alertas.append("espaços duplicados")

    # 3. vetos temáticos (falha)
    for grupo, termos in TAXO["vetos_tematicos"].items():
        achados = [t for t in termos if contem_termo(tn, t)]
        if achados:
            falhas.append(f"veto temático ({grupo}): {', '.join(achados)}")
    marcas = [m for m in TAXO["marcas_e_pessoas_reais"] if contem_termo(tn, m)]
    if marcas:
        falhas.append(f"marca ou pessoa real: {', '.join(marcas)}")
    if re.search(r"\d+\s?%|\b\d{1,3}(\.\d{3})+\b", texto_publico):
        falhas.append("dado numérico ou estatística no texto público")

    # 4. linguagem proibida pelo DNA (autoajuda, moralismo, abstração, melodrama)
    for chave, rotulo in (("lexico_autoajuda_e_moralismo", "autoajuda ou moralismo"),
                          ("lexico_abstracao_excessiva", "abstração excessiva"),
                          ("lexico_melodrama", "melodrama")):
        achados = [t for t in TAXO[chave] if contem_termo(tn, t)]
        if achados:
            falhas.append(f"{rotulo}: {', '.join(achados)}")

    # 5. redundância entre foto e texto (regra absoluta do DNA)
    pn, pf = palavras(na_foto), palavras(fora)
    sobreposicao = jaccard(palavras_conteudo(na_foto), palavras_conteudo(fora))
    if sobreposicao >= 0.5:
        falhas.append(f"FORA repete NA FOTO (sobreposição {sobreposicao:.2f})")
    elif sobreposicao >= 0.3:
        alertas.append(f"possível redundância entre NA FOTO e FORA (sobreposição {sobreposicao:.2f})")

    # 6. conceito fotográfico
    cn = norm(conceito)
    for termo in TAXO["regras_foto"]["termos_de_alerta_no_conceito"]:
        if mencao_afirmativa(cn, termo):
            alertas.append(f"conceito fotográfico menciona '{termo}' (a foto não pode conter texto)")
    if not isinstance(c.get("rosto"), bool):
        falhas.append("campo rosto deve ser true ou false")

    # 7. similaridade textual com histórico e com o próprio lote
    comparativos = [(h["id"], f"{h['na_foto']} {h['fora_do_enquadramento']}") for h in historico]
    comparativos += [(o["id"], f"{o.get('na_foto','')} {o.get('fora','')}") for o in lote if o["id"] != c.get("id")]
    max_sim, com_quem = 0.0, None
    for oid, otexto in comparativos:
        s = similaridade_texto(texto_publico, otexto)
        if s > max_sim:
            max_sim, com_quem = s, oid
    if max_sim >= hist_cfg["similaridade_texto_falha"]:
        falhas.append(f"quase repetição de {com_quem} (similaridade {max_sim:.2f})")
    elif max_sim >= hist_cfg["similaridade_texto_alerta"]:
        alertas.append(f"semelhante a {com_quem} (similaridade {max_sim:.2f})")

    # 8. repetição estrutural (mecanismo, abertura sintática, objeto central)
    recentes = historico[-hist_cfg["janela_mecanismo"]:]
    if c.get("mecanismo") and any(h["mecanismo"] == c["mecanismo"] for h in recentes):
        alertas.append(f"mecanismo {c['mecanismo']} já usado nas últimas {hist_cfg['janela_mecanismo']} edições")
    abertura = " ".join(pf[:3])
    janela = historico[-hist_cfg["janela_abertura_sintatica"]:]
    if abertura and any(" ".join(palavras(h["fora_do_enquadramento"])[:3]) == abertura for h in janela):
        alertas.append(f"abertura sintática repetida: '{abertura}'")

    # 9. cota de rosto (últimas 10 + esta)
    ultimas = historico[-9:]
    com_rosto = sum(1 for h in ultimas if str(h.get("rosto")).lower() == "true") + (1 if c.get("rosto") is True else 0)
    if c.get("rosto") is True and com_rosto > CONFIG["rostos"]["max_por_10_edicoes"]:
        falhas.append("cota de rostos excedida (máx 2 a cada 10)")

    # 10. concentração emocional (alerta, nunca veto)
    emocoes = [h["emocao"] for h in historico[-hist_cfg["janela_emocao"]:]] + ([c["emocao"]] if c.get("emocao") else [])
    if len(emocoes) >= 10:
        emo, qtd = Counter(emocoes).most_common(1)[0]
        if qtd / len(emocoes) > hist_cfg["alerta_concentracao_emocao"]:
            alertas.append(f"concentração emocional em '{emo}' ({qtd}/{len(emocoes)})")

    return {
        "id": c.get("id"),
        "palavras": {"na_foto": n_nf, "fora": n_fora},
        "similaridade_max": {"valor": round(max_sim, 2), "com": com_quem},
        "falhas": falhas,
        "alertas": alertas,
        "passou": not falhas,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    entrada = Path(sys.argv[1])
    saida = None
    if "--saida" in sys.argv:
        saida = Path(sys.argv[sys.argv.index("--saida") + 1])
    if "--registro" in sys.argv:
        global REGISTRO
        REGISTRO = Path(sys.argv[sys.argv.index("--registro") + 1])
    lote = json.loads(entrada.read_text(encoding="utf-8"))
    historico = carregar_historico()
    resultados = [avaliar(c, historico, lote) for c in lote]
    texto = json.dumps(resultados, ensure_ascii=False, indent=2)
    if saida:
        saida.write_text(texto + "\n", encoding="utf-8")
    else:
        print(texto)
    ok = sum(r["passou"] for r in resultados)
    print(f"{ok}/{len(resultados)} passaram nos filtros determinísticos", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
