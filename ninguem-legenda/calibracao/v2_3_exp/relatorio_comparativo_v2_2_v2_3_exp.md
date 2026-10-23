# Relatório comparativo: Crítico v2.2 contra v2.3-exp (conjunto W01 a W30)

Data: 22/10/2026. Fase A. Protocolo executado como pré-registrado (protocolo_validacao_v2_3_exp.md). Rótulos externos fixados antes (SHA-256 6dc6f015...06dd6, commit 8531a5e). Prompts, rótulos, itens e critérios não foram alterados durante nem depois da execução. A v2.3-exp NÃO foi homologada e este relatório não propõe v2.4.

Execuções: 3 previsões cegas por item; 2 execuções da v2.3-exp e 2 da v2.2, em contextos isolados, códigos e ordem diferentes em cada uma. Validador: 0 inconsistências em 120 avaliações. Nenhuma falha técnica ocorreu nas execuções; a única limitação metodológica registrada é a do julgador de motivos (seção 7). Matriz completa dos 30 itens: conjunto/resultados/matriz_30_itens.md. Dados brutos: conjunto/resultados/.

## 1. Conclusão em poucas linhas

Não há evidência de melhoria real da v2.3-exp sobre a v2.2 neste conjunto. Ambas preservam todas as BOA e ambas aprovam RUIM. A v2.3-exp ficou menos consistente entre execuções, perdeu uma detecção correta de AMBÍGUA (W30) e uma de RUIM (W25) por classificar como periférica (B) uma falha que a avaliação externa considera central, e produziu justificativas menos coincidentes com o motivo editorial real. O único ganho nítido é o ajuste 1: nenhum defeito de clichê ou redundância da v2.3-exp se apoia na previsão fora da frase de corroboração, o que acontecia na v2.2.

## 2. Resultados nas medidas pedidas (por execução, sem agregar)

Rótulos externos: 10 BOA, 4 AMBÍGUA, 16 RUIM.

| | v2.2 e1 | v2.2 e2 | v2.3 e1 | v2.3 e2 |
|---|---|---|---|---|
| 1. RUIM aprovada (de 16) | 6 | 2 | 4 | 2 |
| 2. BOA reprovada (de 10) | 0 | 0 | 0 | 0 |
| 3. BOA enviada a REVISAR | 0 | 0 | 0 | 0 |
| AMBÍGUA aprovada (de 4), contestável | 3 | 3 | 4 | 3 |
| RUIM em REVISAR em vez de REPROVADA | 2 | 6 | 8 | 7 |
| Não aprovados RUIM/AMBÍGUA com defeito que coincide com o motivo externo | 10 de 11 | 13 de 15 | 6 de 12 | 10 de 15 |
| Não aprovados com motivo só em parte | 1 | 1 | 3 | 4 |
| Não aprovados com motivo que não coincide | 0 | 1 | 3 | 1 |
| Itens com veredicto diferente entre as duas execuções | 4 (W08, W16, W17, W21) | | 8 (W03, W08, W09, W10, W11, W19, W21, W25) | |

Leitura sem percentuais:
- A diferença entre versões nas aprovações indevidas de RUIM (8 contra 6, somando as execuções) é menor do que a diferença entre duas execuções da mesma v2.2 (6 contra 2). Não sustenta que uma versão seja melhor.
- W15 foi aprovado nas quatro execuções e W19 em três (REVISAR só na v2.3-exp e1). A justificativa externa de ambos é sentimentalismo convencional sobre ausência. As duas versões tratam isso como familiaridade legítima ("familiaridade não é clichê").
- W14 e W24 (AMBÍGUA) foram aprovados nas quatro execuções, e W09 em três. A falha apontada no W24 (relação entre instrumento, data e gesto depende de pressupostos) foi registrada pelas duas versões como "omissão legítima" (não se diz se o pai morreu). Aqui o Teste de Integridade não alterou o julgamento.
- BOA: nenhuma versão reprovou ou mandou para revisão um item BOA. Na v2.3-exp, nove observações classe B aparecem em itens BOA (W02, W05, W12, W13, W20, W29) sem bloqueio; são modestas e coerentes com o texto.

## 3. Fronteira B/C (decisão 3)

Casos em que o Crítico classificou como periférica (B) uma falha que a avaliação externa considera central:

