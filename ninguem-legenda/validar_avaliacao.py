#!/usr/bin/env python3
"""Valida a coerência interna das avaliações do Crítico v2 (determinístico).

Uso: python3 validar_avaliacao.py AVALIACAO.json [AVALIACAO2.json ...]

Regras (derivadas de prompts/critico.md):
- campos obrigatórios presentes;
- APROVADA exige E1, E2, E3 e E4, nenhuma eliminatória e grau de previsão diferente de "previu quase tudo";
- REVISAR exige instrucao_de_revisao com "Errado", "Mudar" e "NÃO pode mudar" (ou "Não pode mudar"), sem eliminatórias;
- REPROVADA exige ao menos uma eliminatória;
- nenhum travessão nos textos.
Modo v2.2 (experimental): ativado quando a avaliação traz versao_criterio == "v2.2". Regras:
- previsão cega não é defeito (categoria "previsibilidade" é inválida);
- APROVADA exige E1 a E5, nenhum defeito demonstrado e nenhuma eliminatória;
- REVISAR exige ao menos um defeito, todos corrigíveis, cada um com categoria da lista, trecho e demonstração, e instrução com "Defeito", "Mudar", "NÃO pode mudar" e menção ao núcleo/acontecimento central;
- REPROVADA exige ao menos um defeito estrutural ou eliminatória;
- aviso (não conta como inconsistência) quando a demonstração usa linguagem hipotética.
Modo v2.3-exp (experimental): versao_criterio == "v2.3-exp". Aplica as regras do v2.2 e acrescenta:
- campos integridade (6 chaves) e imprecisoes_perifericas obrigatórios;
- cada defeito exige classe C (gravidade corrigivel) ou D (gravidade estrutural), relacao_comprometida e justificativa_veredicto;
- veredicto mecânico: D ou eliminatória => REPROVADA; senão C => REVISAR; senão APROVADA (se E1 a E5);
- aviso para demonstração vaga ("falta contexto", "não está clara") curta.
O modo v2.1 permanece idêntico.
Não altera veredictos: só aponta inconsistências para auditoria humana.
"""
import json
import sys
from pathlib import Path

OBRIG = ["codigo", "grau_previsao", "elemento_que_muda", "elo_humano", "parafrase_concreta", "nomeia_emocao_sem_fato",
         "ambiguidades", "generalidade", "evidencias_positivas", "eliminatorias", "defeitos", "veredicto",
         "justificativa_objetiva", "nota"]


CATEGORIAS_V22 = {"relacao_narrativa_insuficiente", "ambiguidade_prejudicial", "contradicao", "plausibilidade_comprometida",
                  "redundancia", "cliche_efetivo", "perda_segunda_leitura", "revelacao_arbitraria", "obscuridade",
                  "sentimentalismo_moralismo", "repeticao", "veto"}
OBRIG_V22 = ["codigo", "versao_criterio", "previsoes_que_capturaram", "elemento_que_muda", "elo_humano", "parafrase_concreta",
             "nomeia_emocao_sem_fato", "ambiguidades", "associacao_mais_comum", "e_a_associacao_mais_comum",
             "perspectiva_especifica", "evidencias_positivas", "defeitos_demonstrados", "observacoes_descartadas",
             "eliminatorias", "veredicto", "justificativa_objetiva", "nota"]
INTEGRIDADE_V23 = ["transformacao_central", "relacao_sustentadora", "implicitos", "necessidade_dos_ausentes",
                   "plausibilidade_sem_invencao", "efeito_na_segunda_leitura"]
VAGAS_V23 = ("falta contexto", "não está clara", "nao esta clara", "não fica claro", "relação não é clara")
HIPOTETICO = ("talvez", "possivelmente", "pode ser que", "poderia ser", "quem sabe")


