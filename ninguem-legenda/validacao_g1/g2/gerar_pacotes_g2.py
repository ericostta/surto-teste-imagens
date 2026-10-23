#!/usr/bin/env python3
"""Prepara (sem enviar nem executar) os pacotes cegos da G2 a partir do lote G1 congelado.
Códigos opacos e ordem são DERIVADOS por hash do conjunto congelado e do código interno: determinístico, reprodutível, sem frase-semente e sem sorteio.
Trilhas: 'externa' (rotulagem pelo avaliador externo) e 'triagem' (leitura cega dos subagentes de triagem), com códigos e ordens diferentes.
O pacote contém somente: codigo, foto, na_foto, fora. Mapas ficam em privado/."""
import json, hashlib, os
V='validacao_g1'
sha=lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
man=json.load(open(f'{V}/manifesto_g1.json',encoding='utf-8'))
hconj=man['hash_do_conjunto_incluido']
incl=man['itens_incluidos']['fluxo']+man['itens_incluidos']['desafio']
CABEC={'externa':"""# Avaliação de candidatas: O QUE NINGUÉM LEGENDA

São 60 itens, em ordem embaralhada. Cada item tem uma foto (descrita), um NA FOTO (a leitura imediata) e um FORA DO ENQUADRAMENTO (a revelação). A série mostra uma parte na foto e revela o resto no texto.

Para cada item, responda BOA, RUIM ou AMBÍGUA. Critério único: depois de ler o FORA DO ENQUADRAMENTO, você tem um motivo para olhar a foto de novo?
Comentário é opcional. Pode responder em linhas assim:

    P1A2B3C: BOA
    P4D5E6F: RUIM (previsível)
    P7A8B9C: AMBÍGUA (não entendi o gesto)

A foto ainda não existe: o texto descreve a foto prevista. Use apenas o que está no item. Os códigos não têm significado.
""",
'triagem':"""# Leitura cega de triagem: O QUE NINGUÉM LEGENDA

São 60 itens, em ordem embaralhada. Cada item tem foto (descrita), NA FOTO e FORA DO ENQUADRAMENTO.
Para cada item, preveja BOA, RUIM ou AMBÍGUA pelo critério único: depois de ler o FORA DO ENQUADRAMENTO, há motivo para olhar a foto de novo?
Responda uma linha por item: CÓDIGO: RÓTULO (motivo em até 12 palavras). Use apenas o que está no item. Os códigos não têm significado. Sua resposta é um sinal de triagem, não um rótulo.
"""}
PREF={'externa':'P','triagem':'T'}
mapa={}; hashes={}
os.makedirs(f'{V}/g2/pacotes',exist_ok=True); os.makedirs(f'{V}/g2/privado',exist_ok=True)
for tr in ('externa','triagem'):
    cod={c:PREF[tr]+sha(f'g2|{tr}|{hconj}|{c}')[:6].upper() for c in incl}
    assert len(set(cod.values()))==len(incl),'colisão de código'
    ordem=sorted(incl,key=lambda c:sha(f'g2-ordem|{tr}|{hconj}|{c}'))
    pac=[]
    for c in ordem:
        it=json.load(open(f'{V}/itens/{c}.json',encoding='utf-8'))
        pac.append({'codigo':cod[c],'foto':it['conceito_foto'],'na_foto':it['na_foto'],'fora':it['fora']})
    json.dump(pac,open(f'{V}/g2/pacotes/pacote_{tr}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    md=CABEC[tr]+"\n"+"".join(f"\n## {p['codigo']}\nFOTO: {p['foto']}\nNA FOTO: {p['na_foto']}\nFORA DO ENQUADRAMENTO: {p['fora']}\n" for p in pac)
    open(f'{V}/g2/pacotes/pacote_{tr}.md','w',encoding='utf-8').write(md)
    mapa[tr]={cod[c]:c for c in ordem}
    for ext in ('json','md'): hashes[f'{V}/g2/pacotes/pacote_{tr}.{ext}']=hashlib.sha256(open(f'{V}/g2/pacotes/pacote_{tr}.{ext}','rb').read()).hexdigest()
json.dump({'nota':'MAPA PRIVADO dos códigos opacos da G2. Não entra em pacote, não é entregue a avaliadores, preditores, Críticos ou julgadores.','derivacao':'código = prefixo + SHA-256("g2|trilha|hash_do_conjunto|codigo_interno")[:6]; ordem = SHA-256("g2-ordem|trilha|hash_do_conjunto|codigo_interno") crescente','hash_do_conjunto':hconj,'mapa':mapa},open(f'{V}/g2/privado/mapa_codigos_opacos.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(hashes,open(f'{V}/g2/pacotes/hashes_pacotes.json','w'),indent=1)
print(len(incl),'itens;',len(hashes),'arquivos de pacote')
