# Auditoria final do piloto: O QUE NINGUÉM LEGENDA

Data: 29/10/2026. Auditor: Claude, a partir do repositório (branch main, commit 1d4bcd7 no último registro da pasta ninguem-legenda) e dos arquivos originais. Nada foi alterado, executado, publicado ou homologado nesta auditoria. Nenhum experimento novo foi feito. n8n, grade, fila, contador real, prompts congelados, lacres e as 72 avaliações não foram tocados (a única escrita temporária, o arquivo verificacao_c1b/verificacao_pre.json produzido pelo conferidor, foi revertida com git checkout; o repositório ficou limpo).

Limite do material recebido: o arquivo do pedido termina em "QUESTÃO 3:", cortado. Respondi às seções 1 a 9 e às questões 1 e 2. A questão 3 e as seguintes precisam ser reenviadas.

---

## 0. Conclusão curta

1. **A skill v0.1.1 é a versão documentada e utilizável**, para piloto manual supervisionado. Está íntegra (ZIP idêntico à fonte, 23 testes passam, conferidor da skill sem falhas). Não há nada além dela: a v0.2 (padrão fotográfico, layout decidido por Eri nesta semana) existe só como proposta.
2. **Nada no projeto está homologado.** O que existe é: autorizações de Eri para uso manual, decisões editoriais suas (algumas lacradas), referências provisórias (Crítico v2.2, perfil B de layout, limiares fotográficos) e propostas (núcleo de identidade, C1b, padrão de excelência fotográfica, contador com livro-razão).
3. **Existe impedimento claro à homologação do Crítico e da autonomia:** o único teste comparável (G3, 240 avaliações) mostrou a v2.2 aprovando 8 dos 11 itens RUIM e 12 a 13 dos 16 AMBÍGUA do rótulo externo; depois a sua arbitragem mudou boa parte desse quadro, mas a falha em itens AMBÍGUA permanece nas duas referências. A verificação que poderia testar a C1b está suspensa e não pode ser retomada sem decisão sua, por causa da possível contaminação de L8CFD e de a sua classificação cega das 12 histórias ainda não existir.
4. **Não é preciso nenhuma rodada nova para encerrar a fase de desenvolvimento do piloto manual.** Faltam decisões suas (seção 10), o fechamento visual do LAB-001 e, se você quiser, a implementação versionada da v0.2.

---

## 1. Método e fontes lidas

Li no repositório: README da pasta, Emenda 2 e seu lacre, registro de circunstância de L8CFD, protocolo da C1b, entregas pós-G3 (três), núcleo de identidade proposto, relatório da G1, registros e lacres da G2 (segunda leitura não independente), relatório da G3 reduzida, relatório da arbitragem, relatório de validação da v2.2, os arquivos da skill v0.1.1 (SKILL.md, referências, config, scripts, testes), a proposta do padrão fotográfico e as auditorias do LAB-001. Executei apenas conferências somente leitura: `verificar_skill.py`, `testes/test_piloto.py`, comparação do ZIP com a fonte e `verificar_c1b.py`.

Resultados das conferências:

| Conferência | Resultado |
|---|---|
| `verificar_skill.py` | skill íntegra |
| `testes/test_piloto.py` | 23 testes, OK |
| ZIP v0.1.1 contra a fonte | idêntico; SHA-256 do ZIP 7791524d...e6a6a, igual ao REGISTRO_VERSAO_v0.1.1.json |
| `verificar_c1b.py` | lacre da Emenda 2: 14 arquivos, 0 divergências; arquivos do M1: 22, 0 divergências; itens da G1: 65, 0 divergências; v2.2 igual ao M1; validador igual; C1b difere da v2.2 apenas nos blocos declarados (3 trechos). Execuções de Crítico: 0 arquivos; pacotes: 0; lacrado: 0; privado: 3; produção: 20 |
| Sinalização "falhas" do conferidor | 2 avisos esperados: pastas privado e producao não estão vazias, porque o conferidor roda em modo "pré" e a produção já ocorreu; não indicam adulteração |

Limite da própria conferência: ela prova que arquivos lacrados não mudaram desde o lacre. Não prova que o conteúdo dos lacres é válido, nem que o isolamento entre agentes foi real (ele é documental).

---

## 2. Estado exato do projeto