def avisos_v22(a: dict) -> list:
    out = []
    for d in a.get("defeitos_demonstrados", []) or []:
        t = (d.get("demonstracao", "") or "").lower()
        if any(h in t for h in HIPOTETICO):
            out.append(f"{a.get('codigo')}: demonstração com linguagem hipotética ({d.get('categoria')})")
    return out


def validar_v22(a: dict) -> list:
    erros = []
    for campo in OBRIG_V22:
        if campo not in a:
            erros.append(f"campo ausente: {campo}")
    v = a.get("veredicto")
    ev = set(a.get("evidencias_positivas", []))
    defs = a.get("defeitos_demonstrados", []) or []
    elim = a.get("eliminatorias", []) or []
    for d in defs:
        cat = d.get("categoria")
        if cat not in CATEGORIAS_V22:
            erros.append(f"categoria de defeito inválida: {cat}" + (" (previsão não é defeito)" if cat and "previs" in cat else ""))
        if not (d.get("trecho") or "").strip():
            erros.append(f"defeito '{cat}' sem trecho citado")
        if not (d.get("demonstracao") or "").strip():
            erros.append(f"defeito '{cat}' sem demonstração")
        if d.get("gravidade") not in ("corrigivel", "estrutural"):
            erros.append(f"defeito '{cat}' com gravidade inválida")
    if v == "APROVADA":
        falta = {"E1", "E2", "E3", "E4", "E5"} - ev
        if falta:
            erros.append(f"APROVADA sem evidências obrigatórias: {sorted(falta)}")
        if defs:
            erros.append("APROVADA com defeito demonstrado (deveria ser REVISAR ou REPROVADA)")
        if elim:
            erros.append("APROVADA com eliminatórias")
        if a.get("nomeia_emocao_sem_fato") is True:
            erros.append("APROVADA com emoção nomeada sem fato concreto")
        if a.get("e_a_associacao_mais_comum") is True and (a.get("perspectiva_especifica") in (None, "", "nenhuma", "Nenhuma")):
            erros.append("APROVADA com associação comum e sem perspectiva específica")
    elif v == "REVISAR":
        if not defs:
            erros.append("REVISAR sem defeito demonstrado")
        if any(d.get("gravidade") == "estrutural" for d in defs):
            erros.append("REVISAR com defeito estrutural (deveria ser REPROVADA)")
        if elim:
            erros.append("REVISAR com eliminatórias (deveria ser REPROVADA)")
        ins = a.get("instrucao_de_revisao", "") or ""
        for chave in ("Defeito", "Mudar"):
            if chave not in ins:
                erros.append(f"REVISAR sem '{chave}' na instrução")
        if "pode mudar" not in ins.lower():
            erros.append("REVISAR sem 'não pode mudar' na instrução")
        if "núcleo" not in ins.lower() and "acontecimento central" not in ins.lower():
            erros.append("REVISAR sem preservar explicitamente o núcleo narrativo")
    elif v == "REPROVADA":
        if not elim and not any(d.get("gravidade") == "estrutural" for d in defs):
            erros.append("REPROVADA sem defeito estrutural nem eliminatória")
    else:
        erros.append(f"veredicto inválido: {v}")
    if "—" in json.dumps(a, ensure_ascii=False) or "–" in json.dumps(a, ensure_ascii=False):
        erros.append("travessão no texto")
    return erros


