#!/usr/bin/env python3
"""Verificações de preparação da G2, revisão 2 (não avalia nada). Retorna 1 se alguma falhar. Grava g2/verificacao_preparacao.json."""
import json, re, os, glob, hashlib, sys, unicodedata, subprocess
sys.path.insert(0,'instrumentos_g1')
import manifesto_hashes as M
V='validacao_g1'; falhas=[]; ok={}
norm=lambda s: re.sub(r'\s+',' ',re.sub(r'[^a-z0-9 ]+',' ',unicodedata.normalize('NFKD',s.lower()).encode('ascii','ignore').decode())).strip()
sh=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
man=json.load(open(f'{V}/manifesto_g1.json',encoding='utf-8'))
incl=man['itens_incluidos']['fluxo']+man['itens_incluidos']['desafio']
mp=json.load(open(f'{V}/g2/privado/mapa_codigos_opacos.json',encoding='utf-8'))['mapa']
itens={c:json.load(open(f'{V}/itens/{c}.json',encoding='utf-8')) for c in incl}
tri=json.load(open(f'{V}/g2/pacotes/pacote_triagem.json',encoding='utf-8')); ext=json.load(open(f'{V}/g2/pacotes/pacote_externa.json',encoding='utf-8'))
tmd=open(f'{V}/g2/pacotes/pacote_triagem.md',encoding='utf-8').read(); emd=open(f'{V}/g2/pacotes/pacote_externa.md',encoding='utf-8').read()
# A: triagem sem FORA
ok['A_triagem_campos']=all(set(p)=={'codigo','foto','na_foto'} for p in tri) and len(tri)==60
if not ok['A_triagem_campos']: falhas.append('A: campos do pacote de triagem')
nt=norm(tmd+json.dumps(tri,ensure_ascii=False)); vaz=[]
for c,it in itens.items():
    if norm(it['fora']) in nt: vaz.append(c)
    for f in re.split(r'[.!?;]+',it['fora']):
        if len(norm(f))>=18 and norm(f) in nt: vaz.append(c)
ok['A_triagem_sem_texto_do_FORA']=not vaz
if vaz: falhas.append(f'A: texto do FORA no pacote de triagem {sorted(set(vaz))}')
# instrução de triagem = preditor.md sem alteração, e preditor.md igual ao commit anterior
pred=open('prompts/preditor.md',encoding='utf-8').read().strip()
ok['D_instrucao_igual_preditor_md']=pred in tmd
if not ok['D_instrucao_igual_preditor_md']: falhas.append('D: instrução diferente de prompts/preditor.md')
ok['D_preditor_md_sha256']=sh('prompts/preditor.md')
diff=subprocess.run(['git','diff','--quiet','HEAD','--','prompts/preditor.md']).returncode
ok['D_preditor_md_inalterado_vs_HEAD']=(diff==0)
if diff: falhas.append('preditor.md alterado')
# B: externo
ok['B_externa_campos']=all(set(p)=={'codigo','foto','na_foto','fora'} for p in ext) and len(ext)==60
if not ok['B_externa_campos']: falhas.append('B: campos do pacote externo')
ref=open(f'{V}/g2/referencia_editorial_avaliador.md',encoding='utf-8').read().strip()
ok['B_externa_contem_referencia']=ref in emd
if not ok['B_externa_contem_referencia']: falhas.append('B: referência ausente')
PROIB=[r'G1-',r'\bK\d\d\b',r'fluxo',r'desafio',r'inten[cç]',r'sorteio',r'manifesto',r'cr[ií]tico',r'v2\.\d',r'c[eé]lula',r'previs(ão|ões|ao|oes)\b',r'preditor',r'veredit',r'chatgpt',r'autoria',r'fonte:',r'criador',r'subagente',r'\bEri\b',r'gabarito',r'sentimentalismo',r'corre[cç][aã]o pontual',r'diverg[eê]ncia leg[ií]tima potencial']
for nome,txt in (('externa',emd+json.dumps(ext,ensure_ascii=False)),('triagem',tmd+json.dumps(tri,ensure_ascii=False))):
    for rx in PROIB:
        if re.search(rx,txt,re.I):
            # 'previs' e 'preditor' são esperados na instrução da trilha de triagem
            if nome=='triagem' and rx in (r'previs(ão|ões|ao|oes)\b',r'preditor'): continue
            falhas.append(f'{nome}: termo proibido {rx}')
