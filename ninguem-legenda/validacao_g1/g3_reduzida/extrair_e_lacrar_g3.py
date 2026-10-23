#!/usr/bin/env python3
"""Extrai VERBATIM a resposta final de cada agente (transcrição) para execucoes/, confere cobertura de códigos e calcula SHA-256.
Não abre rótulos nem decodifica. Uso (a partir de ninguem-legenda/): extrair_e_lacrar_g3.py AGENTES.json"""
import json, re, sys, hashlib
V = 'validacao_g1/g3_reduzida'; EX = f'{V}/execucoes'
ag = json.load(open(sys.argv[1]))
base = '/root/.claude/projects/-home-claude/6475ae3b-fefe-5105-8fc9-a74e780d2bc8/subagents/agent-%s.jsonl'
rel = {}
for k, a in ag.items():
    last = None; modelo = set()
    for l in open(base % a, encoding='utf-8'):
        d = json.loads(l)
        if d.get('type') == 'assistant':
            m = d['message']; modelo.add(m.get('model', '?'))
            c = m['content']; t = ''.join(b.get('text', '') for b in c if b.get('type') == 'text') if isinstance(c, list) else c
            if t.strip(): last = t
    raw = last
    p = f'{EX}/bruto_{k}.txt'; open(p, 'w', encoding='utf-8').write(raw)
    info = {'agente': a, 'modelo': sorted(modelo), 'sha256': hashlib.sha256(raw.encode()).hexdigest(), 'arquivo': p}
    try:
        j = json.loads(re.search(r'\[.*\]', raw, re.S).group(0))
        e, part = k.rsplit('_', 1)
        pac = json.load(open(f'{V}/pacotes/pacote_{e}_parte{part[1]}.json', encoding='utf-8'))
        info['n_itens'] = len(j); info['cobertura_ok'] = sorted(x['codigo'] for x in j) == sorted(x['codigo'] for x in pac); info['json_ok'] = True
    except Exception as ex:
        info['json_ok'] = False; info['erro'] = str(ex)
    rel[k] = info
json.dump(rel, open(f'{EX}/lacre_execucoes_g3.json', 'w'), indent=1, ensure_ascii=False)
for k, v in rel.items(): print(k, v.get('n_itens'), v['json_ok'], v.get('cobertura_ok'), v['modelo'], v['sha256'][:12])