| Execução | Item | Rótulo | O que o Crítico registrou como B | Motivo externo | Por que é central |
|---|---|---|---|---|---|
| v2.3 e1 | W08 | RUIM | "Lavar não preserva o cheiro dele, apenas dá cheiro de roupa limpa; a leitura poética sustenta." | Lavar remove o vestígio que se quer conservar | É o mecanismo da história; a "leitura poética" é o resgate artificial que a decisão 4 manda não aceitar |
| v2.3 e1 | W21 | RUIM | "O carregador espera o celular, não a bateria; não compromete." | A referência à bateria não estabelece relação precisa | É a frase final da revelação |
| v2.3 e1 | W25 | RUIM | "Enumeração genérica que a foto já sugere; sem peso." | Revelação genérica, sem informação sobre a data | É a revelação inteira; as duas execuções da v2.2 reprovaram o item por isso |
| v2.3 e1 | W30 | AMBÍGUA | "Casa sem ovos e café por meses é pouco literal; lê-se como itens da lista não repostos." | Permanência da falta enfraquece a plausibilidade literal | Mesmo problema que a v2.2 classificou como defeito nas duas execuções |
| v2.3 e2 | W30 | AMBÍGUA | Idem | Idem | Idem |

Em todos, o Crítico reconheceu a imperfeição e a demonstrou, mas usou a classe B para dispensá-la com uma frase ("não compromete", "a leitura poética sustenta") sem demonstrar a ausência de efeito na segunda leitura. A regra de materialidade exige demonstrar a importância do defeito; ela não exige demonstrar a irrelevância do que foi rebaixado a B. Esse é o ponto exato que Eri antecipou. Em W30 e W25 a v2.3-exp ficou pior que a v2.2 nas duas direções que importam: onde a v2.2 acertou, a v2.3-exp aprovou.
Contraponto honesto: em W09 (e2), a v2.3-exp demonstrou redundância com a foto (parede recém-pintada ao redor) e clichê dos riscos de altura, ambos com demonstração independente e corroboração separada, e acertou o motivo externo. A v2.2 aprovou W09 nas duas execuções.

## 4. Caso W08 (decisão 4)

- v2.2 e1 aprovou, registrando a tensão ("lavar tira o cheiro dele") como observação descartada. v2.2 e2 mandou REVISAR por clichê, citando a incompatibilidade como segunda razão (correspondência em parte).
- v2.3-exp e1 identificou a incompatibilidade material e a rebaixou a B com uma interpretação alternativa ("cheiro de roupa limpa", "leitura poética"), que é a solução artificial que a decisão 4 manda não aceitar. v2.3-exp e2 reconheceu a mesma incompatibilidade, expressou-a como ambiguidade entre "cheiro dele" e "cheiro de roupa limpa" e mandou REVISAR (correspondência em parte; o julgador não a considerou mesma questão por tratar como ambiguidade e não como mecanismo que se anula).
- Nenhuma das quatro execuções produziu defeito da categoria "contradicao" em qualquer item. O procedimento do ajuste 2 (alternativa natural) não foi acionado no conjunto, então seu efeito não pôde ser medido. Nenhuma execução reprovou o W08. Nenhuma versão resolve o caso de forma consistente.

## 5. Consistência entre execuções

- v2.2: 4 itens divergentes, todos RUIM, todos entre APROVADA e REVISAR (W08, W16, W17, W21).
- v2.3-exp: 8 itens divergentes. Cinco entre aprovar e não aprovar (W08, W09, W19, W21, W25), três entre REVISAR e REPROVADA (W03, W10, W11).
- A v2.3-exp ficou menos estável. A regra mecânica de veredicto (C leva a REVISAR, D a REPROVADA) transfere a instabilidade para a decisão entre C e D e entre B e C. O alerta pré-definido (divergência maior que a da v2.2) disparou.

## 6. Qualidade das justificativas (decisão 7)

