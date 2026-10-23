# Plano experimental conceitual, revisão 2

Data: 22/10/2026. Fase A. Documento conceitual para discussão e aprovação de Eri.

Este documento substitui, sem apagar, `plano_experimental_conceitual.md` (versão 1, commit c203047), que permanece como registro. Não há prompts experimentais, não há novos textos, não há execuções, não há v2.4, não há imagens nem créditos visuais. Nada aqui altera rótulos ou registros históricos, a grade das dez janelas, o n8n, a fila, as publicadas ou as skills existentes. Nada é homologado.

Propósito, nas palavras de Eri: consolidar um experimento capaz de produzir evidência confiável, inclusive quando os resultados forem desfavoráveis à hipótese de melhoria, e que mostre com igual clareza quando a versão sob teste melhora, quando permanece igual e quando piora.

## 0. O que mudou em relação à versão 1

| Decisão de Eri (22/10, 23h22) | Onde está tratada |
|---|---|
| 1. Rotulagem independente | seções 2 e 3 |
| 2. Segundo avaliador | seção 3 |
| 3. Fontes dos exemplos | seção 4 |
| 4. Amostra de fluxo e de desafio | seções 5 e 6 |
| 5. Execuções e pareamento | seções 7 e 8 |
| 6. Continuar, superior, homologar | seção 9 |
| 7. Julgador de motivos | seção 10 |
| 8. Controles especiais | seção 11 |
| 9. Fronteiras editoriais | seção 2 e seção 10 |
| 10. Sinais de reconsideração | seção 12 |
| 11. Limites operacionais | seção 1 e seção 14 |
| Condições para autorização futura | seção 13 |

Trocas principais: Eri deixa de ser a rotuladora de todos os itens e passa a arbitrar divergências e uma amostra de controle; a faixa histórica de variação da v2.2 deixa de ser o teste de superioridade; os oito critérios deixam de ser oito condições absolutas e viram dimensões de avaliação; a hipótese deixa de pressupor uma v2.4.

## 1. Hipótese e escopo

Pergunta: o Crítico, aplicando a referência editorial conceitual, reconhece melhor a qualidade, erra menos nos erros graves e decide com maior consistência do que o controle, em exemplos que nenhum Crítico e nenhum redator de Crítico viu?

O plano não pressupõe a criação de uma nova versão. A "versão sob teste" será a que Eri autorizar numa etapa posterior (pode ser a v2.3-exp já existente, uma variante, ou uma versão nova). Os controles são a v2.2 (principal) e, se Eri quiser, a v2.3-exp. Como o experimento também mede quanto do que o processo normal de criação entrega é publicável, ele serve a uma segunda pergunta, que pesa na decisão de estratégia: o problema está no Crítico ou na geração dos candidatos?

Hipóteses (podem falhar separadamente, e cada uma será respondida com melhora, sem diferença distinguível, piora ou inconclusivo):
- H1, aprovações indevidas: menos itens não BOA aprovados, em especial os de premissa sentimental conhecida com gesto concreto.
- H2, mérito: as BOA continuam aprovadas, e pela razão certa.
- H3, fronteiras: separa REVISAR de REPROVADA conforme a possibilidade de correção pontual.
- H4, B contra C: não inventa defeito em BOA nem dispensa falha relevante.
- H5, consistência: decide de forma mais estável entre execuções repetidas.

Correspondência operacional (decisão de 22/10, 23h18): BOA corresponde, em princípio, a APROVADA; AMBÍGUA, a REVISAR; RUIM, a REPROVADA. Não são verdades absolutas, e divergências legítimas e arbitragens ficam identificadas à parte.

## 2. Rotulagem independente e tratamento das divergências

### 2.1 Princípio

Todo item inédito é classificado por dois avaliadores efetivamente independentes antes de qualquer execução de Crítico. O ChatGPT pode ser um deles. Personagens, prompts ou sessões diferentes do mesmo modelo não são avaliadores independentes (uma repetição do mesmo modelo pode, no máximo, medir o ruído do próprio avaliador, e será registrada como tal, nunca como segundo avaliador).

### 2.2 Condições de independência

