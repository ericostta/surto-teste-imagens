# Protocolo de verificação limitada da candidata C1b (versão atualizada, NÃO executado)

Data: 23/10/2026, revisado após a decisão de Eri de 23/10 (16:53) sobre a C1b. Substitui o desenho A.3 de `pos_g3/ENTREGA_PROXIMA_ETAPA.md` (que permanece como registro histórico). Este é o texto normativo anexo à Emenda 2; congelado na publicação dela. A v2.2 em `prompts/`, o validador, os registros de M1, G1, G2 e G3 e os 60 itens da G1 permanecem intactos. Entra em vigor com a publicação da Emenda 2 (autorizada por Eri em 23/10, condicionada à incorporação das correções abaixo).

## 1. O que se quer saber

Se a C1b reconhece melhor a diferença entre história BOA (inclusive aberta a várias leituras e inclusive apoiada em número), história AMBÍGUA (mérito insuficiente) e história RUIM, sem apenas reprovar mais. Um ganho só conta se vier sem perda de BOA e sem punir informação numérica funcional.

## 2. Material: doze histórias inéditas em cinco grupos

| Grupo | Qtd | Condição de produção (instrução ao Criador, lacrada, nunca vista pelos Críticos) |
|---|---|---|
| N. Número narrativamente indispensável | 3 | O número, idade ou quantidade é o próprio mecanismo da segunda leitura (por exemplo, a contagem que sustenta um contraste) |
| D. Número decorativo | 3 | O número, idade ou quantidade aparece como particularização que não muda a leitura da foto |
| M. Motivo declarado na última oração | 2 | A última oração explica o porquê |
| A. Aberta a várias leituras fortes | 2 | O FORA admite duas ou mais leituras legítimas e diferentes |
| P. Produção normal | 2 | Sem restrição; mostra o comportamento corrente |

Observações:
- Os grupos N, D, M e A são estresse e ficam declarados como tal. O grupo P não é amostra representativa da produção futura (12 itens não sustentam isso).
- A intenção de produção não é o rótulo. Quem decide se o número é funcional ou decorativo, e se a história é BOA, AMBÍGUA ou RUIM, é Eri, às cegas (seção 4). A análise agrupa pelas classificações dela, nunca pela intenção do Criador.
- Produzidas pelo Criador existente em agentes novos, sem acesso a Críticos, rótulos, às seis arbitradas ou aos 60 itens da G1 além do que o Criador já usa. Três previsões cegas frescas por item, por agentes que veem só foto e NA FOTO.
- Verificação mecânica prévia (apenas informativa): contagem de dígitos e numerais por extenso no FORA, para confirmar que N e D contêm detalhe numérico. Itens sem detalhe numérico nesses grupos são registrados, não substituídos.

## 3. Regressão conhecida (não é teste inédito)

As seis histórias arbitradas entram nos mesmos pacotes de 18 itens (12 inéditas + 6) para as duas versões:
- AMBÍGUA por decisão de Eri: Q6NC (D04), Q0JK (F22), QNB0 (D32). Espera-se que a C1b deixe de aprová-las.
- BOA por decisão de Eri: Q8N9 (D31), QG3F (F26), Q6TV (D15). D31 e F26 devem continuar aprovadas; D15 é observação (na G3 a v2.2 oscilou entre REVISAR e APROVADA nela).
- A v2.2 também é reexecutada nelas, para a comparação ocorrer nas mesmas condições (72 avaliações, autorizado por Eri). As quatro execuções da G3 ficam como dado histórico, não como baseline desta rodada.
- Limite declarado: D04, F22 e D32 foram a origem do desenho da C1. Acertá-las é verificação de que a mudança faz o que foi desenhada para fazer, não validação. Por isso a regressão nunca entra na contagem de ganhos da seção 6.
- Dado que importa para o risco: dos seis, Q8N9 ("onze anos", "quatro") e QG3F ("três vezes") são BOA com detalhe numérico, e QNB0 ("onze") é AMBÍGUA com detalhe numérico. Eri anota o papel do detalhe numérico nas seis (seção 4, etapa 2); isso torna a regressão um teste de proteção de número funcional já com dois casos reais. As classificações editoriais das seis, já lacradas (d4399f4), não são reabertas nem reclassificadas.

## 4. Referência: classificação às cegas de Eri, em duas etapas separadas