| Bloco | O que o repositório mostra | Estado |
|---|---|---|
| G1 | 60 candidatos (30 de fluxo, 30 de desafio) gerados por 60 agentes Criadores; 5 exclusões técnicas por duplicata de conceito, com substituição; um filtro lexical falhou em G1-F08 e foi mantido por decisão registrada | Concluída e congelada |
| Rótulos externos dos 60 | 5 BOA em 24 inéditas na validação da v2.2; nos 60 da G1, rótulos externos lacrados (fad0b7f). Autor: ChatGPT, com Eri como responsável | Lacrados; referência única, não independente |
| G2 | 27 itens (tensões mais controle) no pacote humano H; Eri recebeu a segunda leitura, feita pelo MESMO ChatGPT que produziu os 60 rótulos externos | **NÃO é avaliação humana independente.** O próprio registro diz: "o requisito de auditoria humana independente permanece PENDENTE" |
| G3 reduzida | 8 partes, 240 avaliações, v2.2 contra v2.4-exp, Emenda 1 pré-registrada, saídas lacradas antes de abrir rótulos | Concluída. Superioridade da v2.4-exp NÃO demonstrada. v2.2 mantida como referência provisória |
| Arbitragem pós-G3 | 6 itens decididos por Eri: 3 BOA (D31, F26, D15) e 3 AMBÍGUA (D04, F22, D32), 0 RUIM. Decisões lacradas antes de abrir o mapa | Lacrada. Declarada pela própria Eri como NÃO independente (análise feita em conversa com o ChatGPT) |
| C1b | Candidata a partir da v2.2 com três inserções (E1 e E5 corrigidas após devolutiva, mais salvaguarda interpretativa); congelada por hash na Emenda 2 | Congelada. Não é versão operacional |
| Emenda 2 | Verificação limitada: 12 histórias inéditas mais 6 arbitradas, v2.2 contra C1b, 2 execuções cada, 18 x 2 x 2 = 72 avaliações. Publicada e verificada mecanicamente antes da produção | Publicada. Não homologa nada |
| Produção das 12 | 12 histórias produzidas e lacradas (5 grupos: N, D, M, A, P); filtros determinísticos 12 de 12 passaram; 3 previsões cegas por item, lacradas | Concluída |
| Classificação cega de Eri sobre as 12 | Não há registro nem lacre no repositório. Existe só o pacote para ela (`lote_cego_12.md`) | **Pendente** |
| As 72 avaliações | Nenhuma execução de Crítico existe (0 arquivos em execuções, pacotes e lacrado) | **Suspensas** e não executadas |
| L8CFD | Uma das 12 foi usada como primeira história do piloto, avaliada por Eri fora do procedimento cego ("BOA, FUNCIONAL", provisória), com prompt e composição feitos a partir dela | Registro de circunstância publicado: possível contaminação da referência cega. Qualquer mudança na participação de L8CFD é desvio metodológico que só ocorre por sua autorização expressa |
| Skill v0.1 e v0.1.1 | v0.1.1 de 23/10 aceita por Eri para piloto manual supervisionado; v0.1 preservada | v0.1.1 vigente |
| Padrão de Excelência Fotográfica | Proposta A a H publicada; não aprovada; não incorporada à skill | Proposta |
| Piloto visual LAB-001 | 10 versões de foto (v1 do Gemini; v2 a v10 do ChatGPT) e composições simuladas. v10 tratada (brilho do piso) é a base proposta; layout de teste B215 | Aprovação visual da arte: **pendente de Eri**. Aprovação editorial da foto: não existe |

Duas imprecisões do resumo recebido, para correção do histórico: (1) os "27 itens encaminhados para avaliação humana independente" não receberam avaliação humana independente; receberam uma segunda leitura não independente. (2) O texto "Emenda 2 não homologada definitivamente" é correto, mas a Emenda 2 nunca foi desenhada para homologar: é um protocolo de verificação limitada, sem desfecho que promova a C1b automaticamente.

---

## 3. Auditoria do conceito NA FOTO / FORA DO ENQUADRAMENTO

Pergunta de fundo: o mecanismo sustenta uma série autoral? A evidência do repositório diz o seguinte, sem pretender decidir por você.

**O que os dados permitem afirmar.** O mecanismo produz, sob o Criador atual, uma proporção grande de histórias que você aceita como BOA (nos 60 itens da G1, o rótulo externo deu cerca de metade BOA). O mecanismo não é, portanto, vazio. Mas os 60 itens foram gerados dentro do mesmo desenho que os avalia, e a diversidade medida (conceitos fotográficos sorteados no fluxo) é de assunto visual, não de mecanismo narrativo.

