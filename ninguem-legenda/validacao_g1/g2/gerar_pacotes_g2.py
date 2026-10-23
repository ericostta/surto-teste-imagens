#!/usr/bin/env python3
"""Prepara (sem enviar nem executar) os pacotes cegos da G2 a partir do lote G1 congelado.
Códigos opacos e ordem são DERIVADOS por hash do conjunto congelado e do código interno: determinístico, reprodutível, sem frase-semente e sem sorteio.
Revisão 2 (decisões de Eri de 23/10, 00h27):
- Trilha 'triagem' (preditores Claude): SOMENTE codigo, foto (conceito fotográfico), na_foto e a instrução da tarefa de previsão
  (texto de prompts/preditor.md, copiado sem alteração). NÃO contém o FORA DO ENQUADRAMENTO de nenhum item.
- Trilha 'externa' (ChatGPT): codigo, foto, na_foto, fora, mais a referência editorial para o avaliador (g2/referencia_editorial_avaliador.md).
  Sem autoria, intenção, previsões, veredictos, rótulos ou indicação de amostra.
Códigos e ordens diferem entre as trilhas. Mapas ficam em privado/."""
import json, hashlib, os
V='validacao_g1'
sha=lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
man=json.load(open(f'{V}/manifesto_g1.json',encoding='utf-8'))
hconj=man['hash_do_conjunto_incluido']
incl=man['itens_incluidos']['fluxo']+man['itens_incluidos']['desafio']
REF=open(f'{V}/g2/referencia_editorial_avaliador.md',encoding='utf-8').read()
PREDITOR=open('prompts/preditor.md',encoding='utf-8').read()
PREF={'externa':'P','triagem':'T'}
TAG={'externa':'externa','triagem':'triagem-v2'}
mapa={}; hashes={}
os.makedirs(f'{V}/g2/pacotes',exist_ok=True); os.makedirs(f'{V}/g2/privado',exist_ok=True)
for tr in ('externa','triagem'):
    cod={c:PREF[tr]+sha(f'g2|{TAG[tr]}|{hconj}|{c}')[:6].upper() for c in incl}
    assert len(set(cod.values()))==len(incl),'colisão de código'
    ordem=sorted(incl,key=lambda c:sha(f'g2-ordem|{TAG[tr]}|{hconj}|{c}'))
    pac=[]
    for c in ordem:
        it=json.load(open(f'{V}/itens/{c}.json',encoding='utf-8'))
        pac.append({'codigo':cod[c],'foto':it['conceito_foto'],'na_foto':it['na_foto']}|({'fora':it['fora']} if tr=='externa' else {}))
    json.dump(pac,open(f'{V}/g2/pacotes/pacote_{tr}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    if tr=='triagem':
        md="# Tarefa de previsão cega\n\n"+PREDITOR.strip()+"\n\n---\n\nItens (código, foto prevista, NA FOTO). Há 60, em ordem embaralhada.\n"+"".join(f"\n## {p['codigo']}\nFOTO: {p['foto']}\nNA FOTO: {p['na_foto']}\n" for p in pac)
    else:
        md=REF.strip()+"\n\n---\n\nItens a avaliar. Há 60, em ordem embaralhada.\n"+"".join(f"\n## {p['codigo']}\nFOTO: {p['foto']}\nNA FOTO: {p['na_foto']}\nFORA DO ENQUADRAMENTO: {p['fora']}\n" for p in pac)
    open(f'{V}/g2/pacotes/pacote_{tr}.md','w',encoding='utf-8').write(md)
    mapa[tr]={cod[c]:c for c in ordem}
    for ext in ('json','md'): hashes[f'{V}/g2/pacotes/pacote_{tr}.{ext}']=hashlib.sha256(open(f'{V}/g2/pacotes/pacote_{tr}.{ext}','rb').read()).hexdigest()
json.dump({'nota':'MAPA PRIVADO dos códigos opacos da G2. Não entra em pacote, não é entregue a avaliadores, preditores, Críticos ou julgadores.','derivacao':'código = prefixo + SHA-256("g2|etiqueta_da_trilha|hash_do_conjunto|codigo_interno")[:6]; ordem = SHA-256("g2-ordem|etiqueta_da_trilha|hash_do_conjunto|codigo_interno") crescente; etiquetas: externa, triagem-v2','hash_do_conjunto':hconj,'mapa':mapa},open(f'{V}/g2/privado/mapa_codigos_opacos.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(hashes,open(f'{V}/g2/pacotes/hashes_pacotes.json','w'),indent=1)
print(len(incl),'itens;',len(hashes),'arquivos de pacote')
