---
name: "cena-cortada"
description: "Gera a edição diária da série CENA CORTADA de @surtodelucidez para Stories 9:16: cena breve e ambígua, trio de fotos do ambiente na película, numeração 000/001/002. Gatilho: 13!"
---

# CENA CORTADA (@surtodelucidez)

Gatilho fixo: Eri manda "13!" sozinho (ou pede a edição do dia da Cena Cortada). Nesse caso, não pedir confirmação de layout nem de cena. Escolher a cena sozinho, conforme as regras abaixo, e seguir o fluxo. Idioma: português do Brasil. Sem travessão no meio de frases.

A série é um Story único 1080x1920 (9:16): mesa de madeira escura vista de cima, película de cinema ondulada com três fotos, tesoura metálica cortando a tira, e uma folha de papel envelhecido com título, cena e assinatura.

## 0. A máscara é fixa (decisão de Eri, 02/11/2026)

A arte da edição 001 ("O troco da vez", lotérica) é a MÁSCARA de todas as publicações. Papel, madeira, tesoura, gravação "@surtodelucidez" na lâmina, película e brilho ficam idênticos em toda edição. Todo dia mudam SOMENTE quatro coisas: título, texto da cena no papel, as três fotos de prévia e a numeração da película. Nunca redesenhar, "melhorar" ou regenerar a arte por gerador de imagem. A tentativa de dar ultra realismo ao molde com Gemini foi rejeitada por Eri em 30/10/2026; não repetir.

## 1. Conceito editorial

Cena breve, concreta e humana, que deixa mais de uma interpretação aberta. As leituras respondem à mesma pergunta aberta e competem pelo sentido do acontecimento central, cada uma com apoio observável próprio na cena. A película "corta" a cena: o leitor vê o ambiente, nunca a ação, e o texto conta o recorte.

Se existir uma versão mais nova do prompt editorial de Eri (v1.4 ou superior, ou cena_cortada_prompt_v1_3_b6g.txt no Drive do Surto, com a lista de situações já trabalhadas), ela prevalece sobre esta seção no que for mais específico.

- Título curto (2 a 5 palavras), concreto, sem explicar a cena.
- Texto de 55 a 75 palavras (limite máximo 80), em 5 a 7 linhas no papel, em prosa, presente do indicativo.
- Dois personagens com nome próprio (ou um personagem e um objeto), um gesto cotidiano, uma pequena disputa ou desvio, sem violência explícita.
- Final aberto: nunca moral da história, nunca julgamento, nunca explicar a intenção de ninguém. Quem lê decide o que aconteceu.
- Ambiente reconhecível e do dia a dia brasileiro (lotérica, padaria, ponto de ônibus, cozinha, sala de espera, mesa posta).
- Não repetir ambiente, situação nem estrutura de frase das edições anteriores. Consultar o registro (seção 8) e a lista de situações do prompt v1.3 antes de escolher.
- Sem texto de autoajuda, sem hashtag, sem emoji, sem travessão no meio de frases.
- "Cena Cortada" aparece uma única vez na arte (assinatura).

Edição de referência aprovada (padrão de tom e tamanho), "O troco da vez", 69 palavras:
"Na fila da lotérica, Nilza paga o bolão do escritório e recebe o troco. Rui, atrás dela, estende a mão para pegar o recibo que ficou no balcão. Ela o puxa primeiro, dobra em quatro e guarda na bolsa. Rui abaixa a mão devagar e olha para o relógio. Quando ela sai, ele fica no mesmo lugar, deixa passar a próxima pessoa e só então avança até o guichê."

## 2. Numeração da película (regra fixa)

O número do meio é SEMPRE o número da edição do dia. Esquerda é a edição anterior, direita é a seguinte.

- Primeira publicação (edição 001, 03/11/2026): 000 | 001 | 002, destaque no 001.
- Segunda (edição 002, 04/11/2026): 001 | 002 | 003, destaque no 002. E assim por diante, em 3 dígitos.
- O destaque do número do dia é sutil: mais claro e de tinta mais cheia, mesmo tamanho e mesma família de cor, sem brilho artificial.
- Só avança com publicação confirmada. Nunca pular nem repetir número; manter o registro (seção 8).

## 3. Trio de fotos: prévia que desperta a imaginação

As três fotos são só um estímulo inicial para o leitor imaginar a cena. Mostram o LUGAR, nunca a ação, e não entregam o texto.