**O que os dados não permitem afirmar.** Que a série seja sustentável por muitas edições sem repetir o truque (risco C). Não há teste de longo prazo, só a janela de repetição do config (5 edições para mecanismo, 30 para emoção e abertura) e o filtro de similaridade, que são controles estatísticos de superfície.

**Critérios objetivos de aprovação e rejeição** (proponho esta redação por critério; hoje estão espalhados entre o núcleo proposto, o Crítico v2.2 e a skill):

| Critério | Aprova quando | Rejeita ou devolve quando |
|---|---|---|
| A. Necessidade da revelação | O FORA muda o que o leitor entende da foto e o elemento da cena que sustenta a mudança é apontável | O FORA só acrescenta um detalhe curioso e a foto poderia ser trocada por outra sem perda |
| B. Plausibilidade | O acontecimento é humanamente comum, sem coincidência que o texto precise justificar | Depende de coincidência artificial ou de uma explicação que o texto não dá |
| C. Originalidade | O mecanismo e a emoção não repetem as últimas edições (janelas do config) e o gesto central é novo na série | Repete o mesmo truque (por exemplo, a inversão do NA FOTO por uma ausência) em edições seguidas |
| D. Autossuficiência | Funciona sem legenda externa, sem continuação e sem conhecimento prévio de série | Exige explicação de fora ou outra edição para fazer sentido |
| E. Precisão | Afirma só fatos observáveis dentro da ficção; motivação e emoção ficam implícitas | Afirma pensamento ou sentimento de alguém sem sustentação, ou psicologiza |
| F. Força editorial | Há uma ideia demonstrada, não só uma frase bem torneada | Depende exclusivamente de efeito de frase ou de moral explícita |
| G. Diferenciação | Ver abaixo | Poderia ser publicada, sem mudança, em outra série irmã |

**Diferenciação em relação a Cena Cortada, Nota Fiscal Emocional e Palavra em Julgamento (G).** Não consegui auditar este ponto contra fontes: o repositório não contém a definição de nenhuma dessas séries (busca por nome nos arquivos .md, .json e .py: zero ocorrências fora desta auditoria). Posso apenas propor o critério de separação, e não o confirmo como fato: O QUE NINGUÉM LEGENDA depende de uma FOTO específica cuja leitura é reorganizada por um FORA; se o texto funcionasse sem a foto (como uma cena breve, uma nota ou uma palavra), pertence a outra série. Para fechar G, preciso dos documentos das três séries.

**Conclusão sobre o conceito.** Mecanismo defensável e distinto, sem prova de sustentabilidade. A decisão de que ele é uma série autoral continua sendo editorial e sua. O que a auditoria exige é registrar, como já registrado no núcleo proposto, que o estoque encolhe em vez de forçar publicação fraca.

---

## 4. Auditoria do Crítico editorial

**O que foi efetivamente testado**
- v2.1 (controle) e v2.2: validação independente de 24 itens inéditos, com rótulos externos fixados antes (5 BOA, 8 AMBÍGUA, 11 RUIM); v2.2 em duas execuções, v2.1 em uma. Zero falsa aprovação de RUIM e zero falsa reprovação de BOA nas duas versões; a v2.2 recuperou BOA aprovadas (3 e 5 de 5, contra 1 da v2.1) à custa de aprovar mais AMBÍGUA (4 e 5, contra 3) e de ficar menos estável (7 e 10 aprovadas entre as duas execuções).
- v2.2 contra v2.4-exp na G3 reduzida: 240 avaliações. A v2.4-exp corrigiu alguns erros, perdeu BOA, criou erros novos e foi menos consistente (divergiu em 11 itens entre execuções, contra 5 da v2.2). Superioridade não demonstrada.

**O que foi apenas proposto:** v2.3 e v2.4 (experimentais, não promovidas), C1 (preservada como histórico, nunca executada), C1b (congelada, não executada), gate 3 sobre a v2.2, Auditor Lógico v1 (somente testes).

**Lacradas e pendentes.** Lacradas: rótulos externos, triagens, marcação de previsibilidade, cruzamento, decisões da arbitragem, saídas brutas da G3, pedidos e saídas de produção das 12. Pendentes: sua classificação cega das 12 inéditas, as 72 avaliações, a segunda etapa (papel dos números nas seis conhecidas) e a decisão sobre o resultado.

