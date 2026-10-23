#!/usr/bin/env python3
"""Montagem de pacotes cegos para a comparação G3 (instrumento; rascunho G0; não executado sobre itens reais).

pacote_critico: para cada execução, códigos opacos e ordem embaralhados de forma independente (seed + run).
O pacote contém SOMENTE: codigo, conceito_foto, na_foto, fora, previsoes_cegas, textos_anteriores.
Nenhum id, rótulo, origem, versão ou mapa entra no pacote. O mapa fica em arquivo separado.
Embaralhar códigos só evita viés de ordem: não é garantia de independência (ver g1_protecao_conjunto_validacao.md).

pacote_julgador: contexto completo para o julgador de motivos, sem a identificação da versão, com porta de
completude. Elemento obrigatório ausente => inconclusivo_por_pacote = True (o item não é julgado).
"""
import hashlib, json, sys

CAMPOS_ITEM = ("conceito_foto", "na_foto", "fora")
CAMPOS_PACOTE_CRITICO = {"codigo", "conceito_foto", "na_foto", "fora", "previsoes_cegas", "textos_anteriores"}
CAMPOS_REFERENCIA = ("estado", "motivo", "tipo_fundamento", "natureza")


def _h(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def pacote_critico(itens: dict, previsoes: dict, anteriores: list, seed: str, run: int):
    """itens: {id: {conceito_foto, na_foto, fora, ...}} ; previsoes: {id: [3 textos]} ; anteriores: lista de textos."""
    ids = sorted(itens)
    codigos = {}
    for i in ids:
        base = _h(f"{seed}|{run}|cod|{i}")[:6].upper()
        codigos[i] = "C" + base
    assert len(set(codigos.values())) == len(ids), "colisão de códigos; mude a semente"
    ordem = sorted(ids, key=lambda i: _h(f"{seed}|{run}|ord|{i}"))
    pacote, mapa = [], {}
    for i in ordem:
        it = itens[i]
        faltam = [c for c in CAMPOS_ITEM if not str(it.get(c, "")).strip()]
        prev = previsoes.get(i)
        if faltam or not prev or len(prev) != 3:
            raise ValueError(f"item {i}: campos ausentes {faltam} ou previsões != 3")
        p = {"codigo": codigos[i], "conceito_foto": it["conceito_foto"], "na_foto": it["na_foto"], "fora": it["fora"],
             "previsoes_cegas": list(prev), "textos_anteriores": list(anteriores)}
        assert set(p) == CAMPOS_PACOTE_CRITICO
        pacote.append(p)
        mapa[codigos[i]] = i
    return pacote, mapa


def pacote_julgador(codigo: str, item: dict, saida_critico: dict, referencia: dict, anteriores, concorrentes=None):
    faltantes = [c for c in CAMPOS_ITEM if not str(item.get(c, "")).strip()]
    if anteriores is None:
        faltantes.append("textos_anteriores")
    if not isinstance(saida_critico, dict) or not saida_critico.get("veredicto"):
        faltantes.append("saida_critico")
    faltantes += [f"referencia.{c}" for c in CAMPOS_REFERENCIA if not str(referencia.get(c, "")).strip()]
    contestado = bool(referencia.get("contestado"))
    if contestado and not concorrentes:
        faltantes.append("fundamentos_concorrentes")
    saida = {k: v for k, v in (saida_critico or {}).items() if k != "versao_criterio"}  # julgador cego à versão
    pacote = {"codigo": codigo, "conceito_foto": item.get("conceito_foto"), "na_foto": item.get("na_foto"),
              "fora": item.get("fora"), "textos_anteriores": anteriores if anteriores is not None else None,
              "saida_critico": saida, "referencia": {k: referencia.get(k) for k in CAMPOS_REFERENCIA + ("correcao_pontual", "contestado")},
              "fundamentos_concorrentes": concorrentes or [], "faltantes": faltantes,
              "inconclusivo_por_pacote": bool(faltantes)}
    return pacote


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("itens"); ap.add_argument("previsoes"); ap.add_argument("--seed", required=True)
    ap.add_argument("--run", type=int, required=True); ap.add_argument("--anteriores")
    ap.add_argument("--pacote", required=True); ap.add_argument("--mapa", required=True)
    a = ap.parse_args()
    itens = json.load(open(a.itens, encoding="utf-8")); prev = json.load(open(a.previsoes, encoding="utf-8"))
    ant = json.load(open(a.anteriores, encoding="utf-8")) if a.anteriores else []
    pac, mapa = pacote_critico(itens, prev, ant, a.seed, a.run)
    json.dump(pac, open(a.pacote, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(mapa, open(a.mapa, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
