# Versão, limitações e controle de mudanças

## Identificação
O QUE NINGUÉM LEGENDA, PILOTO MANUAL v0.2.1 (30/10/2026), derivado da v0.2 e da v0.1.1 (ambas preservadas integralmente). Uso manual e supervisionado.

## O que esta versão É
Uma skill operacional para criar e avaliar histórias originais, preparar prompts fotográficos para o gerador de imagem que Eri escolher (Gemini, ChatGPT ou outro, sem exclusividade), analisar a foto que Eri gerar e montar a peça do Story para aprovação dela.

## O que NÃO é
- Não é homologação do sistema, do núcleo editorial, do Crítico nem do layout.
- Não integra n8n, não insere histórias na fila de publicação, não altera a grade de dez publicações, não publica Story, não consome nem aciona o contador real, não gera imagens automaticamente, não usa serviços pagos, não compra créditos.
- Não promove a candidata C1b, que permanece experimental e isolada (fora desta skill).

## Limitações conhecidas
1. O Crítico v2.2 é referência provisória e consultiva. Pode aprovar histórias que Eri classificaria AMBÍGUA, e seu veredicto oscila entre execuções. Quem aprova é Eri.
2. Avaliadores da mesma família de modelos que cria as histórias: concordância entre modelos não é validação editorial independente.
3. O núcleo de identidade editorial é proposta conceitualmente aprovada, não homologada.
4. Layout, posição, tamanho, hierarquia e composição dos elementos visuais NÃO estão homologados. As zonas de segurança (250 px no topo e 340 px embaixo) são valores provisórios a verificar.
5. A numeração do piloto é manual (registro anexado por Eri). A skill não enxerga o contador real.
6. Sem a ferramenta de agentes, as previsões "cegas" e a avaliação do Crítico perdem independência (a skill declara isso).
7. A skill instalada não grava arquivos entre conversas: o registro do piloto vive no CSV que Eri anexa e recebe de volta.
8. O Padrão de Excelência Fotográfica é referência operacional provisória: os limiares de contraste, de resolução e de inclinação não estão homologados, uma única cena foi calibrada (reprodutibilidade entre episódios não demonstrada) e o contraste medido não inclui a sombra do texto.
9. Geradores de imagem costumam ignorar instruções de geometria (inclinação, rotação) e voltar à pose preferida; a correção mais eficaz foi mudar o arranjo físico da cena, descrito por pontos de contato.
10. Os 12 textos do lote cego da verificação da C1b e os 60 itens da G1 não são material da skill. O experimento permanece separado da produção manual.
11. O perfil D (v0.2.1) é proposta visual: a mancha de escurecimento cobre o bloco inferior e o título em posições calculadas para o caso do piloto; a mancha não foi testada em fotos muito claras ou muito escuras, e o contraste continua sendo apenas medido e avisado, nunca garantido.

## Controle de versões
Qualquer mudança futura recebe nova versão (v0.3...) e preserva o histórico anterior. Não alterar retrospectivamente dados experimentais congelados.

| Versão | Data | Mudança |
|---|---|---|
| v0.1 | 23/10/2026 | Primeira versão utilizável: fluxo manual de 8 passos, Crítico v2.2 consultivo, prompt fotográfico, análise visual, composição provisória do Story, regras provisórias de assinatura e numeração. |
| v0.1.1 | 23/10/2026 | Revisão técnica mínima após auditoria: (1) estados do registro unificados entre documento e filtros, com legados e teste de que histórias aprovadas e publicadas entram no controle de similaridade, repetição e diversidade; (2) config.json identifica a v2.2 como Crítico consultivo e não aponta para a v2.1 nem para caminhos do laboratório; (3) conferência de prompt em duas camadas, com análise semântica obrigatória; (4) bloqueio técnico da arte quando o texto não cabe ou invade zonas de segurança, sem nunca alterar o texto; (5) reserva, confirmação e liberação de números no registro do piloto, com recusa de reutilização de número confirmado; (6) licença OFL completa das fontes; (7) duas propostas visuais, A e B; (8) verificar_skill.py e testes reproduzíveis. |
| v0.2 | 30/10/2026 | Alterações pedidas por Eri e justificadas na auditoria de 29/10: (1) número público exibido como 001, sem "Nº"; (2) perfil de layout C (padrão), com o número discreto abaixo de @surtodelucidez, à esquerda, assinatura em 22 px, rótulos em alfa 215 e degradê do topo reforçado, sem homologar o layout inteiro; (3) gerador de imagem não exclusivo; (4) Padrão de Excelência Fotográfica incorporado como referência provisória, com contraste efetivo no relatório de composição, scripts/medir_inclinacao.py e faixa de atenção de resolução; (5) exceção documentada ao limite de duas correções; (6) lição de prompt por pontos de contato físicos. Sem mudança no Crítico v2.2, nos controles de repetição, na numeração e nos dados congelados. |
| v0.2.1 | 30/10/2026 | Layout escolhido por Eri na rodada visual de 30/10 (perfil D, novo padrão; A, B e C continuam disponíveis e geram arte idêntica à da v0.2): blocos mais baixos, traço divisor de largura total, "001" sob o S e o U, escurecimento suave localizado atrás do título e do bloco inferior (sem degradê inferior) e título em duas linhas (O QUE NINGUÉM pequeno; LEGENDA em EB Garamond SemiBold, serifa reta). Inclui a fonte EB Garamond SemiBold com sua licença OFL (assets/fonts/OFL_EBGaramond.txt). Sem mudança no Crítico v2.2, nos controles, na numeração, no Padrão de Excelência Fotográfica e nos dados congelados. Layout, fonte e valores de escurecimento seguem não homologados. |

## Circunstância registrada: L8CFD
A história L8CFD pertence ao lote cego de 12 histórias da verificação experimental da C1b. Ela foi discutida e escolhida como primeiro piloto visual, e uma avaliação provisória de Eri ("BOA, detalhe funcional") foi dita fora do registro lacrado. Isso pode contaminar a referência cega dela. Não se altera nenhum item congelado nem se substitui história automaticamente. As 72 avaliações permanecem suspensas. Qualquer mudança na participação de L8CFD na verificação é desvio metodológico a documentar e depende de autorização expressa de Eri.

## Origem dos arquivos copiados do laboratório
- references/critico_v2_2_referencia.md: cópia literal de prompts/critico_v2_2.md (SHA-256 468fd3823f83909dd87127d7a4affd835df4be09c7601e62c37b38dc54b553a3).
- references/preditor_cego.md: cópia literal de prompts/preditor.md.
- scripts/filtros.py: cópia de filtros.py com mudanças do piloto (histórico lido de registro_piloto.csv ou de --registro; estados canônicos e legados). scripts/config.json: cópia ajustada (versão do Crítico v2.2 e caminho interno da skill). scripts/taxonomia.json: cópia literal.
- assets/fonts: Inter Regular, Medium e SemiBold, com a licença SIL Open Font License 1.1 completa em assets/fonts/OFL.txt (copyright The Inter Project Authors).
