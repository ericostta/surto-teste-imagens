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
Modo v2.4-exp (rascunho G0, instrumento; não executado): versao_criterio == "v2.4-exp". Regras independentes das anteriores:
- campos obrigatórios; integridade com 6 chaves; merito com os campos definidos;
- cada objeção com fundamento A/B/C, categoria da lista, trecho, argumento e gravidade; C só com gravidade "preferencia";
  a categoria NÃO determina o fundamento (decisão de Eri de 22/10, 23h55): qualquer categoria aceita A, B ou C;
  fundamento B bloqueante (corrigivel ou estrutural) exige leitura_alternativa_mais_favoravel e atinge_nucleo;
  gravidade "nao_demonstrada" (só para B, com "lacuna"): falha que o Crítico não conseguiu demonstrar; não decide o estado e não é rebaixada a C;
- elegibilidade_automatica (true só se APROVADA sem divergência material), coerente com veredicto e divergência;
- veredicto mecânico: estrutural => REPROVADA; senão corrigivel => REVISAR (nucleo obrigatório); senão mérito demonstrado => APROVADA;
  mérito não demonstrado => REVISAR com nucleo, ou REPROVADA com objeção estrutural;
- APROVADA exige os quatro elementos de mérito, sem objeção corrigivel ou estrutural, e por_que_nao_compromete quando há objeção periférica;
- divergencia_legitima: "nenhuma" ou objeto com interpretações fundamentadas; material exige APROVADA contra outro estado;
- aviso quando objeção B parece sem confronto real com a leitura favorável.
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


OBRIG_V24 = ["codigo", "versao_criterio", "previsoes_que_capturaram", "leitura_inicial", "elemento_que_muda", "elo_humano",
             "parafrase_concreta", "nomeia_emocao_sem_fato", "ambiguidades", "integridade", "imprecisoes_perifericas",
             "associacao_mais_comum", "e_a_associacao_mais_comum", "perspectiva_especifica", "merito", "objecoes", "nucleo",
             "observacoes_descartadas", "divergencia_legitima", "veredicto", "elegibilidade_automatica", "justificativa_objetiva"]
MERITO_V24 = ["demonstrado", "segunda_leitura", "o_que_muda_na_foto", "elemento_especifico", "contribuicao_do_gesto",
              "objecao_relevante", "por_que_nao_compromete"]
CATEG_V24 = {"relacao_narrativa_insuficiente", "redundancia", "perda_segunda_leitura", "sentimentalismo_moralismo",
             "contradicao", "plausibilidade_comprometida", "ambiguidade_prejudicial", "obscuridade", "repeticao", "veto",
             "cliche_efetivo", "insuficiencia_editorial"}
NUCLEO_V24 = ["o_que_preservar", "deficiencia", "intervencao_localizada"]


def _txt(x) -> str:
    return (x if isinstance(x, str) else "").strip()


def _vazio_ou_nao_se_aplica(x) -> bool:
    return _txt(x).lower() in ("", "nao se aplica", "não se aplica", "nenhuma", "nenhum")