- Cada avaliador recebe o mesmo pacote cego: foto (conceito), contexto necessário da série, texto, códigos opacos embaralhados.
- Nenhum avaliador vê o rótulo, a justificativa ou a existência do outro antes de entregar o seu.
- Nenhum avaliador vê saída de Crítico.
- Cada avaliador entrega estado (BOA, AMBÍGUA, RUIM), motivo principal em poucas linhas com o tipo de fundamento (A defeito demonstrável, B interpretação fundamentada, C preferência), e, para os não BOA, se há correção pontual possível (descrita em uma frase) ou se exige outra ideia.
- Os rótulos de cada avaliador são lacrados com SHA-256 antes de serem confrontados.
- O uso de modelo externo não pode revelar classificações de outros avaliadores. Quem intermedeia (Eri ou eu) não repassa rótulos entre avaliadores antes do lacre.

### 2.3 Tratamento das divergências

Depois do lacre, cada item cai em uma de três situações:

1. Consenso: os dois concordam no estado. Forma o núcleo de consenso. Uma parte dele recebe controle humano (2.4).
2. Divergência: os estados diferem. Eri examina as duas justificativas e classifica, na ordem:
   - erro de leitura ou erro factual de um dos avaliadores: corrige-se a leitura ou descarta-se a avaliação viciada; o item volta ao consenso ou é excluído, com registro;
   - interpretação incompatível com o texto ou justificativa não demonstrada: descartada, não é impasse editorial;
   - divergência legítima: interpretações razoáveis, argumentadas e materialmente incompatíveis. Material, quando as avaliações discordam sobre publicar como está (APROVADA contra REVISAR ou REPROVADA). REVISAR contra REPROVADA orienta o tratamento editorial, mas não é conflito de elegibilidade.
3. Dúvida de preferência (C) sem defeito: não bloqueia nem aprova sozinha; registra-se como preferência, sem alterar o estado.

Itens em divergência legítima formam a zona contestada. Eles nunca são convertidos em consenso. Eri decide a elegibilidade para publicação, como autoridade editorial, e registra a decisão separada do rótulo original, com data e circunstâncias.

### 2.4 Intervenção humana concentrada

Eri não rotula os cerca de 60 itens automaticamente. Ela atua em:
- todos os itens com divergência (2.3);
- uma amostra de controle dos itens com consenso, sorteada por procedimento fixado e semeado antes da rotulagem, com tamanho definido antes (proposta: cerca de 20% dos itens de consenso, com mínimo de 10). Eri rotula esses itens às cegas, sem ver o rótulo de consenso, e depois confronta.

A amostra de controle serve para detectar consenso espúrio (dois avaliadores errando do mesmo jeito). Se a taxa de discordância de Eri com o consenso for alta, o núcleo de consenso perde valor probatório e o relatório diz isso.

### 2.5 Ficha de referência por item (campos)

Estado final e sua origem (consenso, consenso confirmado por Eri, decisão de Eri em divergência); condição (consenso, divergência legítima material, divergência legítima não material, erro de leitura corrigido); natureza editorial (ver 2.6); correção pontual possível ou exige outra ideia; motivo principal e tipo de fundamento; procedência e processo de criação; indicação de contaminação.

### 2.6 Natureza editorial, conforme a decisão 9

Cada item não BOA recebe uma natureza, para que o experimento distinga:
- ausência de mérito (sem segunda leitura, sem núcleo promissor);
- mérito promissor com correção pontual possível (núcleo preservável, deficiência nomeada, intervenção localizada);
- insuficiência estrutural (corrigir exigiria reconstruir a ideia; fundamento A, ou B com argumento específico, confronto com a leitura mais favorável e demonstração de que atinge o núcleo);
- divergência editorial legítima (condição que pode acompanhar qualquer estado).

Nos itens contestados, o Crítico não é medido por concordar com um avaliador. Mede-se três coisas, definidas antes: se oferece uma interpretação defensável (coerente com o texto e com um dos fundamentos documentados ou outro igualmente defensável); se identifica corretamente a natureza do fundamento (A, B ou C); se reconhece a dúvida material quando ela existe.

## 3. Disponibilidade real de um segundo avaliador

### 3.1 O que foi efetivamente verificado

