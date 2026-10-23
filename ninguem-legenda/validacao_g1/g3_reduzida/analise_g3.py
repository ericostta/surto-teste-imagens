#!/usr/bin/env python3
"""Análise da G3 reduzida conforme a Emenda 1 (medidas e gate definidos antes dos resultados). Executar a partir de ninguem-legenda/
SÓ DEPOIS do lacre das saídas brutas. Lê rótulos e decodifica. Não altera nenhum registro anterior. Escreve analise_g3_resultados.json e matriz_g3.md."""
import json, re, sys, collections
V = 'validacao_g1'; G = f'{V}/g3_reduzida'
man = json.load(open(f'{V}/manifesto_g1.json', encoding='utf-8'))
estrato = {i: 'fluxo' for i in man['itens_incluidos']['fluxo']} | {i: 'desafio' for i in man['itens_incluidos']['desafio']}
itens = sorted(estrato)
mp = json.load(open(f'{G}/privado/mapa_execucoes.json', encoding='utf-8')); mapa = mp['mapa']; S12 = mp['sinais_estaticos']
me = json.load(open(f'{V}/g2/privado/mapa_codigos_opacos.json', encoding='utf-8'))['mapa']['externa']
rot = {}
for l in open(f'{V}/g2/lacrado/rotulos_externos_bruto.txt', encoding='utf-8').read().splitlines():
    c, r = l.split(': '); rot[me[c]] = r
tens = {t['item']: t['tipo'] for t in json.load(open(f'{V}/g2/privado/lista_tensoes.json', encoding='utf-8'))['tensoes']}
EXECS = ('v22_e1', 'v22_e2', 'v24_e1', 'v24_e2')
ev = {}
for e in EXECS:
    ev[e] = {}
    for p in (1, 2):
        raw = open(f'{G}/execucoes/bruto_{e}_p{p}.txt', encoding='utf-8').read()
        for x in json.loads(re.search(r'\[.*\]', raw, re.S).group(0)):
            ev[e][mapa[e][x['codigo']]] = x
    assert set(ev[e]) == set(itens), e
ver = lambda e, i: ev[e][i]['veredicto']
def eleg(e, i):
    return ev[e][i].get('elegibilidade_automatica') is True if e.startswith('v24') else ver(e, i) == 'APROVADA'
def erro(e, i):
    v, r = ver(e, i), rot[i]
    if v == 'APROVADA' and r == 'RUIM': return 'RUIM_aprovada'
    if v == 'APROVADA' and r == 'AMBÍGUA': return 'AMBIGUA_aprovada'
    if r == 'BOA' and v != 'APROVADA': return 'BOA_perdida_' + v
    return None
R = {}
# 1. tabelas de veredicto por execução, estrato e rótulo
tab = {}
for e in EXECS:
    for s in ('fluxo', 'desafio'):
        for r in ('BOA', 'AMBÍGUA', 'RUIM'):
            its = [i for i in itens if estrato[i] == s and rot[i] == r]
            tab[f'{e}|{s}|{r}'] = dict(collections.Counter(ver(e, i) for i in its)) | {'n': len(its)}
R['tabela_veredictos'] = tab
R['composicao'] = {s: dict(collections.Counter(rot[i] for i in itens if estrato[i] == s)) for s in ('fluxo', 'desafio')}
R['composicao_tensoes'] = {'tensoes': dict(collections.Counter(rot[i] for i in tens)), 'sem_tensoes': dict(collections.Counter(rot[i] for i in itens if i not in tens))}
# 2. listas de erros por execução
R['erros'] = {e: {k: sorted(i for i in itens if erro(e, i) and erro(e, i).startswith(k)) for k in ('RUIM_aprovada', 'AMBIGUA_aprovada', 'BOA_perdida')} for e in EXECS}
R['erros_por_estrato'] = {e: {s: {k: sum(1 for i in itens if estrato[i] == s and erro(e, i) and erro(e, i).startswith(k)) for k in ('RUIM_aprovada', 'AMBIGUA_aprovada', 'BOA_perdida')} for s in ('fluxo', 'desafio')} for e in EXECS}
R['BOA_aprovadas'] = {e: {s: sum(1 for i in itens if estrato[i] == s and rot[i] == 'BOA' and ver(e, i) == 'APROVADA') for s in ('fluxo', 'desafio')} for e in EXECS}
# 3. corrigidos e novos erros (pares: v22 e1,e2 contra v24 e1,e2)
def nerr(v, i): return sum(1 for e in (f'{v}_e1', f'{v}_e2') if erro(e, i))
corr, novo, parc_c, parc_n = [], [], [], []
for i in itens:
    a, b = nerr('v22', i), nerr('v24', i)
    if a == 2 and b == 0: corr.append(i)
    elif a > b: parc_c.append((i, a, b))
    if b == 2 and a == 0: novo.append(i)
    elif b > a: parc_n.append((i, a, b))
