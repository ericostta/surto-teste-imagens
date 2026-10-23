#!/usr/bin/env python3
"""Verificação mecânica da G3 reduzida (antes e depois da execução). Executar a partir de ninguem-legenda/. Retorna 1 se falhar."""
import json, re, sys, hashlib, subprocess, os, glob, itertools
sys.path.insert(0, 'instrumentos_g1')
import manifesto_hashes as M
V = 'validacao_g1'; G = f'{V}/g3_reduzida'; falhas = []; ok = {}
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
m1 = json.load(open('referencia_editorial/marco_congelamento_g1.json')); flat = {k: v for g in m1['arquivos'].values() for k, v in g.items()}
d = M.verificar(flat); ok['M1_arquivos'] = (len(flat), d)
if d: falhas.append(f'M1 {d}')
man = json.load(open(f'{V}/manifesto_g1.json', encoding='utf-8'))
d = M.verificar({v['arquivo']: v['sha256_arquivo'] for v in man['itens'].values()}); ok['G1_itens'] = (len(man['itens']), d)
if d: falhas.append(f'G1 itens {d}')
d = M.verificar(man['arquivos_de_apoio']); ok['G1_apoio'] = d
if d: falhas.append(f'G1 apoio {d}')
ok['prompt_v22_igual_M1'] = sh('prompts/critico_v2_2.md') == flat['prompts/critico_v2_2.md']
ok['prompt_v24_igual_M1'] = sh('prompts/critico_v2_4_exp.md') == flat['prompts/critico_v2_4_exp.md']
if not (ok['prompt_v22_igual_M1'] and ok['prompt_v24_igual_M1']): falhas.append('prompt diferente do M1')
for p in ('validar_avaliacao.py', 'filtros.py', 'taxonomia.json', 'config.json', 'registro.csv', 'instrumentos_g1', 'prompts', 'referencia_editorial'):
    if subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', p]).returncode: falhas.append(f'alterado vs HEAD: {p}')
lt = json.load(open(f'{V}/g2/lacrado/lacre_triagem.json'))
ok['previsoes_lacradas'] = all(sh(f"{V}/g2/{v['arquivo']}") == v['sha256'] for v in lt.values())
ok['rotulos_lacrados'] = sh(f'{V}/g2/lacrado/rotulos_externos_bruto.txt') == '7d80fa286edf13e672de7fa3d26c664e8986b868af7942196eb65a4748f82e08'
ok['segunda_leitura_lacrada'] = sh(f'{V}/g2/lacrado/segunda_leitura_chatgpt_nao_independente_bruto.txt') == json.load(open(f'{V}/g2/conferencia/registro_segunda_leitura_nao_independente.json'))['sha256']
for lac in ('lacre_marcacao_previsibilidade', 'lacre_cruzamento'):
    for p, h in json.load(open(f'{V}/g2/conferencia/{lac}.json'))['hashes'].items():
        if sh(f'{V}/../{p}' if False else p if os.path.exists(p) else f'{V}/{p}') != h: falhas.append(f'G2 registro alterado {p}')
for k in ('previsoes_lacradas', 'rotulos_lacrados', 'segunda_leitura_lacrada'):
    if not ok[k]: falhas.append(k)
# pacotes
hp = json.load(open(f'{G}/pacotes/hashes_pacotes_g3.json')); ok['pacotes_hash'] = all(sh(p) == h for p, h in hp.items()) and len(hp) == 8
if not ok['pacotes_hash']: falhas.append('hash de pacote')
mp = json.load(open(f'{G}/privado/mapa_execucoes.json', encoding='utf-8'))['mapa']
mt = json.load(open(f'{V}/g2/privado/mapa_codigos_opacos.json', encoding='utf-8'))['mapa']['triagem']
prev = {}
for r in (1, 2, 3):
    raw = open(f'{V}/g2/lacrado/triagem_run{r}.txt', encoding='utf-8').read()
    for x in json.loads(re.search(r'\[.*\]', raw, re.S).group(0)): prev.setdefault(mt[x['codigo']], []).append(x['previsao'])
itens = {i: json.load(open(f'{V}/itens/{i}.json', encoding='utf-8')) for i in prev}
orders = {}; codesets = {}
for e in ('v22_e1', 'v22_e2', 'v24_e1', 'v24_e2'):
    pac = json.load(open(f'{G}/pacotes/pacote_{e}_parte1.json', encoding='utf-8')) + json.load(open(f'{G}/pacotes/pacote_{e}_parte2.json', encoding='utf-8'))
    txt = json.dumps(pac, ensure_ascii=False)
    if len(pac) != 60 or len({p['codigo'] for p in pac}) != 60 or set(mp[e]) != {p['codigo'] for p in pac}: falhas.append(f'{e}: cobertura')
    if any(set(p) != {'codigo', 'conceito_foto', 'na_foto', 'fora', 'previsoes_cegas', 'textos_anteriores'} or p['textos_anteriores'] != [] for p in pac): falhas.append(f'{e}: campos')
    for p in pac:
        i = mp[e][p['codigo']]
        if p['previsoes_cegas'] != prev[i] or p['fora'] != itens[i]['fora'] or p['na_foto'] != itens[i]['na_foto'] or p['conceito_foto'] != itens[i]['conceito_foto']: falhas.append(f'{e}: conteúdo {p["codigo"]}')
    if re.search(r'G1-[FD]\d|\bBOA\b|\bRUIM\b|AMB[IÍ]GUA|v2\.\d|\bT[0-9A-F]{6}\b|\bP[0-9A-F]{6}\b|\bH[0-9A-F]{6}\b', txt): falhas.append(f'{e}: termo/identificador proibido no pacote')
    orders[e] = [mp[e][p['codigo']] for p in pac]; codesets[e] = {p['codigo'] for p in pac}
for a, b in itertools.combinations(orders, 2):
    if orders[a] == orders[b]: falhas.append(f'mesma ordem {a} {b}')
    if codesets[a] == codesets[b]: falhas.append(f'mesmos códigos {a} {b}')
ok['execucoes_distintas'] = not any('mesma' in f for f in falhas)
fut = [f for f in glob.glob(f'{G}/execucoes/*') if os.path.isfile(f)]
ok['arquivos_em_execucoes'] = len(fut)
json.dump({'quando': __import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(), 'resultado': ok, 'falhas': falhas}, open(f'{G}/verificacao_g3_{sys.argv[1] if len(sys.argv)>1 else "pre"}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('FALHAS:', falhas) if falhas else print('verificação G3: todas passaram')
print(json.dumps(ok, ensure_ascii=False)[:900])
sys.exit(1 if falhas else 0)