Em 22/10/2026, antes de redigir esta seção, verifiquei no ambiente de execução desta sessão, em modo somente leitura (apenas nomes de variáveis de ambiente, existência de comandos e pacotes instalados; nenhum serviço foi chamado, nenhuma conta conectada, nenhum recurso pago usado):
- as únicas credenciais de modelo presentes apontam para o endpoint do próprio Claude; não há chave, comando nem pacote de outro provedor de modelos (OpenAI, Google, Mistral, outros) instalado ou configurado;
- as ferramentas desta sessão incluem conectores de e-mail, armazenamento, métricas e navegação, e uma plataforma de geração de imagem, vídeo e áudio (Kairogen) que consome créditos pagos. Ela não é um avaliador de texto e não foi chamada;
- navegadores controláveis existem como ferramenta, mas dependem de contas e sessões de Eri em outras famílias de modelos que eu não verifiquei e não tentei acessar. Não usarei sem autorização expressa dela, e o uso não poderia expor rótulos de outros avaliadores.

Conclusão verificada: dentro do ambiente do projeto não há segundo avaliador de outra família de modelos disponível. Há três recursos reais: o ChatGPT, que Eri opera manualmente; a própria Eri; e subagentes Claude, que pertencem à mesma família do Crítico e do redator dos textos e, portanto, não contam como avaliadores independentes. Eventual acesso de Eri a Gemini ou outro serviço, por conta própria, não está verificado: é uma informação que só ela pode dar.

### 3.2 Alternativas, para Eri escolher antes de iniciar

- Alternativa 1 (preferida, se viável): Eri obtém, por seus próprios meios e sem custo para o projeto, um segundo avaliador de outra família, que recebe o mesmo pacote cego e entrega rótulos lacrados. Eri informa o que realmente tem; nada é presumido.
- Alternativa 2 (padrão, se a 1 não existir): ChatGPT rotula todos os itens como avaliador externo. Eri é a segunda referência independente, mas apenas num subconjunto: (a) itens em que o rótulo do ChatGPT contraria uma predição cega prévia de subagentes Claude (triagem, usada só para decidir onde gastar atenção humana, jamais como rótulo, e registrada como não independente); (b) a amostra de controle de consenso da seção 2.4, que pega os casos em que ChatGPT e a triagem erram juntos. Limitação registrada: um único avaliador externo, de uma família só, mais uma segunda referência parcial.
- Alternativa 3 (mínima): apenas itens com dois rótulos independentes entram no núcleo de consenso; os demais são descritos, sem entrar em conclusões. Reduz o poder, mantém a honestidade.

### 3.3 Consequência para as conclusões

Com a Alternativa 2 ou 3, o núcleo de consenso é mais fraco e o resultado fica limitado à decisão A (continuar investigando) e, no máximo, a uma indicação provisória para B, declarada como provisória no relatório. Nenhuma das alternativas viabiliza a decisão C. A limitação é registrada antes do início, não depois dos resultados.

## 4. Fontes dos exemplos

Fontes candidatas, cada uma com sua independência registrada no mapa privado de procedência:
- A. Textos inéditos do Criador do projeto (Claude, processo normal de criação). Independência de procedência baixa em relação ao Crítico (mesma família), e isso é declarado.
- B. Textos de outra família de modelos, quando disponível. Mesma observação da seção 3: só entra se Eri conseguir obter e se o acesso for real.
- C. Textos de criação humana, quando fornecidos por Eri.
- D. Edições anteriores da série: apenas referência ou material de desenvolvimento, nunca novos casos independentes se já conhecidas pelo Crítico.
- E. Processos distintos do Claude, com independência limitada e expressamente registrada.

Regras: prompts de geração diferentes não conferem independência; procedência, processo de criação e qualidade editorial são três campos distintos e separados; W01 a W30, W05, W15 e W19 e todo item já visto por qualquer Crítico ou avaliador estão fora (queimados ou contaminados). Se só existir a fonte A, o relatório dirá que a independência de procedência é limitada e que isso restringe a generalização.

## 5. Amostra de fluxo e amostra de desafio

Meta inicial de cerca de 60 itens no total, declarada como insuficiente para conclusão científica definitiva. Proposta de partida, não vinculante: cerca de 30 de fluxo e cerca de 30 de desafio. Duas amostras analíticas, com resultados sempre reportados separadamente. Não existe um percentual único combinando as duas como "desempenho geral".

### 5.1 Amostra de fluxo