Julgamento por agente isolado, sem rótulo e sem veredicto, em 84 defeitos. Acertos pelo motivo errado, não contados como acerto pleno:
- W01, v2.3-exp e1: REPROVADA apenas por "repeticao" de texto anterior (cadeira de balanço), sem apontar o sentimentalismo que a avaliação externa aponta. Veredicto correto, motivo editorial não coincide. v2.3-exp e2 e as duas da v2.2 incluíram também clichê ou sentimentalismo.
- W11, v2.3-exp e1 e e2: redundância com a foto (e1) e repetição de texto anterior (e2), sem a razão externa (previsibilidade da ausência). As duas execuções da v2.2 apontaram também clichê.
- W27 (RUIM; referente de "ela sobrou" e causalidade): REVISAR nas quatro. Só a v2.2 e1 apontou a ambiguidade de referência (coincide); a v2.3-exp e2 coincide em parte; v2.2 e2 e v2.3-exp e1 citaram clichê, que não é o motivo externo.
- Soma dos acertos plenos entre os itens não aprovados: v2.2 e1 10 de 11; v2.2 e2 13 de 15; v2.3 e1 6 de 12; v2.3 e2 10 de 15.
Pontos fortes preservados: nenhum defeito de clichê ou redundância da v2.3-exp cita a previsão fora da frase de corroboração (0 de 16). Na v2.2, 7 de 17 citam. O ajuste 1 funciona como desenhado.

## 7. Defeitos inventados ou insuficientemente demonstrados

- Nenhuma execução inventou defeito em item BOA (todas as BOA foram aprovadas sem defeito).
- O julgador marcou 16 defeitos como inválidos no texto, 13 deles por "não verificável". A causa é uma limitação do meu pacote para o julgador: ele recebeu o NA FOTO, o FORA e o motivo externo, mas não a descrição da foto nem os textos anteriores, necessários para checar redundância com a foto e repetição. Verifiquei por mim as alegações de redundância com a foto em W09, W10, W17 e W21 contra a descrição da foto prevista, e todas procedem; W25 procede em parte (papéis e lista de compras aparecem na foto). Não reexecutei o julgador, para não ajustar o procedimento depois dos resultados. Conclusão correta: a contagem de "defeitos inventados" pelo julgador não é confiável e não deve ser citada; não encontrei defeito inventado nas verificações manuais.

## 8. Ganhos e perdas reais da v2.3-exp em relação à v2.2

Ganhos: ajuste 1 efetivo (previsão não constitui defeito); integridade narrativa produziu uma detecção que a v2.2 não fez (W09 e2, com demonstração independente).
Perdas: W30 e W25 aprovados pela v2.3-exp onde a v2.2 acertou o defeito; menor estabilidade (8 contra 4 divergências); mais RUIM em REVISAR em vez de REPROVADA (8 e 7 contra 2 e 6); menos acertos plenos de motivo; custo maior (execuções de 229 a 245 segundos contra 185 a 222, e cerca de 5% a mais de tokens), com o campo de integridade preenchido em todo item e sem benefício medido em decisão.
Sem diferença: BOA preservadas nas duas; W14, W24, W15 aprovados em todas; W08 sem solução em nenhuma.
Complexidade: a v2.3-exp acrescenta seis perguntas e quatro classes por item. Neste conjunto, o acréscimo não reduziu aprovações indevidas nem melhorou consistência. Não há ganho demonstrado que justifique a complexidade adicional.

## 9. Falha comum às duas versões, observada sem propor correção

As duas versões aprovam sistematicamente histórias de ausência sentimental com gesto objetual (W15, W19, parcialmente W08, W21, W16, W17), tratando-as como familiaridade legítima. A avaliação externa as considera clichê sentimental. Pode ser que a distinção "familiaridade não é clichê" proteja BOA e ao mesmo tempo permita essas aprovações; este conjunto não separa as duas hipóteses. Não proponho alteração.

## 10. Limitações

As três origens dos itens são o mesmo modelo, com instruções diferentes, o que não garante independência criativa. Um único avaliador externo, também um modelo, cujo rótulo de W15 e W19 repousa em previsibilidade e não em defeito de texto. Apenas 4 itens AMBÍGUA, o que torna pouco poderoso o teste da fronteira B/C. Cada versão foi executada duas vezes; a variação entre execuções da v2.2 (RUIM aprovada 6 e 2) mostra que duas execuções são pouco para comparar versões. O julgador de motivos teve pacote incompleto (seção 7). O mapa de origens (O1, O2, O3) ainda não foi aberto para análise por origem; abri-lo só altera a leitura por origem, não os veredictos.

## 11. Estado

Nada foi alterado em prompts, rótulos, itens ou critérios. Sem imagens, créditos, grade, n8n, fila, publicações ou skills. Nenhuma versão homologada. Decisão sobre próximos passos fica com Eri.
