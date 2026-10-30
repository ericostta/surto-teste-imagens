---
name: o-que-ninguem-legenda-piloto
description: Piloto manual supervisionado (v0.2.1) da série O QUE NINGUÉM LEGENDA de @surtodelucidez, Stories 9:16 com fotografia documental, NA FOTO e FORA DO ENQUADRAMENTO. Use quando Eri pedir para criar, avaliar ou revisar uma história dessa série, preparar prompt fotográfico para o gerador de imagem escolhido por Eri (Gemini, ChatGPT ou outro), analisar a foto gerada, compor o Story, ou mandar "12!" sozinho. Nunca publica, nunca integra ao n8n e nunca aciona o contador real.
---

# O QUE NINGUÉM LEGENDA: PILOTO MANUAL v0.2.1

Status: piloto manual e supervisionado. NÃO é homologação do sistema, do layout nem do núcleo editorial. Eri controla a criação das imagens, as decisões editoriais, a aprovação visual e a publicação. Leia references/versao_limitacoes.md antes da primeira peça de uma conversa.

Gatilho: `12!` sozinho (propõe uma história) ou com instrução (`12! avaliar`, `12! prompt`, `12! foto`, `12! compor`), ou pelo nome da série. `12!` é provisório e não conflita com os gatilhos 1! a 11! conhecidos; Eri pode trocá-lo. Idioma: português do Brasil. Sem travessão no meio de frases.

## A série em uma frase
Fotografia realista e documental, sem rosto por padrão, mais NA FOTO (o que se vê, até 10 palavras) e FORA DO ENQUADRAMENTO (a informação ausente que transforma a leitura da foto, 6 a 22 palavras). A segunda leitura precisa ser genuína e sustentada por algo da cena; surpresa, emoção ou detalhe curioso não bastam. Detalhe em references/identidade_editorial.md.

## Fluxo manual (8 passos, com portas)
1. **Proposta.** Siga references/criador.md. Produza 3 candidatas internamente, passe nos filtros (`python3 scripts/filtros.py candidatas.json --registro registro_piloto.csv`, rodando a partir da pasta da skill) e apresente a MELHOR proposta, com NA FOTO, FORA e conceito da foto. Se Eri pedir, mostre as outras.
2. **Crítico consultivo.** Siga references/critico_operacao.md (Crítico v2.2, previsões cegas, agentes isolados quando houver). Apresente veredicto, justificativa curta, defeitos com trecho e as limitações conhecidas. APROVADA do Crítico não é aprovação editorial.
3. **Decisão de Eri:** aprovar, revisar ou descartar. REVISAR nunca avança para imagem. Máximo de 2 ciclos de revisão por candidata, com reavaliação nova em contexto limpo. AMBÍGUA nunca é apresentada como pronta.
4. **Prompt fotográfico.** Só para proposta aprovada por Eri. Siga references/prompt_fotografico.md: análise semântica obrigatória da descrição (relações, pistas visuais, antecipação da revelação) mais a conferência lexical auxiliar (scripts/checar_prompt.py, que não é garantia). Entregue em BLOCO DE CÓDIGO, pronto para copiar, sem citar o FORA.
5. **Eri gera a foto manualmente** no gerador que escolher (Gemini/Nano Banana, ChatGPT ou outro; nenhum é exigido nem garante qualidade). Nunca gere imagem nem use serviço pago.
6. **Análise da foto** anexada, conforme references/analise_visual.md (Padrão de Excelência Fotográfica, referência operacional PROVISÓRIA: defeitos impeditivos I1 a I9, incluindo suporte físico plausível, medições de apoio e julgamento humano). Resultado APTA, AJUSTAR ou REFAZER. Limite padrão de 2 correções ou gerações por história; passar disso só com autorização expressa de Eri, registrada (quem autorizou, quando e por quê).
7. **Composição do Story.** `python3 scripts/compor_story.py --foto FOTO --na-foto "..." --fora "..." --numero LAB-001 --saida story.png` (perfil D é o padrão da v0.2.1; `--perfil A`, `--perfil B` e `--perfil C` continuam disponíveis; `--guias` confere zonas; todos são provisórios). Sem foto, use `--simulacao`, que carimba SIMULAÇÃO VISUAL. O script só grava a arte com APROVAÇÃO TÉCNICA: texto que não cabe, elemento em zona de segurança ou número público sem reserva BLOQUEIA. NUNCA altere o texto da história para caber: apresente o bloqueio a Eri, que decide. O relatório inclui o contraste efetivo aproximado do texto; abaixo do limite provisório gera AVISO. Aprovação técnica não é aprovação visual. Entregue o PNG e o .checagem.json com SendUserFile e peça avaliação.
8. **Aprovação expressa de Eri.** Só depois de ela dizer que aprova a arte, a peça pode ser considerada apta para publicação MANUAL, feita por ela. A skill nunca publica.

## Regras que não mudam
- A foto não antecipa a revelação do FORA e não precisa mostrar o que está fora do enquadramento. O prompt fotográfico preserva a relação entre foto e NA FOTO.
- Prompts de imagem sempre em bloco de código.
- Assinatura: apenas @surtodelucidez, com o número da edição discreto logo abaixo dela, à esquerda (perfil D, escolha de Eri na rodada visual de 30/10/2026, layout não homologado; "001" sob o S e o U). Topo: título em duas linhas, O QUE NINGUÉM pequeno e LEGENDA grande em serifa reta. O número público aparece só como 001, 002... (sem "Nº"), exclusivo da série; peças de teste usam LAB-001, LAB-002. Todo número público é RESERVADO antes da composição (`scripts/registro_numeracao.py reservar`) e só é consumido depois que Eri confirmar a publicação manual; número confirmado nunca é reutilizado. Não toque no contador real. Regras e estados em references/assinatura_numeracao.md.
- Nenhuma decisão de composição visual está congelada. Mudanças de posição, tamanho, hierarquia e texto dependem de aprovação expressa de Eri.
- Não use os textos do laboratório (12 do lote cego, 60 da G1, 6 arbitrados) como exemplo nem como molde.
- Produção insuficiente reduz a oferta: nunca force uma história fraca para cumprir cadência.

## Registro
Mantenha o registro do piloto (assets/registro_piloto_modelo.csv). Se Eri anexar o CSV, leia-o e use-o nos filtros e na numeração. Registros legados são lidos, nunca reescritos. Ao fim de cada peça, entregue o CSV atualizado (e o .confirmados.jsonl, se existir) com SendUserFile para ela guardar. Para conferir a própria skill: `python3 scripts/verificar_skill.py` e `python3 testes/test_piloto.py`.

## Proibições
Não integrar ao n8n, não inserir na fila, não alterar a grade, não publicar, não comprar créditos nem contratar ferramentas, não gerar imagens pagas, não modificar o contador real, não promover a candidata C1b, não executar as 72 avaliações da verificação experimental, não alterar dados experimentais congelados.

## Limitações atuais
O Crítico v2.2 é provisório e consultivo; o núcleo editorial e o layout não estão homologados; avaliadores são da mesma família de modelos. Ver references/versao_limitacoes.md.