Objetivo: estimar o comportamento no processo normal de criação.
Seleção, definida antes da geração:
- uma lista de conceitos de foto fixada antes (por sorteio com semente registrada, ou lista que Eri aprovar), sem relação com a qualidade dos candidatos, sem tocar a fila nem a grade;
- todo candidato que o processo normal entregaria para cada conceito entra, na ordem de produção, até completar o tamanho fixado;
- nenhuma triagem por rótulo, por resultado de Crítico ou por impressão de qualidade;
- as proporções de BOA, AMBÍGUA e RUIM saem como saírem. Se saírem poucas RUIM ou poucas BOA, é o fato que o experimento mede, e o relatório diz que os estratos pequenos não sustentam conclusão.
Leitura: com n pequeno, usar contagens com intervalo, não só percentual. Exemplo de ordem de grandeza: zero aprovações indevidas em 30 itens é compatível com uma taxa verdadeira de até cerca de 10% (regra dos três, limite superior aproximado de 95%). Zero observado não é ausência de risco.
Produto adicional: a proporção de itens publicáveis no fluxo, que informa a decisão de estratégia (seção 12).

### 5.2 Amostra de desafio

Objetivo: testar casos difíceis de propósito.
Células declaradas antes da geração, com o que se pretende (intenção de projeto) e sem prometer o que sairá:
- sentimentalismo implícito (premissa de ausência e objeto, bem escrita, sem metáfora explícita);
- ausência de segunda leitura (texto que apenas complementa a foto);
- correções pontuais (núcleo promissor com falha localizada);
- divergências editoriais legítimas (casos em que avaliadores razoáveis discordam);
- os controles especiais da seção 11, em células próprias.
Regras:
- a classe real de cada item é a que os avaliadores e Eri atribuírem, não a intenção de projeto. Um item que não saiu como pretendido permanece na amostra sob a classe real, não é descartado nem escondido;
- não haverá rodadas extras de geração para preencher células depois de conhecer rótulos, salvo uma segunda rodada pré-registrada, com as mesmas regras e declarada no relatório com o número de rodadas;
- células que ficarem pequenas são descritas, não usadas como prova;
- nada da amostra de desafio é apresentado como representativo do fluxo.

## 6. Critérios de inclusão definidos previamente

Antes da geração, lacrar por hash uma lista contendo:

Inclusão (todos obrigatórios):
1. Formato completo da série (foto, NA FOTO, FORA DO ENQUADRAMENTO) e dentro dos limites de tamanho da série.
2. Procedência, processo de criação e data registrados no mapa privado.
3. Nunca visto por Crítico, avaliador ou redator de Crítico; não derivado de W01 a W30 nem das edições usadas no desenvolvimento.
4. Conceito de foto sem repetição em relação a outros itens do conjunto.
5. Produzido e congelado (hash) antes de qualquer rótulo.

Exclusão: apenas por razões técnicas listadas antes (formato inválido, duplicata, conhecimento prévio comprovado, violação de segurança do conteúdo). Exclusão por qualidade, por rótulo ou por resultado de Crítico é proibida.

Registro de excluídos: cada exclusão entra num log com item, motivo da lista, quem decidiu e quando, antes de qualquer rótulo. O relatório final informa quantos candidatos foram produzidos, quantos entraram e quantos saíram, por motivo. Não se completa categoria artificialmente para depois apresentar o resultado como amostra representativa.

## 7. Execuções e condições

- Mínimo de três execuções independentes por versão, tratado como mínimo de um experimento exploratório, não como prova de estabilidade.
- Todas as execuções são registradas e entram na análise. Sem melhor resultado, sem exclusão posterior. Falha técnica pode ser reexecutada uma vez, com o mesmo prompt, com o motivo registrado.
- Condições equivalentes para a versão sob teste e para os controles: mesmos itens, mesmo pacote, mesmo contexto fornecido, mesmo modelo e configuração, códigos opacos e ordem embaralhados de forma independente por execução, contextos isolados, prompts travados por hash, execuções do controle feitas junto com as da versão candidata e não reaproveitadas de experimentos anteriores (outro conjunto, outra época).
- Variação superficial e controles especiais seguem as mesmas condições.

## 8. Comparação pareada entre versões

A unidade de análise é o item. Como a mesma coleção de itens passa pelas duas versões, a comparação é pareada: cada item tem o resultado da versão sob teste e o do controle, execução por execução.

