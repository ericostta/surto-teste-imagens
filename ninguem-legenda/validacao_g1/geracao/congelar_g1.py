#!/usr/bin/env python3
"""Congelamento do lote G1: mapa privado, manifesto de hashes (itens incluídos e excluídos), hash do conjunto.
Não avalia nada. Uso: congelar_g1.py"""
import json, hashlib, glob, os, datetime
sha=lambda b: hashlib.sha256(b).hexdigest()
def shaf(p): return sha(open(p,'rb').read())
V='validacao_g1'
plano={x['codigo']:x for x in json.load(open(f'{V}/geracao/plano_geracao.json'))['itens']}
log=json.load(open(f'{V}/geracao/log_exclusoes_tecnicas.json'))
excl={e['item']:e for e in log['exclusoes']}
sorteio={x['ordem']:x for x in json.load(open('referencia_editorial/sorteio_g1_resultado.json'))['selecionados_em_ordem']}
agora=datetime.datetime.now(datetime.timezone.utc).isoformat()
itens={}
for f in sorted(glob.glob(f'{V}/itens/*.json')):
    c=os.path.basename(f)[:-5]; it=json.load(open(f,encoding='utf-8'))
    canon=json.dumps({k:it[k] for k in ('na_foto','fora','conceito_foto')},ensure_ascii=False,sort_keys=True,separators=(',',':'))
    itens[c]={'arquivo':f,'sha256_arquivo':shaf(f),'sha256_texto_canonico':sha(canon.encode()),'sha256_saida_bruta':shaf(f'{V}/brutos/{c}.txt'),'sha256_prompt_de_geracao':shaf(f'{V}/geracao/prompts/{c}.md')}
incl=[c for c in itens if c not in excl]
fluxo=sorted(c for c in incl if c.startswith('G1-F')); des=sorted(c for c in incl if c.startswith('G1-D'))
assert len(fluxo)==30 and len(des)==30,(len(fluxo),len(des))
mapa={'nota':'MAPA PRIVADO. Não entra em nenhum pacote de avaliação. Células são intenções de geração, não classificações reais. Qualidade editorial e rótulos: vazios até a G2.','criado_em':agora,'itens':[]}
for c in sorted(itens):
    p=plano[c]; it=json.load(open(itens[c]['arquivo'],encoding='utf-8'))
    r={'codigo':c,'amostra':p['amostra'],'ordem_producao':p['ordem_producao'],'status':'excluido_tecnico' if c in excl else 'incluido',
       'procedencia':'fonte A: subagente Criador (modelo sonnet), um por item, prompt do Criador atual sem alteração','processo_de_criacao':'prompts/criador.md + registro.csv + taxonomia.json; uma candidata por item; sem triagem por qualidade; sem rótulos','data_geracao':'2026-10-23',
       'qualidade_editorial':None,'rotulo_externo':None}
    if p['amostra']=='fluxo': r['conceito_sorteado']=sorteio[p['ordem_producao']]['id']
    else: r.update({'celula_intencao':p['celula_intencao'],'ambiente_designado':p['ambiente_designado']})
    if 'substitui' in p: r['substitui']=p['substitui']
    if c in excl: r['exclusao']=excl[c]
    mapa['itens'].append(r)
json.dump(mapa,open(f'{V}/mapa_privado.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
hconj=sha(json.dumps({c:itens[c]['sha256_texto_canonico'] for c in sorted(incl)},sort_keys=True,separators=(',',':')).encode())
man={'lote':'G1','congelado_em':agora,'itens_incluidos':{'fluxo':fluxo,'desafio':des},'n_incluidos':{'fluxo':len(fluxo),'desafio':len(des)},'itens_excluidos_tecnicos':sorted(excl),
 'hash_do_conjunto_incluido':hconj,'itens':itens,
 'arquivos_de_apoio':{p:shaf(p) for p in [f'{V}/geracao/plano_geracao.json',f'{V}/geracao/registro_pre_geracao.json',f'{V}/geracao/log_exclusoes_tecnicas.json',f'{V}/mapa_privado.json',f'{V}/geracao/salvar_itens.py','prompts/criador.md','taxonomia.json','registro.csv','config.json','filtros.py']}}
json.dump(man,open(f'{V}/manifesto_g1.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(incl),hconj)
