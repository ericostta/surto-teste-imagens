#!/usr/bin/env python3
"""Monta o conjunto de calibração para Eri rotular (sem veredictos) e o gabarito do Claude (separado).

Mistura: candidatas do lote real (boas, médias e ruins segundo o Crítico) + negativos clássicos
que violam o DNA. Ordem embaralhada com semente fixa. Eri nunca vê ids de origem nem veredictos.
"""
import json
import random
from pathlib import Path

AQUI = Path(__file__).resolve().parent
LOTE = AQUI.parent / "lote"

lab = {c["id"]: c for c in json.loads((LOTE / "candidatas.json").read_text(encoding="utf-8"))}
adv = {c["id"]: c for c in json.loads((LOTE / "teste_adversarial.json").read_text(encoding="utf-8"))}
aval = {a["id"]: a for a in json.loads((LOTE / "avaliacao_critico.json").read_text(encoding="utf-8"))["avaliacoes"]}

itens = []
for cid, c in lab.items():
    itens.append({"origem": cid, "tipo": "lote", "na_foto": c["na_foto"], "fora": c["fora"], "foto": c["conceito_foto"],
                  "veredicto_claude": aval[cid]["veredicto"]})

negativos = [
    ("ADV-02-autoajuda", "autoajuda"), ("ADV-03-redundante", "redundante"), ("ADV-04-melodrama", "melodrama"),
    ("ADV-05-moralismo", "moralismo"), ("ADV-06-abstrato", "abstrato"),
]
for cid, rotulo in negativos:
    c = adv[cid]
    itens.append({"origem": cid, "tipo": f"negativo:{rotulo}", "na_foto": c["na_foto"], "fora": c["fora"],
                  "foto": c["conceito_foto"], "veredicto_claude": "REPROVADA"})
itens.append({"origem": "NEG-arbitrario", "tipo": "negativo:conexao_arbitraria", "na_foto": "Uma bicicleta encostada no muro.",
              "fora": "A decisão de nunca mais falar com o irmão.", "foto": "Bicicleta azul encostada num muro de tijolos. Nenhuma pessoa.",
              "veredicto_claude": "REPROVADA"})

random.Random(20261022).shuffle(itens)
for i, it in enumerate(itens, 1):
    it["codigo"] = f"K{i:02d}"

# arquivo para Eri: só código, foto, NA FOTO, FORA
linhas = [
    "# Calibração do Crítico: O QUE NINGUÉM LEGENDA",
    "",
    "São 18 itens, em ordem embaralhada. Para cada um, responda BOA, RUIM ou AMBÍGUA.",
    "Critério único: depois de ler o FORA DO ENQUADRAMENTO, você tem um motivo para olhar a foto de novo?",
    "Comentário é opcional. Pode responder em linhas assim:",
    "",
    "    K01: BOA",
    "    K02: RUIM (previsível)",
    "    K03: AMBÍGUA (não entendi a coragem)",
    "",
    "A foto ainda não existe: o texto abaixo descreve a foto prevista.",
    "",
]
for it in itens:
    linhas += [f"## {it['codigo']}", f"FOTO: {it['foto']}", f"NA FOTO: {it['na_foto']}", f"FORA DO ENQUADRAMENTO: {it['fora']}", ""]
(AQUI / "para_eri.md").write_text("\n".join(linhas), encoding="utf-8")

gabarito = {it["codigo"]: {k: it[k] for k in ("origem", "tipo", "veredicto_claude")} for it in itens}
(AQUI / "gabarito_claude.json").write_text(json.dumps(gabarito, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(itens)} itens gerados")
