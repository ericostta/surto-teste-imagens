---
name: o-que-ninguem-legenda-piloto
description: Piloto manual supervisionado (v0.1) da série O QUE NINGUÉM LEGENDA de @surtodelucidez, Stories 9:16 com fotografia documental, NA FOTO e FORA DO ENQUADRAMENTO. Use quando Eri pedir para criar, avaliar ou revisar uma história dessa série, preparar prompt fotográfico para Gemini/Nano Banana, analisar a foto gerada, compor o Story, ou mandar "12!" sozinho. Nunca publica, nunca integra ao n8n e nunca aciona o contador real.
---

# O QUE NINGUÉM LEGENDA: PILOTO MANUAL v0.1

Status: piloto manual e supervisionado. NÃO é homologação do sistema, do layout nem do núcleo editorial. Eri controla a criação das imagens, as decisões editoriais, a aprovação visual e a publicação. Leia references/versao_limitacoes.md antes da primeira peça de uma conversa.

Gatilho: `12!` sozinho (propõe uma história) ou com instrução (`12! avaliar`, `12! prompt`, `12! foto`, `12! compor`), ou pelo nome da série. `12!` é provisório e não conflita com os gatilhos 1! a 11! conhecidos; Eri pode trocá-lo. Idioma: português do Brasil. Sem travessão no meio de frases.

## A série em uma frase
Fotografia realista e documental, sem rosto por padrão, mais NA FOTO (o que se vê, até 10 palavras) e FORA DO ENQUADRAMENTO (a informação ausente que transforma a leitura da foto, 6 a 22 palavras). A segunda leitura precisa ser genuína e sustentada por algo da cena; surpresa, emoção ou detalhe curioso não bastam. Detalhe em references/identidade_editorial.md.

## Fluxo manual (8 passos, com portas)
1. **Proposta.** Siga references/criador.md. Produza 3 candidatas internamente, passe nos filtros (`python3 scripts/filtros.py candidatas.json --registro registro_piloto.csv`, rodando a partir da pasta da skill) e apresente a MELHOR proposta, com NA FOTO, FORA e conceito da foto. Se Eri pedir, mostre as outras.
2. **Crítico consultivo.** Siga references/critico_operacao.md (Crítico v2.2, previsões cegas, agentes isolados quando houver). Apresente veredicto, justificativa curta, defeitos com trecho e as limitações conhecidas. APROVADA do Crítico não é aprovação editorial.
3. **Decisão de Eri:** aprovar, revisar ou descartar. REVISAR nunca avança para imagem. Máximo de 2 ciclos de revisão por candidata, com reavaliação nova em contexto limpo. AMBÍGUA nunca é apresentada como pronta.
4. **Prompt fotográfico.** Só para proposta aprovada por Eri. Siga references/prompt_fotografico.md. Entregue em BLOCO DE CÓDIGO, pronto para copiar, sem citar o FORA. Rode scripts/checar_prompt.py.
5. **Eri gera a foto manualmente** no Gemini/Nano Banana. Nunca gere imagem nem use serviço pago.
6. **Análise da foto** anexada, conforme references/analise_visual.md (formato, fidelidade, ausência de antecipação, realismo, texto e marcas, composição para o texto). Resultado APTA, AJUSTAR ou REFAZER (máximo de 2 gerações por história).
7. **Composição do Story.** `python3 scripts/compor_story.py --foto FOTO --na-foto "..." --fora "..." --numero LAB-001 --saida story.png` (`--guias` para conferir zonas). Layout PROVISÓRIO. Sem foto, use `--simulacao`, que carimba SIMULAÇÃO VISUAL. Entregue o PNG com SendUserFile e peça avaliação.
8. **Aprovação expressa de Eri.** Só depois de ela dizer que aprova a arte, a peça pode ser considerada apta para publicação MANUAL, feita por ela. A skill nunca publica.

## Regras que não mudam
- A foto não antecipa a revelação do FORA e não precisa mostrar o que está fora do enquadramento. O prompt fotográfico preserva a relação entre foto e NA FOTO.
- Prompts de imagem sempre em bloco de código.
- Assinatura: apenas @surtodelucidez. Topo: O QUE NINGUÉM LEGENDA e número. Numeração 001, 002... exclusiva da série; peças de teste usam LAB-001, LAB-002. O número público só é consumido depois que Eri confirmar a publicação. Não toque no contador real. Regras em references/assinatura_numeracao.md.
- Nenhuma decisão de composição visual está congelada. Mudanças de posição, tamanho, hierarquia e texto dependem de aprovação expressa de Eri.
- Não use os textos do laboratório (12 do lote cego, 60 da G1, 6 arbitrados) como exemplo nem como molde.
- Produção insuficiente reduz a oferta: nunca force uma história fraca para cumprir cadência.

## Registro
Mantenha o registro do piloto (assets/registro_piloto_modelo.csv). Se Eri anexar o CSV, leia-o e use-o nos filtros e na numeração. Ao fim de cada peça, entregue o CSV atualizado com SendUserFile para ela guardar.

## Proibições
Não integrar ao n8n, não inserir na fila, não alterar a grade, não publicar, não comprar créditos nem contratar ferramentas, não gerar imagens pagas, não modificar o contador real, não promover a candidata C1b, não executar as 72 avaliações da verificação experimental, não alterar dados experimentais congelados.

## Limitações atuais
O Crítico v2.2 é provisório e consultivo; o núcleo editorial e o layout não estão homologados; avaliadores são da mesma família de modelos. Ver references/versao_limitacoes.md.
