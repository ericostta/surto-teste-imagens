# Protocolo de verificação limitada da candidata C1b (versão atualizada, NÃO executado)

Data: 23/10/2026. Substitui o desenho A.3 de `pos_g3/ENTREGA_PROXIMA_ETAPA.md` (que permanece como registro histórico). Nada aqui foi executado. A v2.2 em `prompts/`, o validador, os registros de M1, G1, G2 e G3 e os 60 itens da G1 permanecem intactos. Este protocolo só entra em vigor se Eri autorizar a Emenda 2 (`EMENDA_2_MINUTA.md`).

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
- A v2.2 também é reexecutada nelas, para a comparação ocorrer nas mesmas condições (muda de 60 para 72 avaliações, ver 5). As quatro execuções da G3 ficam como dado histórico, não como baseline desta rodada.
- Limite declarado: D04, F22 e D32 foram a origem do desenho da C1. Acertá-las é verificação de que a mudança faz o que foi desenhada para fazer, não validação. Por isso a regressão nunca entra na contagem de ganhos da seção 6.
- Dado que importa para o risco: dos seis, Q8N9 ("onze anos", "quatro") e QG3F ("três vezes") são BOA com detalhe numérico, e QNB0 ("onze") é AMBÍGUA com detalhe numérico. Eri pode, se quiser, anotar também o papel do detalhe numérico nesses itens (seção 4, campo 2); isso torna a regressão um teste de proteção de número funcional já com dois casos reais.

## 4. Referência: classificação às cegas de Eri

Antes de qualquer Crítico rodar, Eri recebe um pacote com as 12 inéditas (mais as 6 apenas se quiser anotar o papel do número), códigos novos, ordem embaralhada, a mesma referência editorial uniforme do pacote de arbitragem, sem grupo, sem veredicto, sem previsão. Para cada código, dois campos:
1. BOA, AMBÍGUA ou RUIM (justificativa breve opcional);
2. papel do detalhe numérico: FUNCIONAL, DECORATIVO ou SEM DETALHE NUMÉRICO.

Registro literal, SHA-256 e commit antes de qualquer execução, e nota de natureza: referência de Eri, não independente se houve conversa com ChatGPT, e todos os avaliadores são da mesma família de modelos. O mapa de códigos permanece privado até o lacre.

## 5. Execuções

- Versões: v2.2 (hash 468fd382…, congelada) e C1b (hash a1b5b47e…, `critico_v2_2_c1b.md`).
- Duas execuções por versão, mesmo pacote de 18 itens, mesmas três previsões, códigos e ordem embaralhados por execução, cada execução em agente novo e isolado. 18 itens x 2 execuções x 2 versões = 72 avaliações (G3 teve 240).
- Validador congelado (`validar_avaliacao.py`) sobre cada saída. Saídas literais guardadas e lacradas com SHA-256 antes de abrir as classificações de Eri e o mapa.
- Falha técnica: uma reexecução por parte, com o motivo registrado. Todas as execuções entram na análise. Nenhuma execução favorável é escolhida depois.
- Sem rodada adicional, sem ajuste do prompt, sem ampliação automática da amostra, em nenhum desfecho.

## 6. Medidas e definições (fixadas antes de executar)

Todas por item, em listas, nunca em taxas.

