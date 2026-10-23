# Proposta técnica: Padrão de Excelência Fotográfica de O QUE NINGUÉM LEGENDA

Data: 23/10/2026. Referência: skill piloto manual v0.1.1 (commit f63c516). Estado: PROPOSTA para aprovação. Nenhum arquivo da skill, congelado ou experimental foi alterado. Nada foi publicado, comprado, integrado ao n8n, à grade, à fila ou ao contador real. As 72 avaliações seguem suspensas. O padrão é neutro quanto ao gerador: vale para Gemini/Nano Banana agora e para o Kairogen quando for contratado.

Arquivos novos desta etapa, todos em `pilotos/LAB-001/`: `foto_real_L8CFD_gemini_original.jpg` (original intacto, SHA-256 e06e4d8ad6bd70ebd6601729fa04898ace6877a7b48d7680d88a26d80a77ec7e), `LAB-001_B_foto_real.png` e `LAB-001_B_foto_real_guias.png` (composição simulada no perfil B, com faixa de simulação).

---

## A. Especificação do Padrão

Objetivo: fotografias percebidas como registros reais, com qualidade editorial, que sustentem a segunda leitura depois do FORA. Uma foto só é APTA se passar em três camadas independentes, nenhuma compensando a outra:

1. **Verificações determinísticas (medem números, não beleza).** Dimensões, proporção, formato, integridade do arquivo, hash, fator de ampliação até 1080 x 1920, compressão, contraste medido do texto sobre a foto, sobreposição aproximada do texto com o sujeito, zonas de segurança.
2. **Análise visual semântica obrigatória, feita pelo Claude com ampliação das regiões críticas** (contatos entre objetos e superfícies, bordas, água, reflexos, mãos, textos escondidos). É julgamento, sujeito a erro nos dois sentidos, e deve apontar região, defeito, efeito e correção.
3. **Decisão humana final de Eri.** A skill nunca aprova arte nem foto sozinha.

Eixos avaliados: realismo fotográfico, plausibilidade física, qualidade técnica, linguagem documental, coerência com o NA FOTO, preservação do FORA, especificidade (a foto não poderia ser trocada por uma genérica sem perda) e compatibilidade com a tipografia.

Resultados, como pedido: APTA, AJUSTAR, REFAZER. Sem pontuação numérica.

## B. Critérios obrigatórios e defeitos impeditivos

Um defeito impeditivo bloqueia APTA e nenhum ponto positivo o compensa. Todo defeito apontado precisa de região, demonstração e efeito; sem isso é observação, não defeito.

| Id | Critério | Verificação | Impeditivo para APTA |
|---|---|---|---|
| I1 | Objeto fisicamente implausível (apoio, equilíbrio, gravidade, pontos de contato) | visual, com ampliação | sim, se demonstrado |
| I2 | Geometria, anatomia ou continuidade de superfície comprometidas; duplicações | visual | sim |
| I3 | Artefato evidente (texto ou marca ilegível, deformação, líquido incoerente) | visual | sim |
| I4 | Contradição com o NA FOTO ou com o conceito fotográfico | visual | sim |
| I5 | Antecipação explícita do FORA (pessoa, etiqueta, objeto que revela a relação) | visual | sim |
| I6 | Resolução insuficiente: largura nativa menor que 810 px (ampliação acima de 1,33x até 1080); entre 810 e 1079 px é atenção e exige olhar humano na arte | automático | sim |
| I7 | Arquivo íntegro, proporção 9:16 (tolerância de 1%), formato aceito | automático | sim |
| I8 | Composição que inviabiliza a leitura: sujeito sob os blocos de texto, ou contraste abaixo do limite | automático mais visual | sim, na etapa da arte |
| I9 | Desvio das restrições de composição pedidas no prompt (posição do sujeito, áreas calmas) | visual | AJUSTAR (não é falha de realismo) |

Limiares de contraste, medidos no render sem o texto (com degradê e sombra aplicados): NA FOTO e FORA, média de pelo menos 4,5:1 e pior decil de pelo menos 3:1; título e número, média de pelo menos 3:1. Todos os limiares (I6 e contraste) são **provisórios** e devem ser calibrados com as primeiras fotos reais antes de virarem regra.