- Tabela por item e por execução: estado de referência, veredicto do controle, veredicto da versão candidata, concordância com a referência, motivo.
- Classificação de cada item e execução em: melhorou, igual, piorou, definida pelo veredicto em relação ao estado de referência e ordenada pela gravidade (8.1).
- Padrão por item entre as três execuções (3 de 3, 2 de 3 etc.), preservado. Não se transforma o padrão em uma decisão de maioria como se fosse a decisão do Crítico: em operação autônoma cada execução decide sozinha, então um erro grave em qualquer execução conta como evento.
- Execuções não são amostras independentes de itens. Três execuções de 30 itens não são 90 itens. O n efetivo para itens é 30.
- Pode-se usar testes pareados exatos como auxílio descritivo, com a ressalva de que o tamanho não sustenta inferência forte.
- A faixa histórica de variação da v2.2 (RUIM aprovadas de 6 para 2 entre execuções) é contexto, nunca o teste de superioridade. O ruído relevante é o observado neste experimento, por item e entre execuções repetidas.

### 8.1 Gravidade, fixada antes

Camadas sempre reportadas separadamente, sem índice global que as misture:
1. Aprovar item de consenso RUIM (o erro mais grave).
2. Aprovar item de consenso AMBÍGUA, ou item contestado sem reconhecer a contestação.
3. Reprovar item de consenso BOA, ou inventar defeito em BOA.
4. Confundir REVISAR e REPROVADA.
5. Veredicto correto com motivo errado (seção 10).

## 9. Continuar, demonstrar superioridade, homologar

Os oito critérios de continuidade da versão 1 permanecem como dimensões de avaliação, não como oito condições absolutas. Cada dimensão recebe o resultado melhora, sem diferença distinguível, piora ou inconclusivo, sempre com os itens que sustentam a leitura.

Dimensões: (1) aprovações indevidas de RUIM, (2) aprovações indevidas de AMBÍGUA e contestados, (3) retenção das BOA e defeitos inventados, (4) trocas entre aprovar e não aprovar entre execuções, (5) acerto pelo motivo certo, (6) controles de vocabulário e de variação superficial, (7) estrato sentimental com gesto concreto, (8) ausência de piora onde o controle já acertava.

### 9.A Continuar investigando

Pode ser justificável com evidência parcial, mecanismos de erro compreendidos e hipótese plausível de melhoria. Exemplo: melhora em algumas dimensões, estado inconclusivo em outras, e um diagnóstico por item que explique por que os erros restantes acontecem. Não exige superioridade, e a falha isolada em uma dimensão não encerra a pesquisa. Aprovação indevida de RUIM continua sendo uma meta importante de segurança, mas não o critério único.

### 9.B Considerar a nova abordagem superior

Exige, ao mesmo tempo:
- melhora relevante, consistente e fundamentada sobre o controle, vista no pareamento por item e nas três execuções, nas duas amostras reportadas separadamente;
- ausência de perdas editoriais graves (camadas 1 e 3 da gravidade não pioram);
- controles especiais sem queda;
- avaliação dos motivos conclusiva (seção 10).
Limiares numéricos serão fixados por Eri antes da geração, no protocolo de análise lacrado. Os números da versão 1 (por exemplo, 90% das BOA) ficam apenas como ponto de partida de discussão. Se a evidência de rótulo for a das Alternativas 2 ou 3 da seção 3, a conclusão B sai marcada como provisória.

### 9.C Homologar para publicação autônoma

Exige um padrão substancialmente mais alto de segurança editorial, estabilidade e validação. Este experimento, isoladamente, não pode homologar. Um passo C pediria, no mínimo, um conjunto de validação novo e maior, mais execuções e em momentos distintos, avaliadores independentes de verdade, análise de gravidade sem erros graves, tratamento definido para itens retidos sem tocar as dez janelas, e decisão expressa de Eri. Nada disso está neste plano.

### 9.D Piora e resultado inconclusivo

O plano declara com a mesma clareza o que conta como piora (por exemplo, mais itens de camada 1 ou 3 aprovados ou reprovados indevidamente, nas execuções e no pareamento) e como igual (mudanças dentro do ruído observado, por item). Quando o método falha (julgador de motivos sem contexto, pacote incompleto, rótulos comprometidos), o resultado é inconclusivo e não evidência de qualidade.

## 10. Julgador de motivos

