#!/usr/bin/env python3
"""Cruzamento controlado (autorizado por Eri, 23/10): tensões, controle e pacote humano. Executar a partir de validacao_g1/.
Regra em g2/conferencia/regra_tensoes_controle_pacote_humano.md (lacrada antes)."""
import json, hashlib, math, os
sha=lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
G='g2'; P=f'{G}/privado'; C=f'{G}/conferencia'
M=json.load(open(f'{P}/mapa_codigos_opacos.json',encoding='utf-8')); hconj=M['hash_do_conjunto']
mt=M['mapa']['triagem']; me=M['mapa']['externa']
marc={o['codigo_T']:o for o in json.load(open(f'{C}/marcacao_previsibilidade.json',encoding='utf-8'))}
prev={mt[t]:o['previsivel'] for t,o in marc.items()}
rot={}
for l in open(f'{G}/lacrado/rotulos_externos_bruto.txt',encoding='utf-8').read().splitlines():
    c,r=l.split(': '); rot[me[c]]=r
assert len(rot)==60 and set(rot)==set(prev)
tens=[]
for i in sorted(prev):
    if prev[i] and rot[i]=='BOA': tens.append({'item':i,'tipo':'A','rotulo_externo':rot[i],'previsivel':True})
    if (not prev[i]) and rot[i]=='RUIM': tens.append({'item':i,'tipo':'B','rotulo_externo':rot[i],'previsivel':False})
ti={t['item'] for t in tens}
univ=sorted(set(prev)-ti)
tam=min(len(univ),max(10,math.ceil(0.20*len(univ))))
estr={}
for i in univ: estr.setdefault(rot[i],[]).append(i)
for r in estr: estr[r].sort(key=lambda i:sha(f'g2-controle|{hconj}|{i}'))
# cotas proporcionais, maior resto, mínimo 1 por rótulo presente
q={r:len(v)*tam/len(univ) for r,v in estr.items()}
cota={r:max(1,int(math.floor(x))) for r,x in q.items()}
while sum(cota.values())<tam:
    r=max(q,key=lambda r:(q[r]-cota[r]) if cota[r]<len(estr[r]) else -9); cota[r]+=1
while sum(cota.values())>tam:
    r=max(cota,key=lambda r:cota[r]-q[r]) if True else None
    if cota[r]>1: cota[r]-=1
    else: break
ctrl=[]
for r,v in estr.items():
    for i in v[:cota[r]]: ctrl.append({'item':i,'rotulo_externo':r,'previsivel':prev[i]})
ctrl.sort(key=lambda x:x['item'])
json.dump({'regra':'g2/conferencia/regra_tensoes_controle_pacote_humano.md','n':len(tens),'tensoes':tens},open(f'{P}/lista_tensoes.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump({'regra':'g2/conferencia/regra_tensoes_controle_pacote_humano.md','universo':len(univ),'tamanho_alvo':tam,'universo_por_rotulo':{r:len(v) for r,v in estr.items()},'cotas':cota,'n':len(ctrl),'controle':ctrl},open(f'{P}/selecao_controle.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
sel=sorted({t['item'] for t in tens}|{c['item'] for c in ctrl})
cod={i:'H'+sha(f'g2|humana|{hconj}|{i}')[:6].upper() for i in sel}
assert len(set(cod.values()))==len(sel)
ordem=sorted(sel,key=lambda i:sha(f'g2-ordem|humana|{hconj}|{i}'))
REF=open(f'{G}/referencia_editorial_avaliador.md',encoding='utf-8').read()
pac=[]
for i in ordem:
    it=json.load(open(f'itens/{i}.json',encoding='utf-8'))
    pac.append({'codigo':cod[i],'foto':it['conceito_foto'],'na_foto':it['na_foto'],'fora':it['fora']})
os.makedirs(f'{G}/pacotes',exist_ok=True)
json.dump(pac,open(f'{G}/pacotes/pacote_humano.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
md=REF.strip()+f"\n\n---\n\nItens para conferência. Há {len(pac)}, em ordem embaralhada. Classifique cada um como BOA, AMBÍGUA ou RUIM conforme a referência acima.\n"+"".join(f"\n## {p['codigo']}\nFOTO: {p['foto']}\nNA FOTO: {p['na_foto']}\nFORA DO ENQUADRAMENTO: {p['fora']}\n" for p in pac)
open(f'{G}/pacotes/pacote_humano.md','w',encoding='utf-8').write(md)
json.dump({'nota':'MAPA PRIVADO dos códigos H. Não entra no pacote humano.','mapa':{cod[i]:i for i in ordem}},open(f'{P}/mapa_codigos_humana.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('tensoes',len(tens),'A',sum(t['tipo']=='A' for t in tens),'B',sum(t['tipo']=='B' for t in tens))
print('universo',len(univ),'alvo',tam,'por rotulo',{r:len(v) for r,v in estr.items()},'cotas',cota,'controle',len(ctrl))
print('pacote',len(pac))