## C. Fluxo de auditoria

**Etapa 1, fotografia original (antes de qualquer texto).**
1. Receber a foto; calcular hash, dimensões, fator de ampliação, compressão (script).
2. Análise semântica com ampliação de ao menos: contatos com o piso e com paredes, bordas do sujeito, líquidos e reflexos, fundo, cantos. Registrar achados com região, defeito, efeito e correção.
3. Verificar o que a imagem comunica antes do FORA e se algo o antecipa ou contradiz o NA FOTO. Elementos que só o FORA revela não precisam aparecer.
4. Decidir APTA, AJUSTAR ou REFAZER. Eri confirma ou diverge, e a divergência é registrada.

**Etapa 2, arte completa (só com foto APTA na etapa 1).**
1. Compor no perfil escolhido (B nesta fase), com a numeração reservada ou LAB-.
2. O compositor mede e registra contraste sob cada bloco e fração do texto sobre o sujeito (novo); o bloqueio técnico existente continua (texto não cabe, zonas de segurança, travessão).
3. Análise semântica da arte: preservação da foto, hierarquia, legibilidade em tamanho de celular, sobreposição prejudicial.
4. Decisão APTA, AJUSTAR ou REFAZER; aprovação visual final de Eri.

As duas etapas são independentes: foto excelente pode dar arte ruim, e o inverso não vale.

**Registro.** Um arquivo de auditoria por edição, só de acréscimo, fora do CSV de registro (para não alterar as colunas do CSV): hash da foto, tentativa, achados, decisão da skill, decisão de Eri, parâmetros do gerador.

## D. Correção e nova geração

Para AJUSTAR ou REFAZER a skill: (1) explica o problema concretamente; (2) diz se a correção é visual (recorte, tratamento limitado) ou exige nova geração; (3) entrega prompt revisado em bloco de código, com a diferença em relação ao anterior marcada; (4) preserva integralmente a história aprovada; (5) pede nova imagem a Eri; (6) repete a auditoria.

Limite: a imagem original mais **no máximo duas tentativas de correção**. Depois disso a skill apresenta diagnóstico e Eri decide: continuar, substituir a fotografia ou interromper. Foto insuficiente é corrigida, refeita ou descartada, nunca publicada para cumprir a programação.

**Neutralidade do gerador.** O prompt descreve a cena e não depende de ferramenta. Parâmetros do gerador (modelo, resolução pedida, proporção, seed, custo) ficam num campo separado do registro. Para o Gemini/Nano Banana: pedir sempre a maior resolução disponível no momento de gerar. Para o Kairogen: consultar modelos, resoluções e custo estimado no momento da contratação, sem gerar nada antes de autorização expressa. Não verifiquei aqui as resoluções máximas de nenhum dos dois.

## E. Auditoria demonstrativa: foto do guarda-chuva (L8CFD)

Fora do material de avaliação cega. Arquivo: JPEG 572 x 1024, 68.962 bytes (cerca de 0,94 bit por pixel), ampliação de 1,888x até 1080 x 1920.

**Pontos levantados por vocês, um a um (ampliei contato com o piso, copa/parede e copa/ponta):**

