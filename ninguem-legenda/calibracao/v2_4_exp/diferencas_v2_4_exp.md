# v2.4-exp: resumo das diferenças em relação à v2.2 e à v2.3-exp (revisão 1)

Data: 22/10/2026. Etapa G0. Revisão 1, conforme as decisões de Eri de 23h55, para nova revisão antes do M1. O texto literal das mudanças em relação ao rascunho anterior (commit 0bd077f) está em alteracoes_rev1_prompt.diff, alteracoes_rev1_julgador.diff e alteracoes_rev1_validador.diff, nesta pasta; a seção 6 abaixo as resume. A v2.4-exp (prompts/critico_v2_4_exp.md) não foi executada, não está congelada e não é considerada superior: só resultados inéditos poderão mostrar isso. v2.2 e v2.3-exp permanecem inalteradas (SHA-256 468fd382… e 74bc6f3a…, verificados).

## 1. Quadro comparativo

| Aspecto | v2.2 | v2.3-exp | v2.4-exp |
|---|---|---|---|
| Base do veredicto | Defeitos de lista fechada, evidências E1 a E5 | Idem, mais Teste de Integridade e classes A a D | Integridade (passo 1) e mérito positivo (passo 2) separados, objeções com fundamento A, B ou C, regra de estado |
| Aprovar | E1 a E5 e nenhum defeito demonstrado | Idem, com B periférico | Quatro demonstrações positivas (segunda leitura, o que muda na foto, elemento específico, por que a objeção relevante não compromete) e, quando a associação comum se aplica, explicação de qual contribuição o gesto oferece e se basta para o mérito (não eliminatória) |
| Mérito não demonstrado sem defeito | Não previsto (aprova se E1 a E5) | Não previsto | REVISAR se há núcleo promissor e intervenção localizada, senão REPROVADA com objeção estrutural fundamentada |
| Reprovar | Defeito estrutural ou eliminatória | Classe D ou eliminatória | Fundamento A estrutural, ou B com os três requisitos; C nunca |
| Objeção interpretativa (B) | Mistura com defeitos | Mistura com defeitos | Só bloqueia com argumento específico, confronto com a leitura favorável e demonstração de que atinge o núcleo; se a falha parece real e o Crítico não consegue demonstrar, registra gravidade nao_demonstrada, sem rebaixar a C |
| Preferências C | Não distingue | Não distingue | Declaradas como C; nunca decidem; C1 e C2 só aparecem como C |
| Defeito percebido e dispensado | Descarte livre | Descarte livre | Registrado como objeção periférica com justificativa em merito.por_que_nao_compromete |
| REVISAR | Defeito corrigível | Classe C | Exige o que preservar, a deficiência e a intervenção localizada |
| Divergência legítima | Ausente | Ausente | Condição registrada no campo divergencia_legitima (material só entre APROVADA e outro estado); não é um quarto veredicto |
| Plausibilidade física | Procedimento de contradição | Idem | Mesmo procedimento, mais a regra da interpretação mais natural e da intenção que não substitui o mecanismo |
| Previsão cega | Auxiliar | Auxiliar com corroboração separada | Auxiliar; pode informar a leitura inicial mais plausível, com a ressalva de que três leitores do mesmo modelo não são observações humanas independentes; o Crítico pode justificar outra leitura inicial; nunca defeito |
| Campos de saída (contando a instrução de revisão, condicional) | 19 | 21 | 23 (sai: evidencias_positivas, defeitos_demonstrados, eliminatorias, nota; entram: leitura_inicial, merito, objecoes, nucleo, divergencia_legitima, elegibilidade_automatica) |

## 2. Origem de cada mudança nas decisões consolidadas

| Mudança | Fonte |
|---|---|
| Integridade e mérito separados; ausência de defeitos não comprova excelência | Eri, 22/10 (referência editorial, decisão 4) |
| Fundamentos A, B e C; B com três requisitos; C nunca reprova | Eri, 22/10 (decisões 3 e 6 da referência) |
| Quatro demonstrações para APROVADA; simetria de rigor sem inventar objeções | Eri, 22/10 (revisão 2 da referência, decisão 2) |
| REVISAR com preservar, deficiência e intervenção; REVISAR não é depósito | Eri, 22/10 (decisão 1 da revisão 2) |
| Mérito não demonstrado: REVISAR ou REPROVADA conforme o núcleo | Eri, 22/10 (mesma decisão) |
| Divergência material só entre APROVADA e outro estado; condição, não veredicto | Eri, 22/10 (decisões 1 e 3) |
| Convencionalidade não é motivo automático; o gesto deve contribuir significativamente; sequência, custo e ausência de metáfora não são requisitos | Eri, arbitragem de 22/10 (decisão 5) |
| Interpretação mais natural da ação; intenção não substitui mecanismo | Eri, arbitragem de 22/10 (decisão 6) |
| Preferências C1 e C2 só como C | Eri, 22/10 (registro de preferências C) |
| Não acrescentar agentes, pontuações ou critérios novos | Eri, 22/10 (várias decisões, e a decisão 2 de hoje) |

## 3. Escolhas minhas, com a decisão de Eri de 22/10 (23h55)

