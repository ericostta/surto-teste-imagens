#!/usr/bin/env python3
"""Compara Crítico v1, Crítico v2 (diagnóstico) e os rótulos de Eri no conjunto de calibração 1.

Uso: python3 comparar_v1_v2.py AVALIACAO_V2.json MAPA_CODIGOS.json

AVALIACAO_V2.json: saída do Crítico v2 (lista, campo codigo).
MAPA_CODIGOS.json: codigo -> {conjunto, ref (K01..K18), origem}.
Resultado apenas diagnóstico: o conjunto 1 já foi usado para ajustar o Crítico.
"""
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
EQUIV = {"APROVADA": "BOA", "REVISAR": "AMBÍGUA", "REPROVADA": "RUIM"}
GRAU = {"BOA": 2, "AMBÍGUA": 1, "RUIM": 0}


def main() -> int:
    v2 = {a["codigo"]: a for a in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))}
    mapa = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    eri = json.loads((AQUI / "rotulos_eri.json").read_text(encoding="utf-8"))["rotulos"]
    v1 = json.loads((AQUI / "gabarito_claude.json").read_text(encoding="utf-8"))

    linhas, ac1, ac2, polar1, polar2 = [], 0, 0, 0, 0
    for cod, m in sorted(mapa.items(), key=lambda kv: kv[1]["ref"]):
        if m["conjunto"] != "diag1":
            continue
        k = m["ref"]
        e = eri[k]
        c1 = EQUIV[v1[k]["veredicto_claude"]]
        c2 = EQUIV[v2[cod]["veredicto"]]
        ac1 += c1 == e
        ac2 += c2 == e
        polar1 += abs(GRAU[c1] - GRAU[e]) == 2
        polar2 += abs(GRAU[c2] - GRAU[e]) == 2
        linhas.append((k, m["origem"], e, c1, c2))
    print("item | origem | Eri | v1 | v2")
    for k, o, e, c1, c2 in linhas:
        marca = "" if c2 == e else "  <-- v2 diverge"
        print(f"{k} | {o} | {e} | {c1} | {c2}{marca}")
    n = len(linhas)
    print(f"\nv1 exata: {ac1}/{n} ({ac1/n:.0%}); polares: {polar1}")
    print(f"v2 exata: {ac2}/{n} ({ac2/n:.0%}); polares: {polar2}")
    print("distribuição v2:", dict(Counter(c2 for *_, c2 in linhas)))
    print("distribuição Eri:", dict(Counter(e for _, _, e, *_ in linhas)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