def validar_v24(a: dict) -> list:
    erros = []
    for campo in OBRIG_V24:
        if campo not in a:
            erros.append(f"campo ausente: {campo}")
    n = a.get("previsoes_que_capturaram")
    if "previsoes_que_capturaram" in a and not (isinstance(n, int) and 0 <= n <= 3):
        erros.append("previsoes_que_capturaram deve ser inteiro de 0 a 3")
    integ = a.get("integridade")
    if isinstance(integ, dict):
        for k in INTEGRIDADE_V23:
            if k not in integ or integ[k] in (None, ""):
                erros.append(f"integridade sem '{k}'")
    elif "integridade" in a:
        erros.append("integridade deve ser objeto")
    m = a.get("merito")
    if isinstance(m, dict):
        for k in MERITO_V24:
            if k not in m or m[k] in (None, ""):
                erros.append(f"merito sem '{k}'")
        if not isinstance(m.get("demonstrado"), bool):
            erros.append("merito.demonstrado deve ser true ou false")
    elif "merito" in a:
        erros.append("merito deve ser objeto")
        m = {}
    else:
        m = {}
    objs = a.get("objecoes", []) or []
    for o in objs:
        f = o.get("fundamento"); cat = o.get("categoria"); g = o.get("gravidade")
        if f not in ("A", "B", "C"):
            erros.append(f"objeção '{cat}' com fundamento inválido: {f}")
        if cat not in CATEG_V24:
            erros.append(f"categoria de objeção inválida: {cat}")
        if not _txt(o.get("trecho")):
            erros.append(f"objeção '{cat}' sem trecho")
        if not _txt(o.get("argumento")):
            erros.append(f"objeção '{cat}' sem argumento")
        if g not in ("periferica", "corrigivel", "estrutural", "preferencia", "nao_demonstrada"):
            erros.append(f"objeção '{cat}' com gravidade inválida: {g}")
        if f == "C" and g != "preferencia":
            erros.append(f"objeção '{cat}' de fundamento C só pode ter gravidade 'preferencia'")
        if f in ("A", "B") and g == "preferencia":
            erros.append(f"objeção '{cat}' de fundamento {f} não pode ter gravidade 'preferencia'")
        if g == "nao_demonstrada":
            if f != "B":
                erros.append(f"gravidade 'nao_demonstrada' só vale para fundamento B ('{cat}')")
            if not _txt(o.get("lacuna")):
                erros.append(f"objeção '{cat}' 'nao_demonstrada' sem lacuna")
        if f == "B" and g in ("corrigivel", "estrutural"):
            for campo in ("leitura_alternativa_mais_favoravel", "atinge_nucleo"):
                if not _txt(o.get(campo)):
                    erros.append(f"objeção B bloqueante '{cat}' sem {campo} (registrar como 'nao_demonstrada' com lacuna, não como preferência)")
    estr = [o for o in objs if o.get("gravidade") == "estrutural"]
    corr = [o for o in objs if o.get("gravidade") == "corrigivel"]
    peri = [o for o in objs if o.get("gravidade") in ("periferica", "nao_demonstrada")]
    nuc = a.get("nucleo") if isinstance(a.get("nucleo"), dict) else {}
    nucleo_ok = all(_txt(nuc.get(k)) for k in NUCLEO_V24)
    v = a.get("veredicto")
    demonstrado = m.get("demonstrado") is True
    if estr and v != "REPROVADA":
        erros.append("objeção estrutural exige REPROVADA")
    if (not estr) and corr and v != "REVISAR":
        erros.append("objeção corrigível sem estrutural exige REVISAR")
    if (not estr) and (not corr):
        if demonstrado and v != "APROVADA":
            erros.append("sem objeção bloqueante e com mérito demonstrado o estado é APROVADA")
        if (not demonstrado) and v == "APROVADA":
            erros.append("APROVADA com mérito não demonstrado")
        if (not demonstrado) and v == "REPROVADA":
            erros.append("REPROVADA por mérito não demonstrado exige objeção estrutural fundamentada (insuficiencia_editorial)")
    if v == "APROVADA":
        for k in ("segunda_leitura", "o_que_muda_na_foto", "elemento_especifico"):
            if _vazio_ou_nao_se_aplica(m.get(k)):
                erros.append(f"APROVADA sem merito.{k}")
        if a.get("nomeia_emocao_sem_fato") is True:
            erros.append("APROVADA com emoção nomeada sem fato concreto")
        if a.get("e_a_associacao_mais_comum") is True:
            if _vazio_ou_nao_se_aplica(a.get("perspectiva_especifica")):
                erros.append("APROVADA com associação comum e sem perspectiva específica")
            if _vazio_ou_nao_se_aplica(m.get("contribuicao_do_gesto")):
                erros.append("APROVADA com associação comum sem teste de contribuição do gesto")
        if peri and _vazio_ou_nao_se_aplica(m.get("por_que_nao_compromete")):
            erros.append("APROVADA com objeção periférica sem por_que_nao_compromete")
    elif v == "REVISAR":
        if not nucleo_ok:
            erros.append("REVISAR sem nucleo completo (o_que_preservar, deficiencia, intervencao_localizada)")
        ins = a.get("instrucao_de_revisao", "") or ""
        for chave in ("Defeito", "Mudar"):
            if chave not in ins:
                erros.append(f"REVISAR sem '{chave}' na instrução")
        if "pode mudar" not in ins.lower():
            erros.append("REVISAR sem 'não pode mudar' na instrução")
        if "núcleo" not in ins.lower() and "acontecimento central" not in ins.lower():
            erros.append("REVISAR sem preservar explicitamente o núcleo narrativo")
    elif v == "REPROVADA":
        if not estr:
            erros.append("REPROVADA sem objeção estrutural fundamentada")
    else:
        erros.append(f"veredicto inválido: {v}")
    d = a.get("divergencia_legitima")
    material = isinstance(d, dict) and d.get("material") is True
    if "elegibilidade_automatica" in a:
        esperado = (v == "APROVADA") and not material
        if a.get("elegibilidade_automatica") is not esperado:
            erros.append(f"elegibilidade_automatica incoerente: esperado {esperado} para veredicto {v} e divergência material {material}")
    if d != "nenhuma" and "divergencia_legitima" in a:
        if not isinstance(d, dict):
            erros.append("divergencia_legitima deve ser 'nenhuma' ou objeto")
        else:
            ints = d.get("interpretacoes") or []
            if len(ints) < 2 or any(not _txt(i.get("veredicto")) or not _txt(i.get("fundamento")) for i in ints):
                erros.append("divergencia_legitima sem duas interpretações fundamentadas")
            if not isinstance(d.get("material"), bool):
                erros.append("divergencia_legitima.material deve ser true ou false")
            if not _txt(d.get("razao_sem_consenso")):
                erros.append("divergencia_legitima sem razao_sem_consenso")
            if d.get("material") is True:
                vs = {i.get("veredicto") for i in ints}
                if "APROVADA" not in vs or len(vs) < 2:
                    erros.append("divergência material exige APROVADA contra REVISAR ou REPROVADA")
    texto = json.dumps(a, ensure_ascii=False)
    if "—" in texto or "–" in texto:
        erros.append("travessão no texto")
    return erros