Regras (decididas por Eri em 02/11/2026):
- As três fotos caracterizam o MESMO local, mesma luz, mesma hora do dia, mesmo estilo fotográfico realista, de ângulos ou perspectivas diferentes, de modo que se complementem e juntas deem ao leitor a compreensão inicial do espaço.
- MEIO (edição do dia): plano fechado do ponto central da cena (ex.: balcão com bilhetes).
- ESQUERDA: plano aberto do ambiente inteiro, mostrando onde a cena acontece.
- DIREITA: outro ângulo ou outro lado do mesmo lugar, com detalhe complementar.
- Sem muitos detalhes: só o suficiente para disparar a imaginação. Sem entregar a cena por completo.
- Evitar pessoas: nenhuma pessoa, mão, rosto ou silhueta.
- Mesmo padrão de qualidade das fotos da edição 001: aparência de foto real de câmera profissional, luz natural quente, cores naturais, nitidez preservada.
- Proibições: nenhum texto legível, número legível, marca ou logotipo; nenhuma cor azulada ou rosada artificial; sem filtro sépia; sem moldura, borda, legenda ou marca d'água.

Geração das fotos: o próprio Claude gera o trio pela Kairogen (plano Pro), sem pedir que Eri leve imagens. Decisão de Eri em 02/11/2026: TODAS as fotos da série são geradas com o **z-image-turbo** (1 crédito por imagem, 3 por trio, R$ 0,48 por edição). Não trocar de modelo por conta própria, nem quando uma foto falhar: refazer no mesmo modelo; só mudar se Eri pedir. Regras de uso, aprendidas no teste:
- Chamar generate_image uma vez por foto, com size "3:2", expected_credits 1 e wait_for_completion true. Não usar negative_prompt (o modelo não o aceita e a chamada falha com erro 400); as exclusões vão no próprio prompt, em "Sem ...".
- Começar cada prompt com "Uma única fotografia realista, em quadro cheio". NUNCA escrever "fotos da série", "três fotos" nem pedir variações: o modelo devolve uma folha de contato com seis quadros.
- Para as três fotos parecerem o mesmo lugar, escrever UMA VEZ uma descrição fixa do ambiente (cor das paredes, tipo e cor das cadeiras ou móveis, piso, janela, luz) e repeti-la idêntica no início dos três prompts, mudando só o plano e o foco.
- Conferir cada foto: mesmo lugar, sem pessoas, sem texto legível, cores naturais e quentes (o modelo tende a sair dessaturado, quase sépia: se acontecer, refazer essa foto pedindo "cores vivas e naturais, balanço de branco neutro"), objeto-chave da cena reconhecível. Refazer só a foto reprovada, no máximo 2 vezes por foto.
- Custo esperado: 3 créditos por trio (R$ 0,48), até 7 com refações.

Se Eri pedir o prompt para usar fora da Kairogen, entregar SEMPRE em bloco de código, pronto para copiar inteiro. Modelo de prompt por foto (preencher AMBIENTE_FIXO, PLANO, FOCO):

```
Uma única fotografia realista, em quadro cheio, de AMBIENTE_FIXO. PLANO. Foco principal: FOCO.
Luz natural quente de fim de tarde entrando pela janela. Câmera full frame, lente 35mm, f/8, tudo em foco, cores vivas e naturais, alta definição, aparência de foto real de câmera profissional.
Sem pessoas, sem mãos, sem rostos, sem texto legível, sem números legíveis, sem logotipos, sem filtro sépia, sem moldura.
```

## 4. Composição da arte (por programa, nunca por gerador)

A arte é composta pelo script molde/compor_cena_cortada.py (Python com OpenCV, numpy e Pillow), que parte do molde reconstruído da arte aprovada da edição 001:

```
python3 molde/compor_cena_cortada.py --edicao N --titulo "..." --cena "..." --esq FOTO_ESQ --meio FOTO_MEIO --dir FOTO_DIR --saida arte.png
```

O script troca só título, texto, as três fotos e a numeração (número do meio = edição do dia, anterior à esquerda, seguinte à direita). Saída 1080x1920. Avisa se a cena sair da faixa de 55 a 80 palavras.

O que o molde contém (pasta molde/): compor_cena_cortada.py, config.json (janelas das fotos, borda rasgada, posição dos números), base_clean.png (madeira, papel limpo, tesoura com a gravação "@surtodelucidez", película sem fotos nem números), fonts/ e referencia/ (arte 001 aprovada em 1080x1920 e scripts de preparo).

