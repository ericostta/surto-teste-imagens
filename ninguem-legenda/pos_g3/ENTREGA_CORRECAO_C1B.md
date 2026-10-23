# Entrega: correção de E1 e E5, candidata C1b, protocolo atualizado e minuta da Emenda 2

Data: 23/10/2026. Resposta à devolutiva técnica sobre a entrega A a D (commit 3bf8842). Nada foi executado, publicado, comprado ou homologado. Crítico v2.2 original, validador, registros de M1, G1, G2 e G3, skills, n8n, grade, fila, contador e publicação permanecem intocados. A C1 anterior fica preservada como histórico.

Arquivos novos em `pos_g3/intervencao/`: `critico_v2_2_c1b.md`, `diff_c1_para_c1b.diff`, `diff_v2_2_para_c1b.diff`, `PROTOCOLO_VERIFICACAO_C1B.md`, `EMENDA_2_MINUTA.md`.

---

## A. E1 revisada

Problema reconhecido na redação anterior: exigir que a transformação se apoiasse no que a foto e o NA FOTO "efetivamente mostram ou afirmam" excluía inferências legítimas, e o FORA existe justamente para revelar o que a imagem não traz.

Redação da C1b:

> A transformação precisa estar ancorada na cena: em algo que a foto ou o NA FOTO mostram, afirmam ou tornam plausivelmente inferível (um objeto, gesto, ausência, relação ou situação). Não precisa estar literalmente declarada: uma foto pode sugerir relações, ausências e significados sem explicitá-los, e o FORA existe justamente para revelar o que a imagem não traz. Inferência plausível e fundamentada é admissível.
>
> Distinga duas situações. (a) Inferência sustentada: você consegue apontar na cena ou no NA FOTO o elemento que torna a segunda leitura plausível, e essa leitura reorganiza o que se vê. (b) Interpretação sem sustentação: o FORA apenas contradiz a leitura que as previsões fizeram, ou impõe um sentido que nenhum elemento da cena sustenta nem torna plausível, de modo que a foto poderia ser trocada por outra sem perda. Só (b) não demonstra transformação. Contradizer uma previsão, por si só, não basta; contradizê-la de um modo que reorganiza a leitura da foto a partir de elementos da cena demonstra transformação.
>
> Registre em elemento_que_muda o elemento de ancoragem que você apontou. Se não consegue apontar nenhum, trate como (b). Não exija afirmação literal, explicação fechada, moral explícita ou declaração de intenção.

O critério de distinção é verificável: apontar o elemento da cena e dizer se a foto seria substituível. Não há campo novo na saída (o validador congelado exige o formato existente), por isso a ancoragem é registrada em `elemento_que_muda`.

## B. E5 revisada

Problema reconhecido: "se a transformação some sem o número, o número era ornamento" é uma inferência inválida. A remoção pode destruir o sentido justamente porque o elemento é indispensável, e a preservação do sentido também não prova, sozinha, superficialidade.

Redação da C1b:

> Detalhes particulares (números, idades, quantidades, durações, nomes de coisas) podem ser o próprio mecanismo da segunda leitura, como a contagem que sustenta um contraste ou a idade que muda quem a pessoa parece ser, ou podem apenas particularizar, soando específicos sem mudar a leitura da foto. Use o teste de remoção como instrumento diagnóstico, nunca como critério de reprovação: reescreva mentalmente o FORA sem o detalhe e compare.
> (1) Se a transformação desaparece, o detalhe pode ser o mecanismo, e a retirada de um elemento indispensável destrói o sentido por isso mesmo. Demonstre que relação com a cena o detalhe cria. Se demonstra, ele é funcional e não há defeito.
> (2) Se a transformação permanece intacta, o detalhe é dispensável, e dispensável não é defeito.
> (3) Se, sem o detalhe, resta apenas a associação mais comum da categoria, pergunte se a especificidade é funcional (cria a segunda leitura) ou só particulariza (soa específica e a leitura é a mesma). Apenas no segundo caso, e com o trecho e a demonstração, há cliche_efetivo ou perda_segunda_leitura.
> O resultado do teste, sozinho, nunca justifica REVISAR nem REPROVADA, e nunca impede aprovação. Só vale como prova dentro de um defeito da lista, demonstrado como qualquer outro. Registre o que o teste mostrou e por que o detalhe sustenta ou não a transformação em observacoes_descartadas (funcional ou dispensável sem dano) ou em defeitos_demonstrados (demonstrado).

A Salvaguarda ganhou duas frases: "Informação numérica narrativamente funcional é legítima" e a proibição de usar os reforços para punir "números que sustentam a história".

Efeito esperado, dito sem rodeio: a nova E5 é mais fraca como freio do que a anterior, porque nada reprova mais por regra. O ganho, se existir, virá de E1 (a exigência de apontar o elemento da cena) e da demonstração obrigatória nos casos (1) e (3). Pode acabar sendo pequeno.

## C. Diff mínimo

`diff_c1_para_c1b.diff` (C1 anterior contra C1b) e `diff_v2_2_para_c1b.diff` (v2.2 contra C1b). Alterações: título e cabeçalho (identificação), E1, E5 e Salvaguarda. Nada mais muda no prompt: lista fechada de defeitos, testes T1 a T10, saída e instrução de revisão idênticos à v2.2.

