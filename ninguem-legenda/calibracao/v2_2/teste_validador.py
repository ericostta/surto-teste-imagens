#!/usr/bin/env python3
"""Testes sintéticos do modo v2.2 do validador. Uso: python3 -I calibracao/v2_2/teste_validador.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from validar_avaliacao import validar

base = {"codigo": "T", "versao_criterio": "v2.2", "previsoes_que_capturaram": 3, "elemento_que_muda": "a -> b", "elo_humano": "x",
        "parafrase_concreta": "y", "nomeia_emocao_sem_fato": False, "ambiguidades": [], "associacao_mais_comum": "z",
        "e_a_associacao_mais_comum": False, "perspectiva_especifica": "detalhe", "evidencias_positivas": ["E1", "E2", "E3", "E4", "E5"],
        "defeitos_demonstrados": [], "observacoes_descartadas": [], "eliminatorias": [], "veredicto": "APROVADA",
        "justificativa_objetiva": "ok", "nota": 80}
def com(**k):
    d = dict(base); d.update(k); return d
defc = {"categoria": "ambiguidade_prejudicial", "trecho": "o dele", "demonstracao": "duas leituras incompatíveis", "gravidade": "corrigivel"}
defe = {"categoria": "revelacao_arbitraria", "trecho": "x", "demonstracao": "elo inventado", "gravidade": "estrutural"}
ins_ok = "Defeito: ambiguidade em 'o dele'. Mudar: trocar o pronome. NÃO pode mudar: o núcleo narrativo e o acontecimento central."
casos = [
 ("APROVADA previsível, 3 de 3 capturaram (válida)", com(), 0),
 ("APROVADA sem E5", com(evidencias_positivas=["E1", "E2", "E3", "E4"]), 1),
 ("APROVADA com defeito demonstrado", com(defeitos_demonstrados=[defc]), 1),
 ("REVISAR válida", com(veredicto="REVISAR", evidencias_positivas=["E1"], defeitos_demonstrados=[defc], instrucao_de_revisao=ins_ok), 0),
 ("REVISAR só por previsibilidade (sem defeito)", com(veredicto="REVISAR", instrucao_de_revisao=ins_ok), 1),
 ("REVISAR com categoria previsibilidade", com(veredicto="REVISAR", defeitos_demonstrados=[{**defc, "categoria": "previsibilidade"}], instrucao_de_revisao=ins_ok), 1),
 ("REVISAR sem trecho", com(veredicto="REVISAR", defeitos_demonstrados=[{**defc, "trecho": ""}], instrucao_de_revisao=ins_ok), 1),
 ("REVISAR sem núcleo na instrução", com(veredicto="REVISAR", defeitos_demonstrados=[defc], instrucao_de_revisao="Defeito: x. Mudar: y. NÃO pode mudar: a foto."), 1),
 ("REVISAR com defeito estrutural", com(veredicto="REVISAR", defeitos_demonstrados=[defe], instrucao_de_revisao=ins_ok), 1),
 ("REPROVADA válida", com(veredicto="REPROVADA", defeitos_demonstrados=[defe]), 0),
 ("REPROVADA só por previsão (sem defeito)", com(veredicto="REPROVADA"), 1),
 ("travessão no texto", com(justificativa_objetiva="a — b"), 1),
]
falhas = 0
for nome, a, esperado in casos:
    n = len(validar(a))
    ok = (n > 0) == (esperado > 0)
    falhas += (not ok)
    print(("OK   " if ok else "FALHA"), nome, f"({n} erros)")
print(f"\n{falhas} falhas")
sys.exit(1 if falhas else 0)