| Ponto | Constatação | Veredito |
|---|---|---|
| Sustentação do guarda-chuva | A haste inclina cerca de 9 graus em direção à parede e a borda da copa encosta na parede à direita; a copa inclina para o mesmo lado, coerente com a haste. A sombra cai para a frente, coerente com a luz vinda da porta ao fundo. Dúvida restante: piso úmido de porcelanato tem pouco atrito, então o cabo poderia escorregar, mas isso não é demonstrável numa foto parada. | Sem defeito demonstrado. Dúvida de cenário, para olhar humano. |
| Ponto de contato da haste com o piso | Cabo reto, com anéis concêntricos de água centrados nele e reflexo escuro sob ele. Contato coerente. | Sem defeito. |
| Estrutura e equilíbrio | Varetas, tira de fechamento com botão, ponteira superior e tecido molhado com gotas se comportam como num guarda-chuva real. A borda da copa termina na parede de modo aceitável. | Sem defeito. |
| Água, poça e sustentação | Poça pequena e clara com anéis ao redor do cabo; à direita há uma mancha escura grande e irregular que pode ser água ou sombra. É maior do que o gotejamento visível sugere. | Observação, não defeito impeditivo. Vale reduzir no prompt. |
| Resolução 572 x 1024 | Abaixo do mínimo de 810 px do critério I6 proposto; a ampliação de 1,89x deixa gotas e bordas moles. | **Defeito demonstrado, impeditivo.** |
| Antecipação do FORA | Nenhuma pessoa, etiqueta, nome ou segundo objeto. O FORA continua preservado. | Sem defeito. |
| Especificidade | Gotas, contato com a parede e corredor específico; não é imagem genérica. | Aprovado. |
| Composição pedida no prompt | O prompt pedia o sujeito na metade superior e o terço inferior calmo. A foto tem copa entre 45% e 63% da altura, haste e poça até 84%. | **Desvio (I9).** |

**Compatibilidade com a proposta B (composição simulada, medida em pixels):**
- O script deu aprovação técnica, mas ele não mede contraste nem sobreposição com o sujeito.
- Título: contraste do branco sobre a foto de 2,3:1 em média e 1,3:1 no pior decil (sobre a janela clara). Número LAB-001: 1,6:1. Ambos abaixo do limite proposto.
- NA FOTO: 60% da caixa de texto cai sobre a copa; a haste cruza o bloco FORA.
- O FORA fica legível sobre o degradê. Ele está sobre piso, haste e sombra.

**Classificação (julgamento do Claude, sujeito à sua revisão):** fotografia AJUSTAR (resolução e composição, sem alterar a ideia nem a atmosfera); arte AJUSTAR (contraste do título/número e sobreposição). Não é REFAZER: o realismo e a plausibilidade não apresentaram defeito demonstrado. Não é APTA: há defeito impeditivo.

**Limite desta auditoria:** foi feita por modelo, sobre um arquivo pequeno em que anomalias finas podem não ser distinguíveis de compressão.

**Prompt corrigido** (preserva cena, luz fria e água; muda composição, escala da poça e resolução):

```
Fotografia realista de linguagem documental, formato vertical 9:16, na maior resolução disponível (pelo menos 1080 x 1920 pixels nativos).

Cena: um guarda-chuva preto grande, de cabo reto, aberto, em pé sobre o cabo no piso de porcelanato claro de um corredor comum de apartamento, com a copa inclinada para a parede lateral e a borda da copa encostada nessa parede, de modo que o apoio fique evidente. Gotas escorrem pelas varetas e pela borda do tecido. Uma poça pequena e bem delimitada, com anéis concêntricos de água, forma-se ao redor do cabo; o resto do piso apenas levemente úmido. A porta de entrada ao fundo, entreaberta e desfocada, deixa passar luz cinzenta de dia chuvoso.

Ambiente: corredor estreito e comum, paredes lisas em tom claro, rodapé branco, piso de porcelanato bege acinzentado com reflexos suaves. Nada sobre o piso além do guarda-chuva e da água.

Câmera: ponto de vista na altura do peito, levemente de frente, lente de 35 mm, profundidade de campo moderada (guarda-chuva nítido, fundo levemente desfocado), câmera um pouco mais afastada do que numa foto de detalhe, para deixar ar ao redor do sujeito.

Luz e cor: luz natural fria e difusa vinda da porta ao fundo; exposição levemente baixa, em penumbra suave; paleta contida em cinzas, bege frio e preto, sem cores saturadas. A parte superior do quadro (teto e paredes altas) em sombra suave, mais escura que o resto.

Composição: o guarda-chuva inteiro ocupa a faixa do quadro entre 18% e 52% da altura (copa e cabo), centrado, com ar ao redor. A poça e o piso ficam logo abaixo, e a parte inferior do quadro é calma, apenas piso e reflexo suave. Sem detalhes importantes nos 15% superiores nem nos 20% inferiores. Nenhuma área clara e estourada atrás da faixa superior.

Aparência: foto real, com aspecto de câmera de celular de boa qualidade, grão sutil, sem acabamento publicitário, sem aspecto de ilustração ou render.

Não incluir: nenhuma pessoa, mão ou rosto; nenhum texto, letra, número, logotipo, marca ou marca-d'água; nenhuma etiqueta, cartão, nome ou iniciais no guarda-chuva; nenhum segundo objeto além do guarda-chuva e do ambiente descrito.

Gere uma única imagem.
```

