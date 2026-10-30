# Entrega: skill O QUE NINGUÉM LEGENDA, piloto manual v0.2 (30/10/2026)

Pacote: `dist/o-que-ninguem-legenda-piloto-v0.2.zip` (SHA-256 5c274e32c6e4d0550ea964cd245191ae10d2c9b24383bc28fc4aba27341df218), idêntico à fonte em `v0.2/o-que-ninguem-legenda-piloto/`. Registro com hashes de todos os arquivos: `REGISTRO_VERSAO_v0.2.json`. A v0.1.1 e seu ZIP (SHA-256 7791524d...e6a6a) ficam intactos; a v0.1.1 continua passando em 23 testes e no verificador. Nenhum arquivo versionado anterior foi modificado (git diff vazio antes desta entrega).

Status: desenvolvimento técnico do piloto manual. NÃO é homologação editorial nem autorização operacional. Nada foi publicado, integrado ao n8n, à fila, à grade ou ao contador real.

## O que mudou (e por quê)

| Alteração | Arquivos | Justificativa |
|---|---|---|
| Número público exibido como 001, sem "Nº" | scripts/compor_story.py, references/assinatura_numeracao.md, SKILL.md | Decisão de Eri de 24/10, confirmada em 30/10 |
| Perfil C (padrão): número discreto (11 px, mesma transparência da assinatura, 8 px abaixo) alinhado à esquerda sob @surtodelucidez; assinatura 22 px; rótulos alfa 215; degradê do topo reforçado; título sozinho no topo. Perfis A e B preservados | scripts/compor_story.py, references/assinatura_numeracao.md | Decisões de Eri de 24 a 30/10 e prévia aprovada visualmente. NÃO homologa o layout inteiro |
| Contraste efetivo do texto no relatório de composição (aviso, nunca bloqueio) e posição de título, número e assinatura em `.checagem.json` | scripts/compor_story.py, config.json | Padrão fotográfico verificável; limiares provisórios |
| Padrão de Excelência Fotográfica provisório: defeitos I1 a I9, o que é verificável por código, resultados APTA/AJUSTAR/REFAZER, faixa de atenção de resolução (810 a 1079 px) | references/analise_visual.md, config.json, scripts/analisar_foto.py | Auditoria de 29/10, item 7 da decisão de Eri |
| Ferramenta de inclinação de haste | scripts/medir_inclinacao.py | Defeito I1 (suporte físico), lição do LAB-001. Só Pillow, sem dependência nova |
| Gerador de imagem não exclusivo | SKILL.md, references/prompt_fotografico.md, references/versao_limitacoes.md, compor_story.py (texto do marcador) | Decisão de Eri; o ChatGPT foi o gerador efetivo |
| Limite padrão de duas correções, com exceção só por autorização expressa registrada | config.json, SKILL.md, references/analise_visual.md, references/prompt_fotografico.md | O LAB-001 usou 14 versões por exceções dadas na conversa, sem registro formal |
| Lição de prompt: cena fisicamente estável, pontos de contato em vez de ângulos, uma mudança por vez, sujeito pequeno e alto | references/prompt_fotografico.md | Evidência do LAB-001 (v2 a v14) |
| Verificador e testes ampliados | scripts/verificar_skill.py, testes/test_piloto.py | 39 testes (23 anteriores mais 16 novos), todos OK |

Não alterados: Crítico v2.2 (hash conferido), preditor cego, criador, filtros e janelas de repetição, taxonomia, estados e registro de numeração, fontes e licença, SKILL de outras séries, n8n, grade, fila, contador real, lacres, C1b, Emenda 2, L8CFD, as 72 avaliações.

## Conflitos entre decisões recentes e especificações antigas (status)
- Número no topo à direita (v0.1.1) contra número sob a assinatura (decisão): resolvido no perfil C; A e B mantêm o comportamento antigo, só sem "Nº".
- "20% menor": substituído pela orientação visual de Eri (pequeno e sutil como no Círculo Tipográfico); valor atual 11 px, tamanho final dependente da aprovação dela.
- Assinatura: mantida em 22 px, a última composição vista por Eri. Eri disse para não reduzir de novo; se os 22 px não forem os da composição aprovada, ela deve avisar.
- Gerador Gemini contra ChatGPT: resolvido (não exclusivo).
- Limite de duas gerações contra as exceções do LAB-001: resolvido por exceção registrada.
- Medidas finais: fixadas a partir da prévia aprovada visualmente (`pilotos/LAB-001/LAB-001_B215_v14_tratada_previa_limpa.png`), não de uma imagem final homologada.

## Limitações restantes
1. Layout, fonte, margens, zonas de segurança, posição e tamanho do número: provisórios, não homologados.
2. Padrão fotográfico: limiares provisórios; uma única cena calibrada; contraste medido sem a sombra do texto e aproximado.
3. O número de 11 px é pequeno por desejo de Eri; legível em zoom, quase imperceptível em tamanho normal.
4. Crítico v2.2 só consultivo; avaliadores da mesma família de modelos; nenhuma promoção de versão experimental.
5. A arte final do LAB-001 e a foto como peça editorial seguem pendentes de aprovação expressa de Eri. A foto v14 teve só aprovação visual.
6. Política de rotulagem de conteúdo gerado por IA nas plataformas não foi verificada (necessária antes de qualquer publicação).
7. Decisão sobre L8CFD e sobre a verificação C1b: separada e pendente, sem impedir a v0.2.

## Correção de medição (registro de honestidade)
O script externo `pilotos/LAB-001/medir_contraste.py`, usado nas auditorias das fotos v11 a v14, mede com os parâmetros do perfil B (rótulos em alfa 170 e degradê do topo mais leve), não com o layout de teste B215/C. Por isso o contraste do rótulo NA FOTO nessas auditorias ficou subestimado. Medido pelo próprio compor_story.py no perfil C, a v14 original já passa os limiares provisórios (rótulo NA FOTO média 5,24 e pior decil 3,74); a v14 tratada dá 6,43 e 4,79. O ajuste de tom atrás do rótulo, aplicado antes da aprovação, foi portanto desnecessário pelo critério atual, embora inofensivo. A prévia que Eri aprovou usa a foto tratada. Se Eri preferir a foto sem tratamento, a prévia pode ser refeita com a v14 original.

## Como usar
`python3 scripts/compor_story.py --foto FOTO --na-foto "..." --fora "..." --numero LAB-001 --saida story.png` (perfil C por padrão). Conferir a skill: `python3 scripts/verificar_skill.py` e `python3 testes/test_piloto.py`.

## Decisões que continuam com Eri
Aprovação da arte final do LAB-001; tamanho final do número e da assinatura; homologação (ou não) de layout, fonte, limiares e Padrão Fotográfico; uso da foto tratada ou original; L8CFD e a verificação C1b; política de rotulagem de IA; qualquer publicação.
