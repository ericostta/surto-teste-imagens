#!/usr/bin/env python3
"""G3 reduzida: monta os pacotes comuns (sem avaliar nada). Executar a partir de ninguem-legenda/.
Usa SEM alteração instrumentos_g1/montar_pacotes.pacote_critico (congelado no M1).
Entradas: os 60 itens da G1 (manifesto), as 3 previsões cegas lacradas na G2 (triagem_run1..3, verbatim), textos_anteriores = [].
Saídas: validacao_g1/g3_reduzida/pacotes/ (sem mapa) e privado/mapa_execucoes.json (mapa código->item, sinais S1/S2)."""
import json, re, hashlib, sys, subprocess, os
sys.path.insert(0, 'instrumentos_g1')
from montar_pacotes import pacote_critico
V = 'validacao_g1'; G = f'{V}/g3_reduzida'
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
man = json.load(open(f'{V}/manifesto_g1.json', encoding='utf-8'))
incl = man['itens_incluidos']['fluxo'] + man['itens_incluidos']['desafio']
itens = {i: json.load(open(f'{V}/itens/{i}.json', encoding='utf-8')) for i in incl}
mt = json.load(open(f'{V}/g2/privado/mapa_codigos_opacos.json', encoding='utf-8'))['mapa']['triagem']  # T -> item
prev = {i: [None, None, None] for i in incl}
for r in (1, 2, 3):
    raw = open(f'{V}/g2/lacrado/triagem_run{r}.txt', encoding='utf-8').read()
    for x in json.loads(re.search(r'\[.*\]', raw, re.S).group(0)):
        prev[mt[x['codigo']]][r - 1] = x['previsao']
assert all(all(p) for p in prev.values())
EXEC = {'v22_e1': ('v22', 1), 'v22_e2': ('v22', 2), 'v24_e1': ('v24', 1), 'v24_e2': ('v24', 2)}
mapa = {}; hashes = {}
for e, (ver, run) in EXEC.items():
    pac, m = pacote_critico(itens, prev, [], f'g3-reduzida|{e}', run)
    assert len(pac) == 60
    mapa[e] = m
    for k, (a, b) in enumerate(((0, 30), (30, 60)), 1):
        p = f'{G}/pacotes/pacote_{e}_parte{k}.json'
        json.dump(pac[a:b], open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        hashes[p] = sh(p)
# sinais de risco estáticos (definidos na emenda, antes dos resultados)
cand = [{k: itens[i][k] for k in ('id', 'tema', 'situacao', 'mecanismo', 'emocao', 'tipo_contraste', 'na_foto', 'fora', 'conceito_foto', 'rosto')} for i in incl]
json.dump(cand, open(f'{G}/privado/candidatas_para_filtros.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'filtros.py', f'{G}/privado/candidatas_para_filtros.json', '--saida', f'{G}/privado/resultado_filtros.json'], check=True, stdout=subprocess.DEVNULL)
fl = json.load(open(f'{G}/privado/resultado_filtros.json', encoding='utf-8'))
fl = fl if isinstance(fl, list) else fl.get('resultados', fl)
fmap = {(x.get('id') or x.get('codigo')): x for x in fl}
S = {}
for i in incl:
    s1 = bool(fmap[i].get('alertas')); s2 = itens[i]['tipo_contraste'] == 'presenca_vs_ausencia' or itens[i]['emocao'] == 'melancolia'
    S[i] = {'S1_alerta_filtros': s1, 'S2_zona_ausencia_saudade': s2}
json.dump({'nota': 'MAPA PRIVADO da G3 reduzida. Não entra em pacote nem é dado aos Críticos.', 'mapa': mapa, 'sinais_estaticos': S}, open(f'{G}/privado/mapa_execucoes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(hashes, open(f'{G}/pacotes/hashes_pacotes_g3.json', 'w'), indent=1)
print(len(hashes), 'arquivos de pacote;', 'S1', sum(v['S1_alerta_filtros'] for v in S.values()), 'S2', sum(v['S2_zona_ausencia_saudade'] for v in S.values()))
