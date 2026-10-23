# Proposta v2.3-exp: ajustes ao Crítico (Fase A, experimental, não executada)

Data: 22/10/2026. A v2.2 e todos os resultados anteriores ficam preservados. Nada foi executado nesta etapa. Os ajustes 1 e 2 existem como rascunho em prompts/critico_v2_3_exp.md (SHA-256 em prompt_travado.sha256, diff em alteracoes_prompt.diff). O ajuste 3 é apenas conceitual e aguarda aprovação.

## 1. Previsões cegas (implementado no rascunho)

Regra: a previsão, mesmo confirmada pelos três leitores, nunca constitui sozinha clichê, redundância ou falta de originalidade. O defeito precisa de demonstração narrativa independente, escrita sem citar as previsões (clichê: nomear a associação comum e mostrar no texto que nada específico a transforma; redundância: apontar qual informação do FORA já está na foto ou no NA FOTO). A previsão só entra depois, em frase própria iniciada por "Corroboração:".
Teste de verificação embutido: se, retirada a frase de corroboração, a demonstração não se sustenta, o defeito não está demonstrado e vai para observacoes_descartadas.
Efeito esperado: elimina a brecha usada pela execução 1 em Q05 e Q15.

## 2. Contradição (implementado no rascunho)

Procedimento antes de apontar: (a) escrever a interpretação alternativa mais natural em que os trechos coexistem; (b) se for plausível e natural, não há contradição; (c) só se for artificial ou excessivamente improvável, e a incompatibilidade for demonstrável com o próprio conteúdo, reportar. Na demonstração, "Alternativa natural:" e "Por que não vale:" tornam o raciocínio verificável.
Efeito esperado: a "contradição" de Q05 (execução 1) cairia, pois a alternativa natural existe.

## 3. Omissão legítima, imprecisão corrigível, obscuridade estrutural (SÓ CONCEITUAL, aguarda aprovação)

Diagnóstico de Q06, Q10 e Q22. Nas duas execuções, o Crítico enquadrou as três falhas apontadas pelo avaliador externo como "omissão legítima" ou "ambiguidade pequena". A v2.2 diz que omissão não é defeito, mas não dá um teste para distinguir omissão de elo que não fecha. Sem teste, a tolerância virou regra geral. Em Q10 o texto afirma um mecanismo (a fita faria com que ninguém corrigisse a nota) que não funciona como dito; isso não é informação ausente, é mecanismo afirmado que não se sustenta.

Critério proposto: a pergunta decisiva é "o texto diz algo que não fecha" versus "o texto cala algo". Três perguntas em ordem, respondidas com trecho citado.

1. Relação central. Escreva em uma frase a relação entre o elemento da foto e a revelação. Se não conseguir escrever sem escolher entre duas ou mais versões, ou sem inventar um elemento, vá à pergunta 3.
2. Teste da omissão. Que informação falta? Ao completá-la de qualquer modo plausível, a leitura central muda? Se a história continua a mesma e a lacuna apenas acrescenta interesse (o motivo do segredo, o nome do personagem), é A, omissão legítima. Registrar em observacoes_descartadas.
3. Teste do mecanismo. Se o texto afirma uma relação (causa, intenção, referência) e ela não funciona como escrita, ou exige escolher entre leituras que mudam o sentido, é B, imprecisão corrigível, quando um detalhe pontual resolve sem trocar o acontecimento central. É C, obscuridade estrutural, quando o leitor teria de inventar elementos essenciais.

Veredicto decorrente (regra mecânica, para estabilidade): só A, pode aprovar; qualquer B, REVISAR com a instrução "Defeito/Mudar/NÃO pode mudar"; qualquer C, REPROVADA. Não se pede explicação do que é sutileza (A não gera exigência).

Aplicação conceitual aos casos de diagnóstico (sem reclassificar os rótulos externos):
- Q10: mecanismo da fita não fecha, por isso B. O critério tende a detectá-lo.
- Q06: a referência de "para o lugar continuar dela" admite mais de uma leitura (o lugar da capa, o lugar da filha). Provável B.
- Q22: o critério NÃO resolve bem. O motivo do segredo é omissão legítima (A) e o problema apontado é outro: a palavra VÓ no NA FOTO antecipa o campo emocional. Isso é redundância parcial, hoje coberta pela lista, e o Crítico não a demonstrou. O critério 3 não melhoraria Q22.

## 4. Como isso reduziria AMBÍGUAS aprovadas sem prejudicar BOA

Honestidade primeiro: os ajustes 1 e 2 só restringem as razões para REVISAR. Isoladamente não reduzem aprovação de AMBÍGUA; se algo, tornam o Crítico um pouco mais brando. A redução depende do ajuste 3, que acrescenta uma razão verificável para REVISAR (o mecanismo que não fecha).

Proteção a BOA: cada BOA do conjunto tem omissões legítimas (motivo, personagem, passado). Pelo teste 2 elas continuam A e não geram exigência. O risco é o Crítico tratar um mecanismo bom como falho. Por isso o teste 3 pede trecho citado e a explicação de por que a relação não funciona; sem isso, vira observação descartada.

Estabilidade (decisão 5): em vez de mais execuções, a v2.3 propõe substituir o julgamento de tolerância por perguntas com resposta citável e uma regra de veredicto mecânica. Isso não garante concordância entre execuções. Só uma validação nova mostrará se os 6 divergentes diminuem.

Limite declarado: Q06, Q10 e Q22 estão contaminados e não servem como prova de melhoria. Uma validação futura exige conjunto novo, com rótulos externos fixados antes e protocolo registrado, e a comparação direta v2.2 contra v2.3 nesse conjunto.

## Pendências para sua decisão

1. Aprovar, ajustar ou rejeitar a formulação do ajuste 3 antes de implementá-lo.
2. Autorizar o desenho do protocolo e do conjunto independente (sem executar nada antes disso).
