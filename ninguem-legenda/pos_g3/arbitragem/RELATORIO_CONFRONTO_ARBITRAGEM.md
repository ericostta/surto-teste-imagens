# Confronto da arbitragem de Eri (seis histórias)

Data: 23/10/2026. As seis decisões foram lacradas no commit d4399f4 antes de abrir o mapa privado, cujo hash conferiu com o registrado em e5da566. Nenhuma decisão foi alterada depois do lacre. Rótulos históricos, G1, G2, G3 e M1 permanecem intactos. A G3 não foi recalculada.

**Natureza das decisões:** decisão editorial de Eri como responsável pelo projeto, tomada em conversa com o ChatGPT, que também é o avaliador externo dos rótulos originais. Não é auditoria humana independente nem avaliação livre de influência. Seis itens, escolhidos por serem os mais discutidos: não são amostra representativa.

## Tabela

| Código | Original | Eri | Rótulo externo | Tensão | v2.2 e1, e2 | v2.4-exp e1, e2 |
|---|---|---|---|---|---|---|
| Q6NC | G1-D04 | AMBÍGUA | RUIM | B | Apr, Apr | Apr, Apr |
| Q8N9 | G1-D31 | BOA | RUIM | B | Apr, Apr | Apr, Apr |
| Q0JK | G1-F22 | AMBÍGUA | RUIM | B | Apr, Apr | Apr, Apr |
| Q6TV | G1-D15 | BOA | BOA | A | Rev, Apr | Rev, Rep |
| QG3F | G1-F26 | BOA | RUIM | B | Apr, Apr | Apr, Apr |
| QNB0 | G1-D32 | AMBÍGUA | RUIM | B | Apr, Apr | Apr, Apr |

Apr = APROVADA, Rev = REVISAR, Rep = REPROVADA.

## Consequências por caso

- **D31 e F26 (BOA para Eri, RUIM externo):** os Críticos aprovaram nas quatro execuções, o que coincide com a sua decisão. O rótulo RUIM foi excessivamente severo nestes dois casos.
- **D04, F22 e D32 (AMBÍGUA para Eri, RUIM externo):** o rótulo RUIM foi severo demais, pois nenhum foi RUIM para você. Mas a aprovação dos Críticos, nas quatro execuções, também diverge da sua leitura: AMBÍGUA não autoriza publicação automática. Aqui há uma falha de discernimento do Crítico de grau AMBÍGUA, não de grau RUIM.
- **D15 (BOA nos dois):** a v2.2 não aprovou em uma de duas execuções (Rev, Apr). A v2.4-exp não aprovou em nenhuma (Rev, Rep). Em relação à sua decisão, a v2.4-exp errou de forma consistente e a v2.2 de forma parcial. É o único caso do pacote em que as versões se distinguem.

## A. O que as seis decisões esclareceram

1. Dos cinco itens RUIM aprovados persistentemente, **nenhum foi RUIM para você**. A categoria "RUIM aprovado pelo Crítico", que dominou a leitura da G3, não representa falha grave do Crítico neste conjunto. Isso vale para estes cinco, não se extrapola aos outros seis RUIM, que não foram arbitrados.
2. O rótulo externo RUIM foi mais severo que a sua decisão em 5 de 5 casos. Isso reforça que a referência única do ChatGPT era dura nos itens de tensão B.
3. A discordância que sobra é entre BOA e AMBÍGUA, não entre aprovar e reprovar: em 3 dos 5 casos o Crítico aprovou o que você classifica como AMBÍGUA.

## B. O que permanece problemático no Crítico v2.2

- Tendência a aprovar histórias de grau AMBÍGUA. Na sua arbitragem, 3 de 3 casos; no rótulo externo, 12 ou 13 de 16 AMBÍGUA aprovadas. As duas referências apontam na mesma direção, mas ambas passaram pela mesma influência.
- Instabilidade de veredicto em itens de fronteira (D08, D15, F29, entre outros) e sinal de previsibilidade variável entre execuções.
- Não há evidência, neste conjunto, de que a v2.2 aprove RUIM no seu padrão.

## C. Correção mínima justificável ou versão inalterada

**Manter a v2.2 inalterada por ora.** Razões: (1) três casos AMBÍGUA numa decisão influenciada não bastam para redigir uma regra; (2) os 60 itens da G1 estão contaminados e qualquer regra nova não poderia ser testada neles; (3) o que falta não é uma regra no Crítico, e sim saber se o seu padrão de publicação tolera histórias AMBÍGUA. Esta é uma decisão sua sobre risco, não um achado técnico.

Se você decidir que AMBÍGUA não pode ser publicada sem revisão, aí sim a correção mínima seria uma única regra no limiar de aprovação do v2.2, feita só em prompt novo, testada apenas em itens inéditos e com autorização expressa. Nada disso foi feito ou preparado.

## D. Próximo passo indispensável

**Uma decisão sua, em uma frase:** na implantação controlada, uma história que o Crítico aprova mas que você classificaria como AMBÍGUA pode ir ao ar? Se sim, o caminho é implantar com a v2.2 inalterada, com monitoramento descritivo (Metricool) e revisão periódica de concentrações, sem novos experimentos. Se não, o próximo passo é a correção mínima descrita em C, testada em itens inéditos. Em ambos os casos, o gate de dupla avaliação não é recomendado e nenhuma homologação decorre desta arbitragem.

## Assinaturas e contador público (pendência da etapa operacional)

Registrada, sem alteração. No repositório do laboratório não há especificação de assinatura visual nem do contador. O único registro que tenho é a numeração sequencial 001, 002 do DNA Editorial inicial, cujo documento original não está no repositório. Antes da implantação é preciso localizar essa especificação com você. Regra proposta, a confirmar: o contador público avança somente na publicação efetiva, nunca em teste, rascunho, falha ou história descartada. Nada foi alterado.
