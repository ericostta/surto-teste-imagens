#!/usr/bin/env python3
"""Verificações de preparação da G2 (não avalia nada). Retorna 1 se alguma falhar."""
import json, re, os, glob, hashlib, sys
V='validacao_g1'; falhas=[]
man=json.load(open(f'{V}/manifesto_g1.json',encoding='utf-8'))
incl=man['itens_incluidos']['fluxo']+man['itens_incluidos']['desafio']
mp=json.load(open(f'{V}/g2/privado/mapa_codigos_opacos.json',encoding='utf-8'))
PROIB=[r'G1-',r'\bK\d\d\b',r'fluxo',r'desafio',r'intenç',r'sorteio',r'manifesto',r'critico',r'crítico',r'v2\.\d',r'célula',r'celula',r'mapa',r'rótulo gabarito']
for tr in ('externa','triagem'):
    pac=json.load(open(f'{V}/g2/pacotes/pacote_{tr}.json',encoding='utf-8'))
    if len(pac)!=60: falhas.append(f'{tr}: {len(pac)} itens')
    if len({p['codigo'] for p in pac})!=60: falhas.append(f'{tr}: códigos repetidos')
    if any(set(p)!={'codigo','foto','na_foto','fora'} for p in pac): falhas.append(f'{tr}: campos fora do padrão')
    if set(mp['mapa'][tr].values())!=set(incl): falhas.append(f'{tr}: mapa não cobre os 60')
    if [p['codigo'] for p in pac]==sorted(mp['mapa'][tr]): falhas.append(f'{tr}: ordem alfabética (não embaralhada)')
    txt=open(f'{V}/g2/pacotes/pacote_{tr}.md',encoding='utf-8').read()+json.dumps(pac,ensure_ascii=False)
    for rx in PROIB:
        if re.search(rx,txt,re.I): falhas.append(f'{tr}: termo proibido {rx}')
    for c in incl:   # nenhum código interno ou código opaco de outra trilha
        if c in txt: falhas.append(f'{tr}: código interno {c}')
for o in set(mp['mapa']['triagem'])&set(mp['mapa']['externa']): falhas.append('código repetido entre trilhas '+o)
if list(mp['mapa']['externa'].values())==list(mp['mapa']['triagem'].values()): falhas.append('mesma ordem nas duas trilhas')
# nenhum rótulo, predição ou resultado existe
for f in glob.glob(f'{V}/**/*',recursive=True):
    if re.search(r'rotulo|predicao|previsao|resultado|avaliacao',os.path.basename(f),re.I) and 'g2/' not in f.replace('\\','/').split(V)[1][:4] : falhas.append('arquivo suspeito '+f)
# integridade dos hashes
for p,h in json.load(open(f'{V}/g2/pacotes/hashes_pacotes.json')).items():
    if hashlib.sha256(open(p,'rb').read()).hexdigest()!=h: falhas.append('hash divergente '+p)
for c,i in man['itens'].items():
    if hashlib.sha256(open(i['arquivo'],'rb').read()).hexdigest()!=i['sha256_arquivo']: falhas.append('item alterado '+c)
print('FALHAS:',falhas) if falhas else print('verificações de preparação: todas passaram')
sys.exit(1 if falhas else 0)