## D. Protocolo de verificação atualizado

Detalhe em `PROTOCOLO_VERIFICACAO_C1B.md`. Resumo das mudanças:

1. **Números indispensáveis e decorativos de forma explícita.** Doze inéditas em cinco grupos: 3 de número indispensável, 3 de número decorativo, 2 de motivo declarado, 2 abertas a várias leituras, 2 de produção normal. A intenção do Criador não é o rótulo: você classifica às cegas a história (BOA, AMBÍGUA, RUIM) e o papel do número (FUNCIONAL, DECORATIVO, SEM DETALHE), e a análise agrupa pelas suas classificações.
2. **Proteção explícita.** Qualquer perda de BOA bloqueia o benefício; perda de BOA com número funcional é registrada à parte. Na regressão, Q8N9 (D31, "onze anos", "quatro") e QG3F (F26, "três vezes") são BOA com detalhe numérico, e QNB0 (D32, "onze") é AMBÍGUA com detalhe numérico. Já são casos reais de proteção, se você anotar o papel do número neles.
3. **Distinção entre ganho real e aumento artificial de reprovação.** Relato por versão dos veredictos não aprovados, separados por sua classe e pelo papel do número, mais leitura descritiva da causa de cada mudança (defeito, trecho, qual cláusula foi invocada). Aumento só em itens frágeis é ganho potencial; em itens BOA é perda.
4. **Quatro desfechos pré-registrados:** benefício claro, piora observada, sem benefício (evidência negativa) e inconclusivo. Inconclusivo cobre os casos em que o teste não podia decidir (menos de duas oportunidades, proteção numérica não testável ou falha técnica) e não amplia a amostra automaticamente.
5. **Mudança de custo:** 72 avaliações em vez de 60, porque a v2.2 também é reexecutada nas seis arbitradas, nas mesmas condições da C1b. Pendência para a sua decisão.

Probabilidade honesta de inconclusivo: a G3 sugere que a v2.2 aprova cerca de 70% dos itens AMBÍGUA. Com 3 itens frágeis nas doze, a chance de haver duas oportunidades é de cerca de 77%; com 2, 48%; com 1 ou nenhum, zero. Se você classificar menos de três como frágeis, o mais provável é inconclusivo. Estimativa grosseira.

## E. Riscos residuais e limitações

1. Avaliadores da mesma família de modelos que gera as histórias. Concordância entre eles não é confirmação independente, e a sua classificação também não é independente se houve conversa com ChatGPT.
2. Amostra de doze. Resultado é sobre itens, nunca taxa, e nunca generaliza para a produção futura. Os grupos de estresse não representam a produção real.
3. Subjetividade do papel do número. "Funcional" e "decorativo" dependem do seu julgamento, e dois leitores razoáveis podem divergir. O Crítico também terá de julgar isso, e pode racionalizar nas duas direções com igual fluência: a exigência de demonstração reduz esse risco, não o elimina.
4. A ancoragem de E1 pode ser satisfeita de modo trivial (nomear qualquer objeto da cena). A verificação mecânica só confirma que o campo está preenchido, não que a ancoragem é boa.
5. Ruído do próprio Crítico. A v2.2 mudou de veredicto em 5 de 60 itens entre execuções e o previsor mudou o número de capturas em 23 de 60. Duas execuções reduzem o problema, não o resolvem.
6. Poder reduzido pela correção: ao tornar E5 diagnóstica, a C1b pode simplesmente não mudar quase nada. Isso é um custo aceito da correção lógica.
7. Contaminação por construção: D04, F22 e D32 originaram a C1; a regressão confirma a mudança e não valida.
8. Efeitos não intencionais do texto adicional: a C1b é mais longa que a v2.2 e pode alterar comportamento de formas não previstas. A comparação direta com a v2.2 nas mesmas condições é o único controle.
9. Mesmo com benefício claro, a barreira contra AMBÍGUA continuaria dependendo de um único julgamento de modelo. Os portões G1, G2 e G3 simulados protegeram pouco, e a C1b não muda isso por si só. Autonomia total continua sem garantia de equivalência com o seu critério.
10. Desfecho inconclusivo é provável se houver poucos itens frágeis, e a regra proíbe ampliar a amostra sozinho. A decisão de continuar nesse caso é sua, com novo pré-registro.

## F. Minuta da Emenda 2

`EMENDA_2_MINUTA.md`: natureza, diferenças, tabela de hashes (a recalcular na publicação), entradas, referência, medidas e desfechos por referência ao protocolo, proibições, sequência de lacres e quatro pendências de decisão suas (contar RUIM como frágil; 72 em vez de 60 avaliações; anotar o papel do número nas seis; confirmar que inconclusivo encerra a rodada). Não foi publicada como emenda em vigor, e o script de verificação mecânica ainda não existe.

---

## O que não foi feito, por determinação

Nenhuma produção de história, nenhum Crítico executado, nenhum pacote para você, nenhuma emenda publicada, nenhuma promoção da C1b, nenhuma imagem, crédito ou integração, e nenhuma decisão sobre a posição na grade. Aguardo a sua análise da documentação corrigida.