**Etapa 1, lote cego das 12 inéditas.** Antes de qualquer Crítico rodar, Eri recebe um pacote só com as 12 inéditas, códigos novos, ordem embaralhada, a mesma referência editorial uniforme do pacote de arbitragem, sem previsões, sem veredictos, sem grupos de produção e sem pista do resultado esperado. Para cada código, dois campos:
1. BOA, AMBÍGUA ou RUIM (justificativa breve opcional);
2. papel do detalhe numérico: FUNCIONAL, DECORATIVO ou SEM DETALHE NUMÉRICO.
Registro literal, SHA-256, commit e verificação do lacre antes de qualquer outra etapa.

**Etapa 2, anotação das 6 conhecidas.** Só depois de lacradas as 12 decisões, Eri recebe, separadamente, as seis histórias conhecidas apenas para anotar o papel do detalhe numérico (FUNCIONAL, DECORATIVO ou SEM DETALHE NUMÉRICO). Nenhuma reclassificação editorial delas. Registro literal e lacre próprios. A reavaliação dos casos conhecidos nunca se mistura com a primeira leitura cega das inéditas.

Nota de natureza em ambos os registros: referência de Eri, não independente se houve conversa com ChatGPT, e todos os avaliadores são da mesma família de modelos. O mapa de códigos permanece privado até os lacres. Os Críticos só rodam depois dos dois lacres.

## 5. Execuções

- Versões: v2.2 (hash 468fd382…, congelada) e C1b (hash a1b5b47e…, `critico_v2_2_c1b.md`).
- Duas execuções por versão, pacote de 18 itens, mesmas três previsões. Execuções emparelhadas: a execução 1 da v2.2 e a execução 1 da C1b usam exatamente o mesmo pacote (mesmos códigos, mesma ordem); idem para a execução 2, com códigos e ordem diferentes da execução 1. Cada execução em agente novo e isolado, com o mesmo modelo e configuração. 18 itens x 2 execuções x 2 versões = 72 avaliações (G3 teve 240).
- Validador congelado (`validar_avaliacao.py`) sobre cada saída. Saídas literais guardadas e lacradas com SHA-256 antes de abrir as classificações de Eri e o mapa.
- Falha técnica: uma reexecução por parte, com o motivo registrado. Todas as execuções entram na análise. Nenhuma execução favorável é escolhida depois.
- Sem rodada adicional, sem ajuste do prompt, sem ampliação automática da amostra, em nenhum desfecho.

## 6. Medidas e definições (fixadas antes de executar)

Todas por item, em listas, nunca em taxas. Seja a(v) o número de execuções (0, 1 ou 2) em que a versão v aprova o item.

- **Frágil**: item que Eri classificou AMBÍGUA ou RUIM. Os ganhos são apresentados separadamente em AMBÍGUA e em RUIM.
- **Oportunidade (O)**: item frágil, entre as 12 inéditas, com a(v2.2) = 2.
- **Corrigido**: oportunidade com a(C1b) = 0. **Correção parcial** (relatada à parte, sem contar para a regra): a(v2.2) > a(C1b) > 0 em item frágil.
- **Perda real de BOA**: item que Eri classificou BOA com a(C1b) < a(v2.2). Exemplos: 2 contra 1 é sinal de perda; 1 contra 0 é sinal de perda. **Não é perda**: a(C1b) = a(v2.2), mesmo com veredictos distintos entre execuções (por exemplo, as duas versões em REVISAR na execução 1 e APROVADA na execução 2, ou uma aprovando na execução 1 e a outra na 2). Ganho de aprovação em BOA (a(C1b) > a(v2.2)) é relatado como ganho, sem entrar na regra. Vale para as 12 inéditas e para as seis da regressão.
- **Oscilação**: item em que os veredictos diferem entre as duas execuções da mesma versão, ou em que, com a(C1b) = a(v2.2), o padrão por execução emparelhada difere. Relatada com a lista de itens e as comparações individuais por execução emparelhada, separadamente das perdas reais. Oscilação não é piora demonstrada.
- **Perda numérica**: perda real de BOA cuja anotação de Eri para o detalhe é FUNCIONAL, registrada também à parte.
- **Proteção numérica testável**: existe pelo menos um item BOA com detalhe FUNCIONAL (anotação de Eri, inéditas ou regressão) com a(v2.2) = 2.
- **Leitura de causa (descritiva)**: para toda mudança de veredicto de C1b contra v2.2, citar o defeito da lista, o trecho e se a justificativa invoca E1, E5 ou a Salvaguarda. Distingue rigor por motivo demonstrado de reprovação por palavra-chave. Não entra na regra.
- **Controle de aumento artificial de reprovação**: relatar, por versão, os veredictos não APROVADA por classe de Eri (BOA, AMBÍGUA, RUIM) e por papel do número. Menos aprovações, isoladamente, não é melhoria editorial. Aumento só em itens frágeis é ganho potencial; em itens BOA é perda.
- **Alcance do ganho**: toda afirmação de benefício declara em que categoria ocorreram as correções. Se as únicas correções forem em RUIM, o relatório não afirma que a C1b demonstrou resolver a fronteira entre BOA e AMBÍGUA.

