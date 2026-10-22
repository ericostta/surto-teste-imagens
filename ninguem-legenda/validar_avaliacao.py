#!/usr/bin/env python3
"""Valida a coerência interna das avaliações do Crítico v2 (determinístico).

Uso: python3 validar_avaliacao.py AVALIACAO.json [AVALIACAO2.json ...]

Regras (derivadas de prompts/critico.md):
- campos obrigatórios presentes;
- APROVADA exige E1, E2, E3 e E4, nenhuma eliminatória e grau de previsão diferente de "previu quase tudo";
- REVISAR exige instrucao_de_revisao com "Errado", "Mudar" e "NÃO pode mudar" (ou "Não pode mudar"), sem eliminatórias;
- REPROVADA exige ao menos uma eliminatória;
- nenhum travessão nos textos.
Não altera veredictos: só aponta inconsistências para auditoria humana.
"""
import json
import sys
from pathlib import Path

OBRIG = ["codigo", "grau_previsao", "elemento_que_muda", "elo_humano", "parafrase_concreta", "nomeia_emocao_sem_fato",
         "ambiguidades", "generalidade", "evidencias_positivas", "eliminatorias", "defeitos", "veredicto",
         "justificativa_objetiva", "nota"]


def validar(a: dict) -> list:
    erros = []
    for campo in OBRIG:
        if campo not in a:
            erros.append(f"campo ausente: {campo}")
    v = a.get("veredicto")
    ev = set(a.get("evidencias_positivas", []))
    elim = a.get("eliminatorias", [])
    if v == "APROVADA":
        falta = {"E1", "E2", "E3", "E4"} - ev
        if falta:
            erros.append(f"APROVADA sem evidências obrigatórias: {sorted(falta)}")
        if elim:
            erros.append("APROVADA com eliminatórias")
        if a.get("grau_previsao") == "previu quase tudo":
            erros.append("APROVADA com previsão 'previu quase tudo'")
        if a.get("nomeia_emocao_sem_fato") is True:
            erros.append("APROVADA com emoção nomeada sem fato concreto")
    elif v == "REVISAR":
        ins = a.get("instrucao_de_revisao", "") or ""
        for chave in ("Errado", "Mudar"):
            if chave not in ins:
                erros.append(f"REVISAR sem '{chave}' na instrução")
        if "pode mudar" not in ins.lower():
            erros.append("REVISAR sem 'não pode mudar' na instrução")
        if elim:
            erros.append("REVISAR com eliminatórias (deveria ser REPROVADA)")
    elif v == "REPROVADA":
        if not elim:
            erros.append("REPROVADA sem eliminatória registrada")
    else:
        erros.append(f"veredicto inválido: {v}")
    if "—" in json.dumps(a, ensure_ascii=False) or "–" in json.dumps(a, ensure_ascii=False):
        erros.append("travessão no texto")
    return erros


def main() -> int:
    total, com_erro = 0, 0
    for caminho in sys.argv[1:]:
        dados = json.loads(Path(caminho).read_text(encoding="utf-8"))
        if isinstance(dados, dict):
            dados = list(dados.values())
        print(f"== {caminho}")
        for a in dados:
            total += 1
            e = validar(a)
            if e:
                com_erro += 1
                print(f"  {a.get('codigo')} ({a.get('veredicto')}): " + "; ".join(e))
        print(f"  {len(dados)} avaliações")
    print(f"\n{com_erro} de {total} com inconsistência")
    return 0


if __name__ == "__main__":
    sys.exit(main())