- **Frágil**: item que Eri classificou AMBÍGUA ou RUIM. (RUIM é acréscimo em relação ao desenho anterior; ver pendência 1 da Emenda 2.)
- **Oportunidade (O)**: item frágil, entre as 12 inéditas, que a v2.2 aprovou nas duas execuções.
- **Corrigido**: oportunidade que a C1b não aprova em nenhuma das duas execuções.
- **Perda de BOA**: item que Eri classificou BOA, a v2.2 aprovou em pelo menos uma execução e a C1b não aprovou em pelo menos uma execução. Vale para as 12 inéditas e para as seis da regressão. Perda de BOA com detalhe numérico FUNCIONAL é registrada à parte como perda de proteção numérica.
- **Proteção numérica testável**: existe pelo menos um item BOA com detalhe FUNCIONAL (pela anotação de Eri) que a v2.2 aprovou nas duas execuções.
- **Aprovação sem sustentação**: aprovações de C1b em item frágil, descritas, sem efeito sobre a regra.
- **Leitura de causa (descritiva)**: para toda mudança de veredicto de C1b contra v2.2, citar o defeito da lista, o trecho e se a justificativa invoca E1, E5 ou a Salvaguarda. Serve para distinguir rigor por motivo demonstrado de reprovação por palavra-chave. Não entra na regra.
- **Controle de aumento artificial de reprovação**: relatar, por versão, o número de veredictos não APROVADA separado por classe de Eri (BOA, AMBÍGUA, RUIM) e por papel do número (FUNCIONAL, DECORATIVO, SEM DETALHE). Aumento de reprovação só em itens frágeis é ganho potencial; aumento em itens BOA é perda.
- Consistência entre execuções (itens com veredicto diferente dentro da mesma versão), relatada com listas.

## 7. Regra de decisão e quatro desfechos, fixados antes de executar

Condições:
- **C-a (ganho nas inéditas)**: pelo menos dois itens corrigidos, entre as oportunidades.
- **C-b (proteção de BOA)**: nenhuma perda de BOA, nas 12 inéditas e na regressão.
- **C-c (proteção numérica testável e preservada)**: proteção numérica testável e nenhuma perda de BOA com detalhe FUNCIONAL.
- **C-d (regressão)**: pelo menos dois de D04, F22, D32 não aprovados pela C1b nas duas execuções, e D31 e F26 aprovados nas duas.

Desfechos:
1. **BENEFÍCIO CLARO**: C-a, C-b, C-c e C-d juntas. Mesmo assim a C1b é apenas proposta para Eri decidir, sem promoção nem homologação automática.
2. **PIORA OBSERVADA**: qualquer perda de BOA (C-b falha), em especial de BOA com detalhe FUNCIONAL. A C1b não é promovida, a linha é encerrada, a v2.2 segue.
3. **SEM BENEFÍCIO (evidência negativa)**: o teste era possível (O >= 2 e proteção numérica testável), não houve perda de BOA, mas C-a ou C-d não foi atingida. A linha é encerrada, a v2.2 segue.
4. **INCONCLUSIVO**: o teste não podia decidir. Causas, uma ou mais: O <= 1 nas inéditas (C-a era inatingível, ausência de duas correções não demonstra ineficácia); proteção numérica não testável (nenhum BOA funcional aprovado pela v2.2 nas duas execuções); falha técnica não resolvida. A C1b não é promovida. O resultado da regressão é descrito como indício, não como prova. A amostra NÃO é ampliada automaticamente. Qualquer material novo só existe por nova autorização de Eri e com novo pré-registro, sem tratá-lo como continuação desta rodada.

Ordem de avaliação dos desfechos: primeiro falha técnica, depois PIORA (sempre prevalece), depois testabilidade (INCONCLUSIVO), depois SEM BENEFÍCIO, por último BENEFÍCIO CLARO.

Expectativa honesta sobre a chance de INCONCLUSIVO. Na G3, a v2.2 aprovou nas quatro execuções 11 de 16 itens AMBÍGUA (cerca de 70%). Se Eri classificar k das 12 inéditas como frágeis e a v2.2 se comportar parecido, a chance de ter O >= 2 é de cerca de 48% com k = 2, 77% com k = 3 e 91% com k = 4, e zero com k <= 1. Estimativa grosseira, que assume comportamento semelhante ao da G3 e não é garantia. Se Eri classificar menos de três como frágeis, o mais provável é INCONCLUSIVO, e isso é um resultado legítimo, não um fracasso a corrigir com mais material.

## 8. Limites declarados que permanecem em todos os desfechos

- Rótulos de Eri, possivelmente conversados com ChatGPT; avaliadores da mesma família de modelos que gerou as histórias. Nada aqui é confirmação editorial independente.
- Doze histórias inéditas: resultados são sobre itens, não sobre taxas nem sobre a produção futura.
- Estresse não é produção real.
- A regressão está contaminada por construção (origem do desenho).
- Não se recalcula a G3 e não se usa a G1 como nova validação.