def validar_v23(a: dict) -> list:
    erros = validar_v22(a)
    for campo in ("integridade", "imprecisoes_perifericas"):
        if campo not in a:
            erros.append(f"campo ausente (v2.3-exp): {campo}")
    integ = a.get("integridade")
    if isinstance(integ, dict):
        for k in INTEGRIDADE_V23:
            if k not in integ or integ[k] in (None, ""):
                erros.append(f"integridade sem '{k}'")
    elif "integridade" in a:
        erros.append("integridade deve ser objeto")
    defs = a.get("defeitos_demonstrados", []) or []
    for d in defs:
        cat = d.get("categoria")
        classe = d.get("classe")
        if classe not in ("C", "D"):
            erros.append(f"defeito '{cat}' sem classe C ou D")
        elif (classe == "C") != (d.get("gravidade") == "corrigivel"):
            erros.append(f"defeito '{cat}' com classe {classe} incoerente com gravidade {d.get('gravidade')}")
        for campo in ("relacao_comprometida", "justificativa_veredicto"):
            if not (d.get(campo) or "").strip():
                erros.append(f"defeito '{cat}' sem {campo}")
    for item in a.get("imprecisoes_perifericas", []) or []:
        if not (item.get("trecho") or "").strip() or not (item.get("observacao") or "").strip():
            erros.append("imprecisão periférica sem trecho ou observação")
    v = a.get("veredicto")
    tem_d = any(d.get("classe") == "D" for d in defs) or bool(a.get("eliminatorias"))
    tem_c = any(d.get("classe") == "C" for d in defs)
    if tem_d and v != "REPROVADA":
        erros.append("classe D ou eliminatória exige REPROVADA")
    if (not tem_d) and tem_c and v != "REVISAR":
        erros.append("classe C sem D exige REVISAR")
    if (not tem_d) and (not tem_c) and v != "APROVADA":
        erros.append("sem defeitos C ou D o veredicto mecânico é APROVADA (se E1 a E5) ou há defeito sem classe")
    return erros


def avisos_v23(a: dict) -> list:
    out = avisos_v22(a)
    for d in a.get("defeitos_demonstrados", []) or []:
        t = (d.get("demonstracao", "") or "").lower()
        if len(t) < 120 and any(x in t for x in VAGAS_V23):
            out.append(f"{a.get('codigo')}: demonstração vaga ({d.get('categoria')})")
        if d.get("categoria") in ("cliche_efetivo", "redundancia") and ("previs" in t and "corrobora" not in t and len(t) < 160):
            out.append(f"{a.get('codigo')}: defeito {d.get('categoria')} parece apoiado só na previsão")
    return out


def validar(a: dict) -> list:
    if a.get("versao_criterio") == "v2.3-exp":
        return validar_v23(a)
    if a.get("versao_criterio") == "v2.2":
        return validar_v22(a)
    erros = []
    for campo in OBRIG:
        if campo not in a:
            erros.append(f"campo ausente: {campo}")
    v = a.get("veredicto")
    ev = set(a.get("evidencias_positivas", []))
    elim = a.get("eliminatorias", [])
    v21 = "e_a_associacao_mais_comum" in a  # saída do Crítico v2.1
    if v21:
        for campo in ("previsoes_que_capturaram", "associacao_mais_comum", "perspectiva_especifica"):
            if campo not in a:
                erros.append(f"campo ausente (v2.1): {campo}")
        if a.get("e_a_associacao_mais_comum") is True and a.get("perspectiva_especifica") in (None, "", "nenhuma", "Nenhuma") and v == "APROVADA":
            erros.append("APROVADA com revelação igual à associação comum e sem perspectiva específica")
        n = a.get("previsoes_que_capturaram")
        if isinstance(n, int):
            esperado = "previu quase tudo" if n >= 2 else ("previu parte" if n == 1 else "não previu")
            if a.get("grau_previsao") not in (esperado, "previu parte") or (n >= 2 and a.get("grau_previsao") != esperado):
                erros.append(f"grau_previsao '{a.get('grau_previsao')}' incoerente com {n} previsões que capturaram")
    if v == "APROVADA":
        exigidas = {"E1", "E2", "E3", "E4"} | ({"E5"} if v21 else set())
        falta = exigidas - ev
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
        for a in dados:
            if a.get("versao_criterio") == "v2.2":
                for w in avisos_v22(a):
                    print("  aviso: " + w)
            elif a.get("versao_criterio") == "v2.3-exp":
                for w in avisos_v23(a):
                    print("  aviso: " + w)
    print(f"\n{com_erro} de {total} com inconsistência")
    return 0


if __name__ == "__main__":
    sys.exit(main())
