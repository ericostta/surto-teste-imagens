import sys, copy
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))
import validar_avaliacao as V
base = {"codigo":"T","versao_criterio":"v2.3-exp","previsoes_que_capturaram":1,"elemento_que_muda":"x","elo_humano":"x","parafrase_concreta":"x",
 "nomeia_emocao_sem_fato":False,"ambiguidades":[],"associacao_mais_comum":"x","e_a_associacao_mais_comum":False,"perspectiva_especifica":"x",
 "evidencias_positivas":["E1","E2","E3","E4","E5"],"defeitos_demonstrados":[],"observacoes_descartadas":[],"eliminatorias":[],"veredicto":"APROVADA",
 "justificativa_objetiva":"x","nota":80,"imprecisoes_perifericas":[],
 "integridade":{k:"x" for k in V.INTEGRIDADE_V23}}
dC={"categoria":"relacao_narrativa_insuficiente","classe":"C","trecho":"t","relacao_comprometida":"r","demonstracao":"d","gravidade":"corrigivel","justificativa_veredicto":"j"}
dD={**dC,"categoria":"obscuridade","classe":"D","gravidade":"estrutural"}
ins="Defeito: x. Mudar: y. NÃO pode mudar: o núcleo narrativo."
def caso(nome, mod, esperado_erros):
    a=copy.deepcopy(base); mod(a); e=V.validar(a); ok=(bool(e)==esperado_erros)
    print(("OK  " if ok else "FALHA"), nome, e if e else ""); return ok
r=[]
r.append(caso("aprovada limpa",lambda a:None,False))
r.append(caso("aprovada com B periférico",lambda a:a.update(imprecisoes_perifericas=[{"trecho":"t","observacao":"o"}]),False))
r.append(caso("revisar com C",lambda a:a.update(defeitos_demonstrados=[dC],veredicto="REVISAR",instrucao_de_revisao=ins),False))
r.append(caso("reprovada com D",lambda a:a.update(defeitos_demonstrados=[dD],veredicto="REPROVADA"),False))
r.append(caso("C aprovada (erro)",lambda a:a.update(defeitos_demonstrados=[dC]),True))
r.append(caso("D revisar (erro)",lambda a:a.update(defeitos_demonstrados=[dD],veredicto="REVISAR",instrucao_de_revisao=ins),True))
r.append(caso("sem integridade (erro)",lambda a:a.pop("integridade"),True))
r.append(caso("defeito sem classe (erro)",lambda a:a.update(defeitos_demonstrados=[{k:v for k,v in dC.items() if k!="classe"}],veredicto="REVISAR",instrucao_de_revisao=ins),True))
r.append(caso("classe incoerente (erro)",lambda a:a.update(defeitos_demonstrados=[{**dC,"gravidade":"estrutural"}],veredicto="REVISAR",instrucao_de_revisao=ins),True))
r.append(caso("sem justificativa_veredicto (erro)",lambda a:a.update(defeitos_demonstrados=[{**dC,"justificativa_veredicto":""}],veredicto="REVISAR",instrucao_de_revisao=ins),True))
r.append(caso("travessão (erro)",lambda a:a.update(justificativa_objetiva="a — b"),True))
r.append(caso("previsão como categoria (erro)",lambda a:a.update(defeitos_demonstrados=[{**dC,"categoria":"previsibilidade"}],veredicto="REVISAR",instrucao_de_revisao=ins),True))
print(sum(r),"de",len(r)); sys.exit(0 if all(r) else 1)