**Houve melhoria entre versões?** Parcialmente e com custo. v2.1 para v2.2: menos revisões desnecessárias de BOA, mais aprovações de AMBÍGUA. v2.2 para v2.4-exp: nada demonstrado. Menos aprovações, sozinho, não é melhoria editorial (princípio já escrito na Emenda 2).

**Riscos de vazamento entre geração e julgamento (todos reais, nenhum eliminável sem avaliador humano independente):**
1. O mesmo modelo (claude-sonnet-5-5, registrado nos agentes) gera as histórias, prevê e julga. O isolamento entre agentes é documental, não técnico (mesmo sistema de arquivos).
2. As referências de rótulo (60 externos e os 24 da validação da v2.2) vêm do ChatGPT, e suas decisões de arbitragem e a segunda leitura da G2 passaram por conversa com o mesmo ChatGPT. Concordância entre modelos não é validação independente.
3. Os 60 itens da G1 estão contaminados por leituras diagnósticas minhas (pós-G3) e não valem mais como validação inédita de versões ajustadas com base neles.
4. L8CFD: possível contaminação da referência cega do lote das 12.
5. As seis histórias arbitradas são conhecidas por todos e entram como regressão, não como teste inédito.

**Alteração de critérios durante os experimentos?** Os registros mostram mudanças documentadas e anteriores às execuções: o pacote de triagem da G2 foi reprovado por você antes de uso e substituído; a C1 virou C1b após a devolutiva técnica e antes de qualquer execução; as decisões de 22 e 23/10 foram incorporadas por revisões da G0. Não encontrei alteração de critério depois de abrir resultados. A regra da verificação da C1b foi fixada antes de executar, e a produção das 12 foi lacrada antes de qualquer Crítico.

**A amostra sustenta as conclusões?** Para as conclusões que o relatório da G3 apresenta (superioridade não demonstrada, gate insuficiente, autonomia não demonstrada), sim, com cautela: só 11 itens RUIM, cada um vale cerca de 9 pontos percentuais; todos os RUIM estavam em itens de tensão, então não há taxa válida de RUIM fora das tensões; as quatro avaliações por item repetem os mesmos 60 textos e as mesmas previsões, não são amostras independentes. Para uma conclusão positiva (a v2.2 serve como portão), não sustenta.

**Impedimentos à homologação do Crítico:**
- ausência de avaliador humano independente (a G2 e a arbitragem são não independentes);
- erro persistente em AMBÍGUA nas duas referências (12 a 13 de 16 aprovadas no rótulo externo; 3 de 3 aprovadas na sua arbitragem);
- a instabilidade da fronteira APROVADA/REVISAR (a diferença entre duas execuções do mesmo prompt pesa mais que a diferença entre versões);
- a verificação da C1b, o único teste desenhado para tratar a falha, está suspensa e depende da sua decisão sobre L8CFD.

**Importante para a decisão da arbitragem:** na arbitragem, nenhum dos cinco RUIM aprovados persistentemente foi RUIM para você, então o risco "Crítico aprova RUIM" não foi demonstrado no seu padrão. O risco demonstrado é "Crítico aprova AMBÍGUA como se estivesse pronta". Isso condiz com o papel consultivo que o Crítico tem hoje na skill, e é o argumento para mantê-lo assim.

**Conclusão e restrição mantida:** não há dado suficiente para promover a C1b, e não há necessidade de nova rodada para concluir a auditoria do Crítico: a conclusão cabe nos dados existentes. As 72 avaliações continuam suspensas.

---

## 5. Auditoria da skill v0.1.1