1. Teste de contribuição do gesto: APROVADO COM AJUSTE. Deixa de ser teste binário de retirada hipotética. O Crítico explica qual contribuição o gesto oferece e se é suficiente para justificar mérito; manter parte da segunda leitura sem o gesto não é insuficiência por si; não vira exigência de sequência temporal, arrependimento, comportamento incomum ou custo físico.
2. Leitura inicial e previsões cegas: APROVADO COM RESSALVA. As previsões informam a leitura inicial mais plausível, mas três leitores do mesmo modelo não são três observações humanas independentes e sua concordância não determina o que todo leitor faria. O Crítico pode justificar outra leitura inicial com fundamento na foto e no NA FOTO, e não pode aceitar uma leitura artificialmente ingênua. Previsibilidade continua não sendo defeito.
3. Remoção de E1 a E5 e do campo nota: APROVADA. Perda de comparabilidade documentada na seção 5.
4. Fundamento por categoria: APROVADA como organização inicial, com salvaguarda. A categoria não determina o fundamento: a natureza e a qualidade da demonstração decidem. Uma falha real não é rebaixada a C por o Crítico não ter escrito os três requisitos de B; fica como "nao_demonstrada", tratada como insuficientemente demonstrada.
5. Divergência legítima como escudo: exigência de duas interpretações fundamentadas mantida e acrescida de avaliação qualitativa das divergências e de apresentação dos itens em que a candidata alterou a elegibilidade automática em relação ao veredicto bruto (protocolo, seção 2). Não basta monitorar a taxa.

## 4. Riscos que antevejo

- Mais campos de saída podem aumentar a variância entre execuções, como aconteceu da v2.2 para a v2.3-exp. Não sei se a regra de estado, mais mecânica, compensa isso.
- O Crítico pode preencher os quatro elementos de mérito em tom fluente para aprovações indevidas. O julgador de motivos e a auditoria humana existem para isso, mas é o risco central ("aparência de profundidade").
- O requisito B pode ser cumprido apenas na forma, com uma "leitura alternativa" curta e conveniente. O validador emite aviso para leituras muito curtas, mas não julga qualidade.
- Pode haver subcorreção da fronteira B/C: objeções reais virarem C por faltar um requisito escrito, e passarem. Ou superaplicação: B bloqueando boas propostas. Só dados inéditos mostrarão em que direção.
- O prompt é mais longo que o da v2.3-exp, o que pode afetar a atenção do modelo.

## 5. O que não foi feito

Candidata não executada em nenhum item, real ou sintético. Nenhum teste com novos itens. O validador foi testado só com avaliações escritas à mão. Nada foi ajustado em função dos itens de validação, que não existem.

## 5. Perda de comparabilidade (decisão 8)

A v2.4-exp não tem evidencias_positivas, defeitos_demonstrados, eliminatorias e nota, e acrescenta leitura_inicial, merito, objecoes, nucleo, divergencia_legitima e elegibilidade_automatica. Os campos antigos e os novos não se comparam diretamente. A comparação entre versões é feita por veredictos brutos, decisões de elegibilidade e justificativas verificáveis (julgador e auditoria humana).

## 6. Registro das alterações da revisão 1 (cada decisão de 22/10, 23h55)

| Decisão de Eri | Alteração |
|---|---|
| 1. Controles especiais mantidos | Protocolo, seção 5.3: lote independente posterior, regras congeladas antes da produção, fora dos 30 mais 30, sem eliminar a dimensão 6; sem eles a conclusão fica em A |
| 2. Limiar de 80% de motivos CORRETOS | Protocolo, seção 5.1: quatro categorias separadas; 80% de CORRETO entre as conclusivas em cada amostra, com melhora sobre o controle; PARCIAL à parte; justificativas claramente falsas destacadas; julgador não auditado torna a dimensão INCONCLUSIVA. Substitui "70% corretos ou parciais" |
| 3. Divergência material | Protocolo, seção 2: dois registros (veredicto bruto e elegibilidade automática); campo elegibilidade_automatica no prompt e no validador; 20% como alarme exploratório; monitoramento por estrato |
| 4. Critério de melhoria | Protocolo, seção 4: removida a regra da maior oscilação; prioridades 1 a 7; oscilação como evidência de instabilidade; critérios simétricos |
| 5. Reprovação indevida de BOA | Protocolo, seções 3, 4 e 6: camadas 1 e 3 separadas, sem compensação, piora grave em qualquer uma impede a conclusão B |
| 6. Contribuição do gesto | Prompt, passo 2: explicação da contribuição, sem teste binário nem exigências de sequência, arrependimento, incomum ou custo físico |
| 7. Previsões e leitura inicial | Prompt, passo 2 e T1: ressalva sobre leitores do mesmo modelo; outra leitura inicial permitida; sem leitura ingênua; previsibilidade não é defeito |
| 8. Remoção de E1 a E5 e nota | Seção 5 deste documento e protocolo, seção 7 |
| 9. Fundamentos A, B e C | Prompt, passo 3: categoria não determina fundamento; gravidade "nao_demonstrada" com "lacuna"; validador sem restrição entre categoria e fundamento |
| 10. Divergência como escudo | Prompt, passo 5; protocolo, seção 2 (avaliação qualitativa e itens em que a elegibilidade foi negada); julgador, passo 5 |
| 11. Julgador | Categorias em maiúsculas e separadas; verificação contra a foto prevista e o texto; termos da referência não tornam a justificativa correta; argumento fluente sem fundamento narrativo não é mérito; verificação das divergências; marcação de justificativa claramente falsa |
| 12. Limites | Nada executado, sorteado, gerado ou congelado; sem v2.5, sem novas categorias de defeito nem agentes. Acrescentei apenas dois valores de campo exigidos pelas decisões: gravidade "nao_demonstrada" (decisão 9) e o campo elegibilidade_automatica (decisão 3) |
