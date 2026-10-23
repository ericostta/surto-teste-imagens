#!/usr/bin/env python3
"""Salva, sem alterar, a saída de cada subagente Criador (G1). Instrumento de registro, não de avaliação.
Uso: salvar_itens.py DIR_TASKS DIR_DESTINO CODIGO...   (extrai o JSON da última mensagem do agente cujo id == CODIGO)"""
import json, glob, re, sys, os, hashlib
def ultima_msg(f):
    last=None
    for line in open(f,encoding='utf-8'):
        try: o=json.loads(line)
        except Exception: continue
        m=o.get('message') or {}
        if m.get('role')=='assistant':
            c=m.get('content')
            t=''.join(b.get('text','') for b in c if isinstance(b,dict) and b.get('type')=='text') if isinstance(c,list) else (c or '')
            if t.strip(): last=t
    return last
def main():
    tasks,dest,codigos=sys.argv[1],sys.argv[2],set(sys.argv[3:])
    os.makedirs(dest+'/itens',exist_ok=True); os.makedirs(dest+'/brutos',exist_ok=True)
    achados={}
    for f in glob.glob(tasks+'/*.output'):
        t=ultima_msg(f)
        if not t: continue
        m=re.search(r'\{.*\}',t,re.S)
        if not m: continue
        try: j=json.loads(m.group(0))
        except Exception: continue
        if j.get('id') in codigos: achados.setdefault(j['id'],[]).append((t,j))
    faltam=codigos-set(achados); dup=[k for k,v in achados.items() if len(v)>1]
    if faltam or dup: sys.exit(f'faltam={sorted(faltam)} duplicados={dup}')
    for k,[(t,j)] in achados.items():
        open(f'{dest}/brutos/{k}.txt','w',encoding='utf-8').write(t)
        json.dump(j,open(f'{dest}/itens/{k}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1); open(f'{dest}/itens/{k}.json','a').write('\n')
    print(len(achados),'itens salvos')
main()