def avisos_v24(a: dict) -> list:
    out = []
    for o in a.get("objecoes", []) or []:
        if o.get("gravidade") == "nao_demonstrada":
            out.append(f"{a.get('codigo')}: objeção '{o.get('categoria')}' insuficientemente demonstrada (reportar à parte)")
    for o in a.get("objecoes", []) or []:
        t = (o.get("argumento", "") or "").lower()
        if any(h in t for h in HIPOTETICO):
            out.append(f"{a.get('codigo')}: argumento com linguagem hipotética ({o.get('categoria')})")
        if len(t) < 120 and any(x in t for x in VAGAS_V23):
            out.append(f"{a.get('codigo')}: argumento vago ({o.get('categoria')})")
        if o.get("fundamento") == "B" and len(_txt(o.get("leitura_alternativa_mais_favoravel"))) < 40:
            out.append(f"{a.get('codigo')}: leitura alternativa favorável muito curta ({o.get('categoria')})")
        if o.get("categoria") in ("cliche_efetivo", "redundancia") and "previs" in t and "corrobora" not in t and len(t) < 160:
            out.append(f"{a.get('codigo')}: objeção {o.get('categoria')} parece apoiada só na previsão")
    d = a.get("divergencia_legitima")
    if isinstance(d, dict) and d.get("material") is True:
        out.append(f"{a.get('codigo')}: divergência material declarada (acompanhar a taxa no conjunto)")
    return out


def validar(a: dict) -> list:
    if a.get("versao_criterio") == "v2.4-exp":
        return validar_v24(a)
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
            elif a.get("versao_criterio") == "v2.4-exp":
                for w in avisos_v24(a):
                    print("  aviso: " + w)
    print(f"\n{com_erro} de {total} com inconsistência")
    return 0


if __name__ == "__main__":
    sys.exit(main())