| Item | Constatação | Ação proposta (v0.2, não aplicada) |
|---|---|---|
| Entradas e saídas | Claras: história, foto, prompt, PNG e .checagem.json, CSV | Manter |
| Estados operacionais | Unificados (RASCUNHO a PUBLICADO), legados lidos como equivalentes | Manter |
| Geração e controle de repetição | Criador com 3 candidatas, filtros determinísticos, janelas de repetição do config | Manter; julgamento de originalidade (critério C) continua humano |
| Avaliação | Crítico v2.2 consultivo, nunca portão; REVISAR não avança; máximo 2 ciclos | Manter. É coerente com a evidência |
| Rejeição | Eliminatórias e REPROVADA, com a restrição de que AMBÍGUA nunca é apresentada como pronta | Manter |
| Numeração | Reserva, confirmação e liberação com CSV próprio, recusa o contador real | Atualizar o formato do número real para "001" (decisão sua de 24/10); manter LAB- só em testes |
| Composição visual | Perfis A e B, bloqueio técnico de arte, zonas de segurança 250 e 340 px provisórias | Incorporar, como perfil novo e versionado, os ajustes que você decidiu (seção 7); zonas continuam provisórias até verificação |
| Fontes | Inter em OTF com OFL.txt | Manter; fonte não está homologada |
| Falhas | Texto que não cabe ou elemento em zona de segurança bloqueia; nunca altera o texto | Manter |
| Aprovação humana | Exigida em proposta, foto e arte; a skill nunca publica | Manter |
| Piloto manual contra autônomo | Separados; proibições explícitas (n8n, fila, grade, contador, 72 avaliações, C1b) | Manter |
| Gerador de imagem | SKILL.md e referências dizem "Gemini/Nano Banana" | Reescrever como "gerador escolhido por Eri (Gemini, ChatGPT ou outro)". Na prática o ChatGPT foi usado nas versões v2 a v10 e você o considerou melhor |
| Análise de foto | Verifica formato e proporção e orienta APTA/AJUSTAR/REFAZER, limite de 2 gerações por história | Incorporar o Padrão de Excelência Fotográfica (item da seção 6), com os limites abaixo |
| Limite de 2 gerações | Foi ultrapassado no LAB-001 (v1 a v10) por autorizações suas | Manter o limite como padrão e documentar o caminho de exceção: autorização expressa, registrada |
| Medições | Não existe medição de contraste nem de inclinação | Incluir medição de contraste efetivo e de verticalidade/inclinação como ferramentas de apoio, não como garantia |
| Dependências | Sem dependência nova | Qualquer dependência nova precisa de justificativa |

Não encontrei contradição interna entre os arquivos da skill. Encontrei dois descompassos com o que foi decidido depois da v0.1.1: o formato do número e o gerador de imagem. Também há descompassos de layout (seção 7).

---

## 6. Auditoria fotográfica

**Evidência do LAB-001 (10 versões).** Registrada na pasta pilotos/LAB-001, uma auditoria por versão, com hashes. O que se confirmou:

1. O gerador acerta realismo, luz, fundo e composição, mas ignora instruções de **geometria** (inclinação de haste, rotação de objeto) e volta à pose que prefere. Seis tentativas de corrigir a inclinação falharam (v2, v3, v5, v7, v8, v9).
2. Edição de pixels tem limite: tratamento de tom (piso) é seguro e divulgável; mover ou girar o objeto principal deixa artefatos porque o fundo atrás dele não existe em nenhuma versão.
3. A cena que resolveu o problema foi uma mudança de arranjo físico: guarda-chuva em pé sobre o cabo, haste vertical (0,3 grau de desvio medido), sem apoio na parede.
4. O contraste do texto depende do brilho do piso e do rótulo pequeno; a medição efetiva (texto com transparência real contra o fundo com degradê) mostrou limites abaixo do mínimo provisório no rótulo NA FOTO (4,1 de 4,5), resolvido no perfil de teste com transparência 215 e degradê do topo reforçado.

**Avaliação do Padrão de Excelência Fotográfica (proposto).**

| Elemento do padrão | Veredito da auditoria |
|---|---|
| Realismo documental, coerência física, ausência de artefatos | Adequado e comprovado como útil: o critério de sustentação pegou um defeito real (haste inclinada), embora sutil |
| Correspondência foto e narrativa; não antecipar o FORA | Adequado |
| Resolução (941 px nas versões do ChatGPT, na faixa de atenção 810 a 1079) | Limiar provisório; a skill não deve prometer que 941 px é a resolução ideal |
| Composição e legibilidade | Adequado; a medição de contraste efetivo é necessária. O meu indicador automático de sobreposição subestima e não deve ser usado como portão |
| Resultados APTA, AJUSTAR, REFAZER | Adequado; manter definições objetivas dos defeitos impeditivos |
| Limite de duas correções | Adequado como padrão, desde que a exceção seja uma decisão humana registrada. A experiência mostra que insistir na mesma pose gasta tentativas; a orientação certa é mudar o arranjo físico, não repetir a instrução |
| Mecanismos de rejeição | Adequados; incluir "mudar a cena" como alternativa explícita a REFAZER idêntico |
| Reprodutibilidade entre episódios | Não demonstrada. Uma única cena foi calibrada. Recomendo escolher, quando a história permitir, cenas fisicamente estáveis e pedir ao gerador uma mudança verificável por vez |

