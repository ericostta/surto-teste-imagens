#!/usr/bin/env python3
"""Testes do modo v2.4-exp de validar_avaliacao.py, com avaliações SINTÉTICAS escritas à mão.
Não executa Crítico nenhum e não usa itens reais nem de validação."""
import copy, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import validar_avaliacao as V

INTEG = {k: "x" for k in V.INTEGRIDADE_V23}
BASE = {
    "codigo": "T1", "versao_criterio": "v2.4-exp", "previsoes_que_capturaram": 1, "leitura_inicial": "i",
    "elemento_que_muda": "e", "elo_humano": "h", "parafrase_concreta": "p", "nomeia_emocao_sem_fato": False,
    "ambiguidades": [], "integridade": INTEG, "imprecisoes_perifericas": [], "associacao_mais_comum": "a",
    "e_a_associacao_mais_comum": False, "perspectiva_especifica": "especifica", "objecoes": [], "nucleo": {},
    "observacoes_descartadas": [], "divergencia_legitima": "nenhuma", "veredicto": "APROVADA",
    "justificativa_objetiva": "j",
    "merito": {"demonstrado": True, "segunda_leitura": "s", "o_que_muda_na_foto": "m", "elemento_especifico": "el",
               "contribuicao_do_gesto": "nao se aplica", "objecao_relevante": "nenhuma", "por_que_nao_compromete": "nao se aplica"},
}
NUC = {"o_que_preservar": "n", "deficiencia": "d", "intervencao_localizada": "i"}
OBJ_A_CORR = {"fundamento": "A", "categoria": "ambiguidade_prejudicial", "trecho": "t", "argumento": "arg", "gravidade": "corrigivel"}
OBJ_A_ESTR = {"fundamento": "A", "categoria": "obscuridade", "trecho": "t", "argumento": "arg", "gravidade": "estrutural"}
OBJ_B_ESTR = {"fundamento": "B", "categoria": "insuficiencia_editorial", "trecho": "t", "argumento": "arg", "gravidade": "estrutural",
              "leitura_alternativa_mais_favoravel": "leitura favoravel escrita com cuidado e confronto suficiente", "atinge_nucleo": "atinge"}
REV_INS = "Defeito: x. Mudar: y. NÃO pode mudar: o núcleo narrativo e o acontecimento central."

def mk(**kw):
    a = copy.deepcopy(BASE)
    for k, v in kw.items():
        if k == "merito":
            a["merito"].update(v)
        else:
            a[k] = v
    return a

def erros(a): return V.validar(a)

casos = []
def caso(nome, a, esperado_ok, trecho=None):
    e = erros(a)
    ok = (not e) if esperado_ok else (bool(e) and (trecho is None or any(trecho in x for x in e)))
    casos.append((nome, ok, e))

caso("1 APROVADA válida", mk(), True)
caso("2 APROVADA sem elemento_especifico", mk(merito={"elemento_especifico": "nao se aplica"}), False, "elemento_especifico")
caso("3 associação comum sem teste de contribuição", mk(e_a_associacao_mais_comum=True), False, "contribuição")
caso("4 associação comum com teste", mk(e_a_associacao_mais_comum=True, merito={"contribuicao_do_gesto": "sem o gesto a leitura some"}), True)
bsem = dict(OBJ_B_ESTR); bsem.pop("atinge_nucleo")
caso("5 B bloqueante sem atinge_nucleo", mk(veredicto="REPROVADA", objecoes=[bsem], merito={"demonstrado": False}), False, "atinge_nucleo")
caso("6 C com gravidade corrigivel", mk(objecoes=[dict(OBJ_A_CORR, fundamento="C")], veredicto="REVISAR", nucleo=NUC, instrucao_de_revisao=REV_INS), False, "fundamento C")
caso("7 REVISAR válido (A corrigível)", mk(objecoes=[OBJ_A_CORR], veredicto="REVISAR", nucleo=NUC, instrucao_de_revisao=REV_INS), True)
caso("8 REVISAR sem núcleo", mk(objecoes=[OBJ_A_CORR], veredicto="REVISAR", instrucao_de_revisao=REV_INS), False, "nucleo")
caso("9 REVISAR por mérito não demonstrado, com núcleo", mk(veredicto="REVISAR", nucleo=NUC, instrucao_de_revisao=REV_INS, merito={"demonstrado": False}), True)
caso("10 REPROVADA por mérito sem objeção estrutural", mk(veredicto="REPROVADA", merito={"demonstrado": False}), False, "estrutural")
caso("11 REPROVADA válida (B estrutural)", mk(veredicto="REPROVADA", objecoes=[OBJ_B_ESTR], merito={"demonstrado": False}), True)
caso("12 estrutural com REVISAR", mk(veredicto="REVISAR", objecoes=[OBJ_A_ESTR], nucleo=NUC, instrucao_de_revisao=REV_INS), False, "estrutural")
caso("13 APROVADA com objeção corrigível", mk(objecoes=[OBJ_A_CORR]), False)
peri = {"fundamento": "A", "categoria": "ambiguidade_prejudicial", "trecho": "t", "argumento": "arg", "gravidade": "periferica"}
caso("14 periférica sem por_que_nao_compromete", mk(objecoes=[peri]), False, "periférica")
caso("15 periférica com justificativa", mk(objecoes=[peri], merito={"por_que_nao_compromete": "não toca a relação central"}), True)
dv_ok = {"interpretacoes": [{"veredicto": "APROVADA", "fundamento": "f1"}, {"veredicto": "REVISAR", "fundamento": "f2"}], "material": True, "razao_sem_consenso": "r"}
caso("16 divergência material válida", mk(divergencia_legitima=dv_ok), True)
dv_ruim = {"interpretacoes": [{"veredicto": "REVISAR", "fundamento": "f1"}, {"veredicto": "REPROVADA", "fundamento": "f2"}], "material": True, "razao_sem_consenso": "r"}
caso("17 divergência 'material' entre REVISAR e REPROVADA", mk(divergencia_legitima=dv_ruim), False, "divergência material")
caso("18 divergência com uma interpretação só", mk(divergencia_legitima={"interpretacoes": [{"veredicto": "APROVADA", "fundamento": "f"}], "material": True, "razao_sem_consenso": "r"}), False, "duas interpretações")
caso("19 travessão", mk(justificativa_objetiva="a — b"), False, "travessão")
caso("20 emoção nomeada em APROVADA", mk(nomeia_emocao_sem_fato=True), False, "emoção")
caso("21 mérito não demonstrado com APROVADA", mk(merito={"demonstrado": False}), False, "mérito")
caso("22 categoria B com fundamento A", mk(objecoes=[dict(OBJ_B_ESTR, fundamento="A")], veredicto="REPROVADA", merito={"demonstrado": False}), False, "não admite fundamento A")
caso("23 campo ausente", {k: v for k, v in BASE.items() if k != "merito"}, False, "campo ausente")

falhas = [c for c in casos if not c[1]]
for nome, ok, e in casos:
    print(("ok   " if ok else "FALHA"), nome, "" if ok else e)
print(f"\n{len(casos) - len(falhas)} de {len(casos)} casos conforme o esperado")
sys.exit(1 if falhas else 0)