- Um acerto de veredicto com justificativa errada não é acerto editorial pleno.
- O julgador recebe o contexto necessário completo: conceito da foto, textos anteriores relevantes da série, texto integral do item, saída integral do Crítico, ficha de referência do item (motivo, tipo de fundamento, natureza) e, para os contestados, os fundamentos concorrentes.
- Procedimento definido antes e lacrado: para cada item, (i) verificar se as afirmações factuais do Crítico se sustentam no texto e no contexto, sem olhar o rótulo; (ii) comparar o motivo com o da referência e classificar como motivo correto, parcialmente correto, errado ou não avaliável; (iii) nos contestados, aplicar as três perguntas da seção 2.6.
- Porta de completude: antes de julgar, uma checagem objetiva de que cada elemento exigido do pacote está presente. Pacote incompleto torna a avaliação do item inconclusiva. Se a parcela de itens inconclusivos passar de um limite fixado antes (proposta: acima de 15%), a dimensão dos motivos inteira fica inconclusiva.
- O julgador não sabe qual versão produziu cada saída, e a ordem é embaralhada.
- Uma amostra das avaliações do julgador, definida antes, é conferida por Eri.
- Limitação registrada: o julgador também é um modelo, da mesma família do Crítico, a menos que a Alternativa 1 da seção 3 inclua outra família para esse papel.
- O defeito do julgador anterior (pacote sem foto e sem textos anteriores, 16 sinalizações inválidas) é a razão do desenho acima: aquele resultado continua tratado como não confiável, e não é reexecutado.

## 11. Controles especiais (desenho conceitual, sem criar textos)

Cada controle tem estado esperado como hipótese de projeto. Os rótulos independentes decidem o estado real; se os avaliadores discordarem da intenção, o item é registrado sob a classe real, sem ser forçado.

1. Tecnicamente correto, editorialmente vazio. Sem defeito A ou B, mas sem segunda leitura: o texto só complementa a foto. Testa a distinção entre integridade narrativa e mérito. Esperado: não APROVADA. Aprovação aqui é a falha mais direta do conceito.
2. Mérito positivo com imperfeição periférica. Segunda leitura genuína, ligada à foto, com um senão que não atinge o núcleo (por exemplo uma imprecisão de classe B periférica ou uma dúvida C). Testa o excesso de zelo. Esperado: APROVADA, com o senão registrado como periférico.
3. Pares de variação superficial. Duas versões do mesmo item mudando só a forma (ordem de frases, sinônimos, pontuação) sem alterar a qualidade. Esperado: o mesmo veredicto e o mesmo motivo nos dois. A análise é por par; os pares ficam fora dos totais das duas amostras.
4. Texto fraco com o vocabulário da referência. Aparência de "gesto concreto" e "segunda leitura" sem contribuição real. Esperado: não APROVADA. Se o Crítico aprovar por reconhecer a forma, é o sinal de que aprendeu palavras.
5. Texto forte sem o vocabulário da referência. Segunda leitura obtida por outro caminho que não o gesto concreto explícito. Esperado: APROVADA. Se reprovar por ausência do formato, é o sinal inverso.

Observação sobre os controles 1, 4 e 5: o Crítico pode usar o vocabulário da referência nas justificativas; isso não é evidência de qualidade. O que conta é o veredicto e o motivo verificado.

### 11.1 Preservar um conjunto verdadeiramente inédito

A produção posterior se divide em dois lotes disjuntos:
- lote de desenvolvimento: pode ser visto, usado para ensaiar os instrumentos (pacotes, procedimento do julgador, protocolo de lacre) e fica queimado para ajuste;
- lote de validação: produzido depois que a versão sob teste e o protocolo de análise estiverem travados por hash, nunca visto por quem redige o Crítico ou o julgador, usado uma vez.
Se a versão for alterada depois de ver resultados do lote de validação, esse lote fica queimado e o novo teste exige outro. A produção dos controles não usa o texto da versão sob teste no contexto do gerador.

## 12. Sinais de reconsideração (alertas diagnósticos)

Os sete sinais permanecem, reformulados:
1. A melhoria fica dentro do ruído observado no pareamento (entre execuções e por item), não apenas dentro da faixa histórica da v2.2.
2. Aprovações indevidas persistem no estrato sentimental, mesmo com a referência aplicada.
3. As trocas entre aprovar e não aprovar continuam tão frequentes quanto antes.
4. A maioria dos acertos vem pelo motivo errado, ou com justificativas fluentes que a referência desmente.
5. A melhora some nos controles de vocabulário ou de variação superficial.
6. O Crítico acompanha um avaliador específico sem separar consenso de zona contestada, ou não reconhece contestabilidade.
7. Itens limpos e vazios são aprovados (mérito não distinguido de integridade).