**Gemini e Nano Banana:** tratar como ferramentas possíveis, não exigência nem garantia, como você pediu. O ChatGPT foi o gerador efetivo e a skill precisa deixar de nomear um só.

**A fotografia do guarda-chuva não está aprovada editorialmente.** O que existe é: foto-base proposta (v10 tratada), aprovação visual da arte pendente, e a história L8CFD em situação metodológica especial (possível contaminação). A assinatura e o número aprovados em layout não equivalem à aprovação da foto, da fonte ou do texto.

---

## 7. Identidade visual e numeração

**O que consta nos arquivos da skill v0.1.1:** topo com nome da série e número no canto direito, blocos NA FOTO e FORA, assinatura exclusiva @surtodelucidez no rodapé, número no formato "Nº NNN" para peças reais e LAB-NNN para testes. Tudo marcado como provisório.

**O que você decidiu depois (registrado em `pilotos/LAB-001/DECISOES_EDITORIAIS_LAB-001.md`, vale hoje só no perfil de teste B215):**
- número da série colado ao nome da série, e não alinhado à margem direita;
- assinatura @surtodelucidez menor (22 px no teste, antes 27, ou seja, cerca de 19% menor);
- número real exibido só como "001", sem "Nº";
- rótulos NA FOTO e FORA com transparência 215/255 e degradê do topo reforçado.

**Discrepância a esclarecer:** o seu pedido fala em "numeração aproximadamente 20% menor". Não encontrei esse registro em nenhum arquivo do repositório. Na conversa de 24/10 a sua instrução foi que o "nome Surtodelucidez" ficasse "um pouco menor", e eu entendi como a assinatura do rodapé, reduzindo-a cerca de 19%. O número manteve 30 px. Preciso que você confirme qual elemento deve ficar 20% menor (a assinatura, o número, ou os dois).

**Incorporação:** ainda não consta na skill. Proposta versionada: novo perfil C, derivado do B, com as decisões acima, sem apagar os perfis A e B; documentar que posição, fonte, dimensões e zonas de segurança continuam sem homologação.

**Fonte:** a recomendação de tipografia (Inter) não é decisão homologada; o único documento correspondente é a licença OFL e a escolha técnica do piloto.

---

## 8. Arquitetura futura com n8n (avaliação técnica, sem ativar nada)

Fase atual: produção e avaliação manual supervisionada. Fase futura: possível integração automática. Requisitos técnicos mínimos, sem os quais a autonomia não é segura:

| Requisito | Situação |
|---|---|
| Impedir repetição narrativa | Há filtros de similaridade e janelas; falta um julgador de originalidade que não seja o mesmo modelo gerador |
| Diversidade de situações | Janelas do config (mecanismo, emoção, abertura) existem; não são testadas em volume |
| Controle de numeração | Especificado (livro-razão append-only com reservado, confirmado, liberado, inconclusivo); depende de confirmar se a conferência de um estado "inconclusivo" é possível no prazo de insights de Stories |
| Impedir publicação de material reprovado | Exige portão editorial que hoje não existe: o Crítico não protege (G3), e a aprovação humana é o único portão real |
| Registro de versões e decisões | Já é prática do repositório (lacres, hashes, commits); precisa de espelho operacional |
| Falhas de geração | Ensaio com publicador de mentira especificado e não executado |
| Alterações involuntárias da grade | A série tem de ficar fora de fila, grade e scripts existentes até autorização específica; hoje isso é verdade |
| Foto sem aprovação humana | Impossível no desenho atual: o padrão fotográfico tem componente semântico que depende de julgamento humano |

**Conclusão:** a autonomia editorial não é demonstrada nem pelo Crítico, nem pelo avaliador, nem pela fotografia. O primeiro passo realista, quando você decidir, é um ensaio operacional sem publicar, com contador LAB- e publicador de mentira. Nada disto é autorização operacional presente.

---

## 9. Respostas às questões numeradas