Observação: se quiser preservar a foto atual, a alternativa é reduzir e reposicionar o sujeito na arte, o que a skill não faz hoje e que ainda deixaria o problema de resolução. Recomendo a nova geração.

## F. Arquivos da skill v0.1.1 que seriam modificados

Modificar: `SKILL.md` (passos 5 e 7 com os portões das duas etapas); `references/analise_visual.md` (reescrever com o padrão, critérios e lista de defeitos); `references/prompt_fotografico.md` (composição para tipografia, resolução, parâmetros do gerador); `references/versao_limitacoes.md` (nova linha de versão e limitações); `scripts/analisar_foto.py` (resolução, fator de ampliação, compressão, proporção, hash); `scripts/compor_story.py` (medir e registrar contraste e sobreposição; bloqueio por contraste, sem mudar os perfis); `scripts/config.json` (limiares provisórios); `scripts/verificar_skill.py` (novas verificações); `testes/test_piloto.py` (novos testes).

Criar: `references/padrao_excelencia_fotografica.md`; `scripts/registrar_auditoria.py` (registro só de acréscimo); `assets/auditoria_modelo.jsonl`.

Não modificar: referência literal da v2.2, `registro_numeracao.py`, `filtros.py`, `taxonomia.json`, o CSV e suas colunas, qualquer arquivo congelado ou experimental, n8n, grade, fila, contador real.

## G. Limitações e riscos residuais

1. Verificações automáticas garantem números (dimensões, contraste, sobreposição aproximada), não realismo, beleza ou qualidade artística. A skill não deve alegar o contrário.
2. A análise visual é feita por modelo da mesma família que escreve os prompts, pode deixar passar artefatos finos ou apontar defeitos que não existem, e é mais fraca em arquivos pequenos.
3. Os limiares de resolução e contraste são provisórios.
4. O contraste medido ignora peso da fonte, suavização e sombra de texto; a sobreposição usa luminância como aproximação do sujeito, não segmentação.
5. O limite de duas correções pode abandonar uma ideia que mais uma tentativa resolveria; a escolha de continuar é de Eri.
6. Risco de uniformização: prompts parecidos tendem à mesma luz, enquadramento e ambiente. O registro de auditoria deve permitir observar repetição entre edições, sem impor cota agora.
7. Resoluções e custos do Gemini e do Kairogen não foram verificados aqui; podem limitar o cumprimento de I6.
8. Questão aberta para você: a série quer ser percebida como registro real, e as plataformas costumam pedir rotulagem de conteúdo fotorrealista gerado por IA. Não verifiquei a política vigente; vale conferir antes da primeira publicação.

## H. Plano de implementação (v0.2, preservando a v0.1.1)

1. Você aprova ou ajusta a proposta, os limiares provisórios e o limite de duas correções.
2. Criar a v0.2 como pacote novo; manter o ZIP da v0.1.1 e da v0.1 intactos, com hashes.
3. Implementar os itens da seção F, com testes reproduzíveis de cada falha corrigida (incluindo o caso da foto de 572 px e do título com contraste baixo, que a v0.1.1 aprova tecnicamente).
4. Rodar `verificar_skill.py` e os testes, empacotar e entregar com registro de versão.
5. Auditar a nova foto do guarda-chuva e compor no perfil B com LAB-001, calibrando os limiares com dados reais.
6. Só então decidir sobre a retomada do uso manual. Nenhuma publicação, número real, n8n, grade, fila ou serviço pago nesta fase.

Decisões que preciso de você: (a) aprovar o padrão; (b) aprovar ou trocar os limiares provisórios; (c) confirmar o limite de duas correções além da imagem original; (d) autorizar a nova geração do guarda-chuva com o prompt corrigido ou indicar outro caminho.
