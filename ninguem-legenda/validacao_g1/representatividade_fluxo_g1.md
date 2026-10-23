# Representatividade do fluxo: uma candidata por conceito (G1)

Data: 23/10/2026. Resposta à decisão 3 de Eri (00h21). Nada foi regenerado nem corrigido.

## 1. Como a candidata única foi obtida (fatos)

- A instrução experimental já determinava produzir uma só candidata. Cada prompt de geração (`geracao/prompts/G1-F01.md` a `G1-F30.md`, hashes no `registro_pre_geracao.json`, commitado antes de qualquer item existir) diz: "entregue UMA candidata (não três)". A mudança foi minha, feita para atender ao pedido de 30 candidatos, um por conceito sorteado.
- Cada subagente entregou exatamente um objeto JSON. Conferi nos 65 registros brutos: nenhuma saída tem mais de um objeto. Três saídas (F04, F05, F25) vieram dentro de bloco de código; extraí o JSON sem alterar o texto, e o bruto integral está em `brutos/`.
- Portanto não houve escolha entre candidatas. Não apliquei critério algum. A candidata entregue é a única que cada subagente devolveu. Não li as conversas internas dos subagentes, então não posso afirmar quantas ideias cada um considerou antes de responder.
- Nenhuma candidata foi refeita, filtrada ou substituída por qualidade. As únicas substituições foram as cinco exclusões técnicas por duplicata, todas no desafio.

## 2. Diferenças em relação ao processo normal

| Aspecto | Processo normal (`prompts/criador.md`) | Procedimento experimental da G1 |
|---|---|---|
| Candidatas por rodada | 3, com 3 mecanismos e 3 emoções diferentes | 1 por conceito, sem diversidade controlada na rodada |
| Foto | O Criador propõe o `conceito_foto` | Fluxo: conceito dado e fixo, vindo do sorteio. Desafio: o Criador propõe, com ambiente designado |
| Memória editorial | Lê as últimas 30 edições e atualiza o registro a cada rodada | Cada subagente leu o mesmo `registro.csv` (12 linhas de laboratório), sem atualização entre itens |
| Controle de repetição | Evita mecanismos, emoções e aberturas recentes | Nenhum controle entre itens, pois cada um foi gerado em contexto separado |
| Filtros determinísticos | Eliminam candidatas antes do Crítico | Rodados depois; só a duplicata de cena eliminou. G1-F08 falhou no filtro lexical e foi mantido |
| Seleção | O Crítico e os filtros selecionam | Nenhuma |
| Modelo | O do Criador de produção | Subagentes `sonnet`, uma instância por item |

## 3. Efeito observável no conjunto (descritivo)

Mecanismo: M01 em 36 dos 60 itens (15 de 30 no fluxo, 21 de 30 no desafio); os demais estão em M03, M12, M05, M08, M06, M10 e M02. Tipo de contraste: "pequeno_vs_grande" em 42 dos 60. Emoção mais frequente: "pequena_alegria" (19) e "cotidiano" (17). No processo normal a regra de 3 mecanismos diferentes por rodada e de evitar os recentes impede, em princípio, essa concentração. Isto é um fato do conjunto produzido, não um julgamento de qualidade.

## 4. Conclusão sobre representatividade

A amostra de fluxo não reproduz o processo normal. Representa uma variante específica dele: conceito fotográfico dado, uma candidata por conceito, geração independente, sem memória editorial atualizada, sem controle de diversidade entre itens, sem eliminação prévia por filtros e sem seleção. Ela é adequada para perguntar como o Crítico julga o que um Criador desse tipo produz sobre fotos dadas e de ambientes variados. Não autoriza generalizar para a produção diária. A concentração em M01 e em "pequeno_vs_grande" é uma limitação a declarar na leitura dos resultados. Não será corrigida por nova geração.

## 5. Denominação e uso (decisão de Eri, 23/10/2026, 00h27)

A amostra passa a ser chamada, em todos os relatórios, de **AMOSTRA DE FLUXO EXPERIMENTAL SIMPLIFICADO**. Seus resultados podem comparar os Críticos nesse conjunto e não podem ser apresentados como estimativa representativa da produção normal. A concentração em M01 (15 de 30 no fluxo; 36 de 60 no total) e em "pequeno_vs_grande" (42 de 60) fica registrada como limitação, sem correção por nova geração.