Alertas, não gatilhos. Nenhum deles dispara automaticamente v2.4, novos agentes ou outra camada de regras. Cada alerta exige um diagnóstico escrito e uma decisão de Eri. Se a melhoria ficar dentro do ruído, se o sentimentalismo continuar passando ou se o mérito continuar mal demonstrado, o plano manda considerar seriamente mudar a estratégia, inclusive a geração dos candidatos (a amostra de fluxo informa quanto do que o processo normal entrega é publicável), em vez de continuar sofisticando o Crítico. As alternativas já mapeadas no diagnóstico seguem como opções: reduzir a ambição do Crítico, outra família de modelos como juiz, atacar a geração.

## 13. Condições para uma futura autorização de geração e teste

Nada é gerado ou executado enquanto estas condições não estiverem cumpridas e Eri não autorizar por escrito, em etapas separadas, sem progressão automática:

Etapa G1, geração de itens (sem execução de Crítico):
1. Alternativa de rotulagem escolhida (seção 3) e limitação registrada.
2. Tamanho e divisão entre fluxo e desafio fixados; lista de conceitos de foto aprovada.
3. Regras de seleção, inclusão, exclusão e log de excluídos lacradas por hash.
4. Células da amostra de desafio e desenho dos controles aprovados.
5. Separação entre lote de desenvolvimento e lote de validação definida.
6. Recursos: confirmação de que não haverá gasto pago, conexão de conta nem crédito visual sem autorização expressa.

Etapa G2, rotulagem:
7. Pacotes cegos e protocolo de lacre aprovados; avaliadores confirmados (os realmente disponíveis).
8. Regra do triador de divergências (Eri) e da amostra de controle (tamanho, semente) fixadas.

Etapa G3, execuções:
9. Versão sob teste e controles travados por hash.
10. Protocolo de análise lacrado antes de qualquer execução: dimensões, tabela pareada, gravidade, definição de melhora, igual, piora e inconclusivo, limiares de Eri para B.
11. Procedimento e porta de completude do julgador de motivos aprovados.
12. Número de execuções e condições equivalentes fixados; regra de reexecução técnica.
13. Declaração de que nenhum prompt, rótulo ou conjunto é ajustado depois de ver resultados.

Em todas as etapas permanecem intocáveis as dez janelas editoriais (início às 06h00, intervalo fixo de 1h30), a grade, o n8n, a fila, as publicadas e as skills existentes. Nenhuma publicação é ativada. Nenhuma versão é homologada por este experimento.

## 14. Limitações do plano

- Redigido pelo mesmo modelo que gerou itens e Críticos; as fontes de textos independentes são limitadas (a fonte A domina, salvo contribuição de Eri ou de outra família).
- Com a Alternativa 2 ou 3 da seção 3 há um único avaliador externo, de uma família só; o núcleo de consenso é mais fraco.
- Cerca de 60 itens, divididos em duas amostras, dão pouco poder para estratos pequenos e não bastam para conclusão científica definitiva.
- Três execuções estimam mal a variação e não demonstram estabilidade definitiva. Erros sistemáticos do modelo se repetem em todas as execuções: consistência não é correção. Contextos isolados reduzem, mas não eliminam, a correlação entre execuções do mesmo modelo.
- O julgador de motivos é um modelo, e a avaliação dos motivos pode resultar inconclusiva.
- Eri conhece os resultados das avaliações anteriores; para os itens novos será cega se o protocolo for seguido.
- Os números citados (30 e 30, 20%, 15%, 10 itens) são propostas de partida para a decisão de Eri, não limiares.

## 15. Decisões que preciso de Eri antes de qualquer etapa

1. Qual alternativa de rotulagem da seção 3: você tem, de fato, acesso a um segundo avaliador de outra família, ou seguimos com a Alternativa 2?
2. Divisão inicial entre fluxo e desafio (proposta 30 e 30) e tamanho da amostra de controle de consenso (proposta 20%, mínimo de 10).
3. Se a v2.3-exp entra como controle secundário.
4. Se a ordem de gravidade da seção 8.1 está correta.
5. Se a porta de completude do julgador (limite de 15%) e a conferência por amostra sua estão adequadas.

Sem pedir nenhuma execução agora: continuamos na Fase A, e exigentes, mas metodologicamente justos.