A saída por história inclui: classificação e papel numérico de Eri, veredictos de ambas as versões nas duas execuções, diferenças entre execuções, ganhos, perdas e as justificativas citadas.

## 7. Regra de decisão e quatro desfechos, fixados antes de executar

Condições:
- **C-a (ganho nas inéditas)**: pelo menos dois itens corrigidos, entre as oportunidades.
- **C-b (proteção de BOA)**: nenhuma perda real de BOA (definição da seção 6), nas 12 inéditas e na regressão.
- **C-c (proteção numérica testável e preservada)**: proteção numérica testável e nenhuma perda numérica.
- **C-d (regressão)**: pelo menos dois de D04, F22, D32 com a(C1b) = 0, e D31 e F26 com a(C1b) = 2.

Desfechos:
1. **BENEFÍCIO CLARO**: C-a, C-b, C-c e C-d juntas, com o alcance declarado (seção 6). Se as correções das inéditas forem só em itens RUIM, o desfecho é lido como BENEFÍCIO CLARO LIMITADO A RUIM e não afirma resolução da fronteira BOA e AMBÍGUA. Em qualquer caso a C1b é apenas proposta para Eri decidir, sem promoção nem homologação automática.
2. **PIORA OBSERVADA**: qualquer perda real de BOA (C-b falha), em especial perda numérica. A C1b não é promovida, a linha é encerrada, a v2.2 segue.
3. **SEM BENEFÍCIO (evidência negativa)**: o teste era possível (O >= 2 e proteção numérica testável), não houve perda de BOA, mas C-a ou C-d não foi atingida. A linha é encerrada, a v2.2 segue.
4. **INCONCLUSIVO**: o teste não podia decidir. Causas, uma ou mais: O <= 1 nas inéditas (C-a era inatingível, ausência de duas correções não demonstra ineficácia); proteção numérica não testável (nenhum BOA funcional com a(v2.2) = 2); falha técnica não resolvida. A C1b não é promovida. O resultado da regressão é descrito como indício, não como prova. A amostra NÃO é ampliada automaticamente. Um resultado INCONCLUSIVO encerra esta rodada (decisão de Eri de 23/10). Nenhuma ampliação, ajuste sucessivo ou novo experimento sem autorização expressa e pré-registro independente, sem tratá-lo como continuação desta rodada.

Ordem de avaliação dos desfechos: primeiro falha técnica, depois PIORA (sempre prevalece), depois testabilidade (INCONCLUSIVO), depois SEM BENEFÍCIO, por último BENEFÍCIO CLARO.

Expectativa honesta sobre a chance de INCONCLUSIVO. Na G3, a v2.2 aprovou nas quatro execuções 11 de 16 itens AMBÍGUA (cerca de 70%). Se Eri classificar k das 12 inéditas como frágeis e a v2.2 se comportar parecido, a chance de ter O >= 2 é de cerca de 48% com k = 2, 77% com k = 3 e 91% com k = 4, e zero com k <= 1. Estimativa grosseira, que assume comportamento semelhante ao da G3 e não é garantia. Se Eri classificar menos de três como frágeis, o mais provável é INCONCLUSIVO, e isso é um resultado legítimo, não um fracasso a corrigir com mais material.

## 8. Limites declarados que permanecem em todos os desfechos

- Rótulos de Eri, possivelmente conversados com ChatGPT; avaliadores da mesma família de modelos que gerou as histórias. Nada aqui é confirmação editorial independente.
- Doze histórias inéditas: resultados são sobre itens, não sobre taxas nem sobre a produção futura.
- Estresse não é produção real.
- A regressão está contaminada por construção (origem do desenho).
- Não se recalcula a G3 e não se usa a G1 como nova validação.
