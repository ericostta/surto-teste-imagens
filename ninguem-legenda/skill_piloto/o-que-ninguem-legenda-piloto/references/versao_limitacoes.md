# Versão, limitações e controle de mudanças

## Identificação
O QUE NINGUÉM LEGENDA, PILOTO MANUAL v0.1 (23/10/2026). Uso manual e supervisionado.

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

## Origem dos arquivos copiados do laboratório
- references/critico_v2_2_referencia.md: cópia literal de prompts/critico_v2_2.md (SHA-256 468fd3823f83909dd87127d7a4affd835df4be09c7601e62c37b38dc54b553a3).
- references/preditor_cego.md: cópia literal de prompts/preditor.md.
- scripts/filtros.py: cópia de filtros.py com uma única mudança (histórico lido de registro_piloto.csv ou de --registro). scripts/config.json e scripts/taxonomia.json: cópias literais.
- assets/fonts: Inter Regular, Medium e SemiBold (licença SIL Open Font License 1.1, The Inter Project Authors).