def desc(i): return {'item': i, 'estrato': estrato[i], 'rotulo': rot[i], 'tensao': tens.get(i), 'v22': [ver('v22_e1', i), ver('v22_e2', i)], 'v24': [ver('v24_e1', i), ver('v24_e2', i)]}
R['corrigidos_completos'] = [desc(i) for i in corr]; R['corrigidos_parciais'] = [desc(i) | {'erros_v22': a, 'erros_v24': b} for i, a, b in parc_c]
R['novos_erros_completos'] = [desc(i) for i in novo]; R['novos_erros_parciais'] = [desc(i) | {'erros_v22': a, 'erros_v24': b} for i, a, b in parc_n]
# 4. consistência
R['inconsistencia_entre_execucoes'] = {v: [desc(i) for i in itens if ver(f'{v}_e1', i) != ver(f'{v}_e2', i)] for v in ('v22', 'v24')}
# 5. bruto x elegibilidade (v2.4-exp)
R['v24_aprovada_bruta_sem_elegibilidade'] = {e: sorted(i for i in itens if ver(e, i) == 'APROVADA' and not eleg(e, i)) for e in ('v24_e1', 'v24_e2')}
R['erros_pela_elegibilidade'] = {e: {k: sorted(i for i in itens if eleg(e, i) and (rot[i] == 'RUIM' if k == 'RUIM' else rot[i] == 'AMBÍGUA')) for k in ('RUIM', 'AMBÍGUA')} for e in EXECS}
R['divergencia_material_v24'] = {e: {i: ev[e][i]['divergencia_legitima'] for i in itens if ev[e][i].get('divergencia_legitima') not in (None, 'nenhuma') and isinstance(ev[e][i]['divergencia_legitima'], dict) and ev[e][i]['divergencia_legitima'].get('material')} for e in ('v24_e1', 'v24_e2')}
# 6. sensibilidade pela composição efetiva
R['erros_em_tensao_e_fora'] = {e: {'em_tensao': {k: sum(1 for i in tens if erro(e, i) and erro(e, i).startswith(k)) for k in ('RUIM_aprovada', 'AMBIGUA_aprovada', 'BOA_perdida')},
                                   'fora_de_tensao': {k: sum(1 for i in itens if i not in tens and erro(e, i) and erro(e, i).startswith(k)) for k in ('AMBIGUA_aprovada', 'BOA_perdida')}} for e in EXECS}
R['nota_sensibilidade'] = 'O grupo fora de tensão não contém RUIM; nenhuma taxa de RUIM aprovado é calculada sobre ele.'
# 7. simulação do gate
def s3(e, i):
    x = ev[e][i]
    if e.startswith('v22'): return bool(x.get('e_a_associacao_mais_comum')) or (x.get('previsoes_que_capturaram') or 0) >= 2
    return bool(x.get('objecoes')) or x.get('divergencia_legitima') not in (None, 'nenhuma')
def sinal(e, i): return {'S1': S12[i]['S1_alerta_filtros'], 'S2': S12[i]['S2_zona_ausencia_saudade'], 'S3': s3(e, i)}
gate = {}
for v in ('v22', 'v24'):
    for ordem in (('e1', 'e2'), ('e2', 'e1')):
        f, s = f'{v}_{ordem[0]}', f'{v}_{ordem[1]}'
        g1 = {i for i in itens if ver(f, i) == 'APROVADA'}
        g2 = {i for i in itens if ver(f, i) == 'APROVADA' and ver(s, i) == 'APROVADA'}
        trig = {i for i in g1 if any(sinal(f, i).values())}
        g3 = {i for i in g1 if i not in trig or ver(s, i) == 'APROVADA'}
        def rel(ap):
            return {'aprovadas': len(ap), 'RUIM_aprovada': sorted(i for i in ap if rot[i] == 'RUIM'), 'AMBIGUA_aprovada': sorted(i for i in ap if rot[i] == 'AMBÍGUA'), 'BOA_aprovadas': sum(1 for i in ap if rot[i] == 'BOA')}
        r1, r2, r3 = rel(g1), rel(g2), rel(g3)
        def vs_base(r, ap):
            return {'erros_evitados': sorted(i for i in g1 - ap if rot[i] in ('RUIM', 'AMBÍGUA')), 'BOA_atrasadas': sorted(i for i in g1 - ap if rot[i] == 'BOA')}
        sem_sinal = sorted(i for i in g1 if rot[i] in ('RUIM', 'AMBÍGUA') and not any(sinal(f, i).values()))
        gate[f'{v}_primeira_{ordem[0]}'] = {'G1_uma_avaliacao': r1, 'G2_dupla_aprovacao': r2 | vs_base(r2, g2), 'G3_sinais': r3 | vs_base(r3, g3) | {'segundas_avaliacoes_acionadas': len(trig), 'de_primeiras_aprovadas': len(g1)},
                                            'aprovados_indevidos_sem_nenhum_sinal': sem_sinal, 'sinais_por_aprovado_indevido': {i: sinal(f, i) for i in g1 if rot[i] in ('RUIM', 'AMBÍGUA')}}
R['gate'] = gate
R['sinais_estaticos_contagem'] = {'S1': sum(v['S1_alerta_filtros'] for v in S12.values()), 'S2': sum(v['S2_zona_ausencia_saudade'] for v in S12.values())}
json.dump(R, open(f'{G}/analise_g3_resultados.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# matriz item a item
L = ['# Matriz item a item (G3 reduzida)\n', '| item | estrato | rótulo | tensão | v2.2 e1 | v2.2 e2 | v2.4 e1 | v2.4 e2 | elegível v2.4 e1/e2 |', '|---|---|---|---|---|---|---|---|---|']
for i in itens:
    L.append(f"| {i} | {estrato[i]} | {rot[i]} | {tens.get(i, '')} | {ver('v22_e1', i)} | {ver('v22_e2', i)} | {ver('v24_e1', i)} | {ver('v24_e2', i)} | {'S' if eleg('v24_e1', i) else 'N'}/{'S' if eleg('v24_e2', i) else 'N'} |")
open(f'{G}/matriz_g3.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('análise gravada')