ok['B_externa_sem_termos_proibidos']=not any(f.startswith('externa: termo') for f in falhas)
for nome,pac in (('externa',ext),('triagem',tri)):
    if len({p['codigo'] for p in pac})!=60: falhas.append(f'{nome}: códigos repetidos')
    if set(mp[nome].values())!=set(incl): falhas.append(f'{nome}: mapa não cobre os 60')
    if [p['codigo'] for p in pac]==sorted(p['codigo'] for p in pac): falhas.append(f'{nome}: ordem alfabética')
    for c in incl:
        if c in json.dumps(pac)+(emd if nome=='externa' else tmd): falhas.append(f'{nome}: código interno {c}')
if set(mp['triagem'])&set(mp['externa']): falhas.append('código repetido entre trilhas')
if list(mp['externa'].values())==list(mp['triagem'].values()): falhas.append('mesma ordem nas duas trilhas')
ok['trilhas_codigos_e_ordens_distintos']=not set(mp['triagem'])&set(mp['externa']) and list(mp['externa'].values())!=list(mp['triagem'].values())
# nada futuro existe
fut=[f for f in glob.glob(f'{V}/**/*',recursive=True) if os.path.isfile(f) and not f.endswith(('.md','.py')) and re.search(r'rotulo|predicao|previsao|triagem_bruta|avaliacao_|resultado',os.path.basename(f),re.I)]
ok['sem_rotulos_previsoes_resultados']=not fut
if fut: falhas.append(f'arquivos futuros existem: {fut}')
ok['lacrado_vazio']=not os.path.exists(f'{V}/g2/lacrado') or not os.listdir(f'{V}/g2/lacrado')
# C: M1 inalterado, G1 inalterado
m1=json.load(open('referencia_editorial/marco_congelamento_g1.json')); flat={k:v for g in m1['arquivos'].values() for k,v in g.items()}
d1=M.verificar(flat); ok['C_M1_22_arquivos']=(len(flat),d1)
if d1: falhas.append(f'C: M1 {d1}')
d2=M.verificar({v['arquivo']:v['sha256_arquivo'] for v in man['itens'].values()}); ok['G1_65_itens']=(len(man['itens']),d2)
if d2: falhas.append(f'G1: itens {d2}')
d3=M.verificar(man['arquivos_de_apoio']); ok['G1_arquivos_de_apoio']=d3
if d3: falhas.append(f'G1 apoio {d3}')
# informativo: palavras de conteúdo do FORA que já aparecem no conceito de foto ou no NA FOTO (possível pista), não altera nada
STOP=set('uma para mais como esta este desde todo toda ainda nunca quando porque pelo pela sobre entre depois antes tudo cada outra outro dele dela'.split())
cw=lambda s:{w for w in norm(s).split() if len(w)>4 and w not in STOP}
inf={c:sorted(cw(it['fora'])&(cw(it['conceito_foto'])|cw(it['na_foto']))) for c,it in itens.items()}
ok['informativo_sobreposicao_FORA_com_foto_ou_NA_FOTO_max']=sorted(((len(v),c) for c,v in inf.items()),reverse=True)[:5]
json.dump({'quando':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'resultado':ok,'falhas':falhas},open(f'{V}/g2/verificacao_preparacao.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('FALHAS:',falhas) if falhas else print('verificações de preparação: todas passaram')
print(json.dumps(ok,ensure_ascii=False)[:1500])
sys.exit(1 if falhas else 0)
