# Relatório 2: teste controlado de J06 e comparação cega das revisões

Data: 22/10/2026. Fase A, só texto. Crítico v2.1 e veredictos originais inalterados (SHA-256 do prompt e dos gabaritos conferidos). Decisões externas registradas em decisoes_externas.json.

## 1. Decisões externas sobre as revisões anteriores

- J15-r1: AMBÍGUA, publicação não autorizada (inconsistência da arrumação às sextas, mais difícil de entender, ganhou imprevisibilidade e perdeu naturalidade). O Crítico tinha dado APROVADA (nota 80).
- J01-r2: RUIM, descarte mantido (perdeu o contraste da original e virou reflexão sobre desacelerar). O Crítico tinha dado REVISAR (nota 66), ou seja, já a barrava.

## 2. J06: experiência controlada (só a foto mudou)

- NA FOTO e FORA preservados literalmente. Foto original: "...uma mão com o dedo pousado na coluna da direita...". Foto corrigida: "...uma mão em repouso sobre a toalha ao lado do cardápio...". Filtros sem falhas.
- Três previsões cegas novas (nenhuma reaproveitada): duas foram para "sozinha esperando alguém que não chega" e uma para "vai encerrar algo e ensaia o que dirá". Nenhuma chegou ao preço. Grau: "não previu".
- Crítico v2.1 em contexto limpo: REVISAR, nota 62 (antes REPROVADA, nota 18). Falhou só em E5: a revelação é a piada conhecida de olhar o preço primeiro; o único detalhe próprio é "da direita para a esquerda"; não diz diante de quem ela finge; a mão em repouso não participa da ideia. Instrução: acrescentar um fato específico (para quem ela encena o gosto, o que faz depois).
- Leitura: a eliminatória "foto que entrega" caiu, mas a de clichê permaneceu na forma de falha em E5. A imprevisibilidade conquistada pela foto nova não virou originalidade, o que confirma o princípio de não confundir as duas. O dedo na coluna era também o gancho visual que ligava a foto ao texto: sem ele, o FORA parece desconectado do que se vê. Pela triagem aprovada, J06 se enquadra no caso 1 (elemento visual dispensável) e a correção controlada foi usada uma vez, sem recuperação. Resultado: não aprovada, não presumida. Um novo ciclo exigiria mexer no FORA, o que a experiência proibia.
- Conclusão sobre o falso negativo: a reprovação original não era só excesso de peso na previsibilidade nem só defeito de foto. O núcleo da ideia, tal como escrito, continua sendo a associação comum. A divergência com a classificação externa BOA persiste como diferença de critério (a classificação externa valoriza o fingimento e a situação social; o Crítico exige perspectiva além do hábito conhecido).

## 3. Comparação cega entre original e revisada

Dois comparadores independentes, ordem A/B sorteada em cada um, sem veredictos, sem saber qual era a original.

| Par | Comparador 1 | Comparador 2 | Externo |
|---|---|---|---|
| J15-r1 | revisada melhor, real, publicável | revisada melhor, real, publicável | AMBÍGUA |
| J01-r1 | revisada melhor, real, não publicável | revisada melhor, real, publicável | não avaliado |
| J01-r2 | revisada melhor, real, publicável | equivalentes, não real, não publicável | RUIM |
| J06 foto corrigida | original (com dedo) melhor, não publicável | original melhor, publicável | não avaliado |

Observações:
- Nenhum comparador apontou defeito novo na J15-r1, que a avaliação externa considerou menos natural e com inconsistência nas sextas. É um ponto cego real: o Critério 7 (não aceitar revisão que troca um defeito por outro) não foi detectado por modelo nenhum aqui, e só a leitura externa o viu.
- Em J01-r2, um comparador achou a revisada melhor e publicável, e o externo disse RUIM. O outro comparador, que achou equivalentes e apontou "minutos ganhos pouco plausível" e "fez a conta" vago, ficou mais perto do externo.
- Em J06 os dois comparadores preferem a foto original, o que mostra o custo de remover o gancho visual.
- Os comparadores tendem a preferir a versão mais elaborada. Ambos são o mesmo tipo de modelo do Criador e do Crítico.

## 4. Diagnóstico: o sistema distingue revisão melhor de reformulação?

- Contenção: sim. O Crítico barrou J01 duas vezes, e J06-f1 e J01-r2 não passaram. Nenhuma revisão fraca foi aprovada que a avaliação externa já tivesse rejeitado como RUIM.
- Recuperação: não demonstrada. Das 3 revisões deste ciclo (J15-r1, J01-r2, J06-f1) nenhuma foi ao mesmo tempo aprovada pelo Crítico e aceita externamente. J15-r1 é a única aprovada pelo Crítico e foi vista como AMBÍGUA, isto é, melhor que a original em originalidade, mas com novo defeito de naturalidade.
- Falha específica a corrigir antes de confiar no mecanismo: a detecção de defeito introduzido pela revisão (plausibilidade interna do ritual, no caso das sextas). Nem o Crítico nem os comparadores a pegaram. Não foi alterado o Crítico; a lacuna fica registrada.
- Uma comparação cega por modelo não substitui a leitura externa: tem viés a favor da versão mais elaborada.

## 5. Limitações

Amostra de 3 revisões; classificação externa de um único avaliador; todos os agentes são o mesmo tipo de modelo; J06 testou uma só correção, só da foto.

## 6. Decisões que cabem a Eri e ao ChatGPT

1. Se a lacuna de detecção de defeito introduzido justifica uma etapa extra de verificação (por exemplo, um leitor cego que só procura inconsistências lógicas na versão revisada) antes de qualquer nova calibração.
2. Se J06 deve ser encerrada aqui ou reaberta como nova candidata com FOTO e FORA reescritos.
3. Se o mecanismo de revisão deve permanecer em teste, sem uso em produção, até haver ao menos algumas recuperações aceitas externamente.