**QUESTÃO 1: Qual é a versão mais recente da SKILL efetivamente documentada e utilizável?**
A v0.1.1 (piloto manual supervisionado), de 23/10/2026. Está em `skill_piloto/o-que-ninguem-legenda-piloto/`, empacotada em `skill_piloto/dist/o-que-ninguem-legenda-piloto-v0.1.1.zip` (SHA-256 7791524dbfa2787ae09cfb41254069f2e81de2b9c6c16a5ba363f722b8a6f301), com 23 testes passando e conferidor sem falhas. A v0.1 está preservada. Não existe v0.2 em arquivos, somente em proposta.

**QUESTÃO 2: Quais elementos estão homologados, quais são provisórios e quais foram apenas propostos?**

| Categoria | Elementos |
|---|---|
| Homologados | Nenhum. Existem autorizações (uso manual supervisionado da v0.1.1 em 23/10) e decisões editoriais suas, mas nenhum item recebeu homologação formal |
| Decisões suas vigentes (não são homologação) | Piloto manual supervisionado; perfil B como base provisória de layout (assinatura exclusiva, ordem NA FOTO e depois FORA); proibições sobre n8n, grade, fila, contador, publicação; as 72 avaliações suspensas; número real "001" sem "Nº"; manutenção do padrão de excelência fotográfica sem afrouxar; classificações lacradas da arbitragem dos 6 itens |
| Provisórios | Crítico v2.2 (consultivo, referência provisória); gatilho 12!; perfil B oficial e o perfil de teste B215; zonas de segurança 250 e 340 px; fonte Inter; limites do config.json; estados do registro; limiares fotográficos (resolução, contraste 4,5 e 3,0, composição); foto-base v10 tratada e a classificação "BOA, FUNCIONAL" de L8CFD |
| Apenas propostos | Núcleo de identidade editorial; C1 (nunca executada) e C1b (congelada, não executada); verificação da Emenda 2 (suspensa); Padrão de Excelência Fotográfica; livro-razão do contador com 4 estados; Auditor Visual da Fase B; política de estoque; integração com n8n; v0.2 |

**QUESTÃO 3 e seguintes:** o arquivo recebido termina em "QUESTÃO 3:". Reenvie o restante do texto, que eu respondo.

---

## 10. O que falta para encerrar a fase de desenvolvimento do piloto com segurança

Itens que dependem de você, sem nova rodada de experimentos:

1. **LAB-001:** aprovação visual da arte (foto v10 tratada, layout B215) e decisão sobre a ponteira sob o título, o número sobre a janela clara e a poça junto ao rótulo.
2. **Discrepância de layout:** qual elemento deve ficar 20% menor (assinatura, número, ou ambos), e se o espaço entre título e número deve ser maior.
3. **L8CFD:** decidir, em registro próprio, se mantém, exclui ou substitui na verificação, ou se encerra a verificação da C1b sem executá-la. As 72 avaliações continuam suspensas até lá.
4. **Classificação cega das 12 inéditas:** só se a verificação da C1b for mantida; se for encerrada, registrar o encerramento.
5. **Padrão de Excelência Fotográfica:** aprovar, ajustar ou rejeitar, incluindo os limiares e o limite de duas correções com exceção humana registrada.
6. **v0.2:** autorizar a implementação versionada (padrão fotográfico, número "001", gerador não exclusivo, perfil C com as decisões de layout, ferramentas de medição de contraste e de inclinação), preservando a v0.1.1 e todos os arquivos congelados. Eu implemento e reverifico os testes, sem tocar em n8n, grade, fila, contador ou lacres.
7. **Documentos das séries irmãs:** enviar Cena Cortada, Nota Fiscal Emocional e Palavra em Julgamento, para fechar o critério de diferenciação (seção 3, G).
8. **Política de plataformas:** verificar a regra de rotulagem de conteúdo gerado por IA antes da primeira publicação. Não foi verificada.
9. **Homologações futuras** (fonte, dimensões, margens, zonas de segurança, posições, trigger 12!): continuam fora desta fase.

Não considero necessário: nova rodada do Crítico, nova geração de histórias ou qualquer experimento novo para encerrar o piloto manual.

---

## Anexo: restrições cumpridas

n8n, grade, fila, contador real, publicação, horários do @surtodelucidez: não tocados. Crítico v2.2, v2.3, v2.4: não promovidos. C1b e Emenda 2: não homologadas. 72 avaliações: não executadas. Prompts e dados congelados: intactos (lacres conferidos). Nenhum crédito consumido, nenhuma imagem paga gerada.
