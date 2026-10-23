# Versão, limitações e controle de mudanças

## Identificação
O QUE NINGUÉM LEGENDA, PILOTO MANUAL v0.1.1 (23/10/2026). Uso manual e supervisionado.

## O que esta versão É
Uma skill operacional para criar e avaliar histórias originais, preparar prompts fotográficos para Gemini / Nano Banana, analisar a foto que Eri gerar e montar a peça do Story para aprovação dela.

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
8. Os 12 textos do lote cego da verificação da C1b e os 60 itens da G1 não são material da skill. O experimento permanece separado da produção manual.

## Controle de versões
Qualquer mudança futura recebe nova versão (v0.2, v0.3...) e preserva o histórico anterior. Não alterar retrospectivamente dados experimentais congelados.

| Versão | Data | Mudança |
|---|---|---|
| v0.1 | 23/10/2026 | Primeira versão utilizável: fluxo manual de 8 passos, Crítico v2.2 consultivo, prompt fotográfico, análise visual, composição provisória do Story, regras provisórias de assinatura e numeração. |
| v0.1.1 | 23/10/2026 | Revisão técnica mínima após auditoria: (1) estados do registro unificados entre documento e filtros, com legados e teste de que histórias aprovadas e publicadas entram no controle de similaridade, repetição e diversidade; (2) config.json identifica a v2.2 como Crítico consultivo e não aponta para a v2.1 nem para caminhos do laboratório; (3) conferência de prompt em duas camadas, com análise semântica obrigatória; (4) bloqueio técnico da arte quando o texto não cabe ou invade zonas de segurança, sem nunca alterar o texto; (5) reserva, confirmação e liberação de números no registro do piloto, com recusa de reutilização de número confirmado; (6) licença OFL completa das fontes; (7) duas propostas visuais, A e B; (8) verificar_skill.py e testes reproduzíveis. |

## Circunstância registrada: L8CFD
A história L8CFD pertence ao lote cego de 12 histórias da verificação experimental da C1b. Ela foi discutida e escolhida como primeiro piloto visual, e uma avaliação provisória de Eri ("BOA, detalhe funcional") foi dita fora do registro lacrado. Isso pode contaminar a referência cega dela. Não se altera nenhum item congelado nem se substitui história automaticamente. As 72 avaliações permanecem suspensas. Qualquer mudança na participação de L8CFD na verificação é desvio metodológico a documentar e depende de autorização expressa de Eri.

## Origem dos arquivos copiados do laboratório
- references/critico_v2_2_referencia.md: cópia literal de prompts/critico_v2_2.md (SHA-256 468fd3823f83909dd87127d7a4affd835df4be09c7601e62c37b38dc54b553a3).
- references/preditor_cego.md: cópia literal de prompts/preditor.md.
- scripts/filtros.py: cópia de filtros.py com mudanças do piloto (histórico lido de registro_piloto.csv ou de --registro; estados canônicos e legados). scripts/config.json: cópia ajustada (versão do Crítico v2.2 e caminho interno da skill). scripts/taxonomia.json: cópia literal.
- assets/fonts: Inter Regular, Medium e SemiBold, com a licença SIL Open Font License 1.1 completa em assets/fonts/OFL.txt (copyright The Inter Project Authors).
