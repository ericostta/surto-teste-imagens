#!/usr/bin/env python3
"""Verificação mecânica PRÉ da verificação limitada da C1b (Emenda 2). Executar a partir de ninguem-legenda/.
Confere: lacre da emenda (hashes), v2.2 e validador congelados, arquivos do M1, G1 (itens e apoio), registros G2/G3,
diffs regeneráveis, ausência de execuções/rótulos/pacotes desta verificação, ausência de travessão nos documentos novos.
Retorna 1 se falhar. Grava verificacao_c1b/verificacao_pre.json."""
import json, sys, hashlib, subprocess, os, glob, datetime
sys.path.insert(0, 'instrumentos_g1')
import manifesto_hashes as M
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
V = 'validacao_g1'; C = 'verificacao_c1b'; falhas = []; ok = {}
lac = json.load(open(f'{C}/lacre_emenda2.json', encoding='utf-8'))['hashes']
d = M.verificar(lac); ok['lacre_emenda2'] = (len(lac), d)
if d: falhas.append(f'lacre emenda 2 {d}')
m1 = json.load(open('referencia_editorial/marco_congelamento_g1.json')); flat = {k: v for g in m1['arquivos'].values() for k, v in g.items()}
d = M.verificar(flat); ok['M1_arquivos'] = (len(flat), d)
if d: falhas.append(f'M1 {d}')
man = json.load(open(f'{V}/manifesto_g1.json', encoding='utf-8'))
d = M.verificar({v['arquivo']: v['sha256_arquivo'] for v in man['itens'].values()}); ok['G1_itens'] = (len(man['itens']), d)
if d: falhas.append(f'G1 itens {d}')
d = M.verificar(man['arquivos_de_apoio']); ok['G1_apoio'] = d
if d: falhas.append(f'G1 apoio {d}')
ok['v22_igual_M1'] = sh('prompts/critico_v2_2.md') == flat['prompts/critico_v2_2.md'] == '468fd3823f83909dd87127d7a4affd835df4be09c7601e62c37b38dc54b553a3'
ok['validador_igual'] = sh('validar_avaliacao.py') == '04a0183bc93598ed72e41ea7a1294cbb1db8d0b92bf175dbe8c65442e4c487f1'
if not (ok['v22_igual_M1'] and ok['validador_igual']): falhas.append('v2.2 ou validador alterado')
for p in ('prompts', 'validar_avaliacao.py', 'filtros.py', 'taxonomia.json', 'config.json', 'registro.csv', 'instrumentos_g1', 'referencia_editorial', 'validacao_g1'):
    if subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', p]).returncode: falhas.append(f'alterado vs HEAD: {p}')
# diffs regeneráveis
def regen(a, b):
    r = subprocess.run(['diff', '-u', a, b], capture_output=True, text=True).stdout
    return hashlib.sha256(r.replace(a, 'v2.2').replace(b, 'C1b').encode()).hexdigest()
I = 'pos_g3/intervencao'
ok['c1b_difere_so_nos_blocos_declarados'] = True
d22 = subprocess.run(['diff', '-u', 'prompts/critico_v2_2.md', f'{I}/critico_v2_2_c1b.md'], capture_output=True, text=True).stdout
hunks = [l for l in d22.splitlines() if l.startswith('@@')]
ok['hunks_c1b_vs_v22'] = len(hunks)
if len(hunks) != 3: falhas.append(f'C1b vs v2.2: {len(hunks)} blocos alterados (esperado 3: cabeçalho, E1 e E5 contíguos, Salvaguarda)')
# estado pré-execução
for sub in ('execucoes', 'lacrado', 'pacotes', 'privado', 'producao'):
    fs = [f for f in glob.glob(f'{C}/{sub}/**', recursive=True) if os.path.isfile(f)]
    ok[f'arquivos_em_{sub}'] = len(fs)
    if fs and '--permitir-estado-posterior' not in sys.argv: falhas.append(f'{C}/{sub} não está vazio (verificação pré)')
# travessão
for f in glob.glob(f'{C}/*.md') + [f'{I}/critico_v2_2_c1b.md', f'{I}/PROTOCOLO_VERIFICACAO_C1B.md']:
    if '—' in open(f, encoding='utf-8').read(): falhas.append(f'travessão em {f}')
json.dump({'quando': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'resultado': ok, 'falhas': falhas}, open(f'{C}/verificacao_pre.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('FALHAS:', falhas) if falhas else print('verificação C1b (pré): todas passaram')
print(json.dumps(ok, ensure_ascii=False)[:700])
sys.exit(1 if falhas else 0)