Regras do molde:
- Mesa de madeira escura, papel envelhecido, película ondulada em S, tesoura cortando entre o quadro do meio e o da direita (rasgo de um lado, tracejado branco do outro). A gravação da lâmina vem do molde, nunca de gerador.
- Zonas seguras do Instagram: nada importante nos 250 px do topo nem nos 350 px da base.
- Tinta do texto: preto profundo (#0D0D0D). Título em serifa de destaque, corpo em serifa, "CENA CORTADA" em negrito espaçado e "@surtodelucidez" menor, com traço fino acima.
- Margens de texto no papel de no mínimo 70 px.

Limites conhecidos do molde v0.1 (02/11/2026): foi reconstruído da arte de 1080x1920, não do master em alta resolução; a tipografia é a mais próxima disponível (Noto Serif e Inter), não a original; o brilho sobre as fotos novas é sintético e leve. Se Eri achar o master original, substituir o molde. Se a pasta molde/ não estiver disponível na sessão, avisar Eri em vez de improvisar ou regenerar a arte por gerador.

## 5. Conferência antes de entregar

- Texto do papel idêntico ao aprovado, sem letra trocada; gravação da lâmina correta ("@surtodelucidez").
- Numeração correta (meio = edição do dia, destaque no meio).
- Trio de fotos do mesmo ambiente, sem pessoas, sem texto legível, luz coerente, sem entregar a ação.
- Fotos com aparência de fotografia real (Eri já rejeitou acabamento que não parecia foto).
- Tinta escura e legível; margens e zonas seguras respeitadas.
- Dimensão final 1080x1920.
- Ampliar e conferir título, parágrafo e rodapé antes de entregar.

## 6. Publicação e fila (n8n)

- Horário na grade diária: 11h00, entre a Permissão do Dia (10h) e o X (12h), conforme a grade de 15 publicações de 23/10/2026.
- Arquivo na fila do GitHub (repositório ericostta/surto-teste-imagens, pasta fila/): AAAAMMDD_1100_cenacortada.png.
- n8n, fluxo Fila Stories: o agendamento passa a incluir 11h, ficando 0 6,7,8,10,11,13,15,19 * * * (fuso America/Sao_Paulo). O código atual já pega o arquivo pelo horário. Ligar o 11h somente quando houver arte na fila, para o fluxo não rodar vazio.
- Tarefa diária das 6h47: escolhe a cena, gera o trio pela Kairogen, compõe a arte com o molde e coloca na fila antes das 11h00. Se falhar qualquer etapa (molde ausente, foto reprovada, sem escrita no repositório), não enfileirar nada e avisar Eri; nunca publicar arte improvisada.
- Todo Story do @surtodelucidez marca @eri_costta (user_tags), conforme a prática da conta.
- Primeira publicação: edição 001, "O troco da vez" (lotérica), em 03/11/2026, película 000 | 001 | 002. Edição 002 em 04/11/2026, película 001 | 002 | 003.

## 7. Entrega manual (execução avulsa com 13!)

Entregar a Eri: título, cena (com contagem de palavras), conferência editorial (pergunta aberta e as duas leituras com o apoio observável de cada uma) e a arte 1080x1920 com SendUserFile. Eri aprova antes de qualquer coisa ir para a fila, até que ela declare a série em regime automático.

## 8. Registro por edição

Anotar a cada edição: número, data, título, ambiente, situação, personagens, horário de publicação, status (aprovada, enfileirada, publicada confirmada). Usar para evitar repetição e para a numeração.

| Nº | Data | Título | Ambiente | Status |
|---|---|---|---|---|
| 001 | 03/11/2026 | O troco da vez | lotérica | arte aprovada; publicação prevista 11h, a confirmar |
| 002 | 04/11/2026 | proposta: O número 47 (Telma cede a ficha 47 a Davi) | sala de espera | proposta, não aprovada; Eri perguntou o porquê do número e não confirmou o título |

## 9. Pendências abertas

- Eri aprovar o molde v0.1 (ou pedir ajustes de fonte, números ou brilho).
- Confirmar a cena e o título da edição 002.
- Confirmar a publicação da 001 (consome o número).
- Gerar e aprovar o trio real da edição 002 com as regras do Z-Image Turbo e ver se o resultado agrada (o teste de 02/11 passou na qualidade segundo Eri, mas o lugar variou entre as fotos).
- Ligar o 11h no fluxo Fila Stories e incluir a série na tarefa das 6h47.
