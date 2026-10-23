# v2.4-exp: resumo das diferenças em relação à v2.2 e à v2.3-exp

Data: 22/10/2026. Etapa G0. Rascunho para revisão de Eri. A v2.4-exp (prompts/critico_v2_4_exp.md) não foi executada, não está congelada e não é considerada superior: só resultados inéditos poderão mostrar isso. v2.2 e v2.3-exp permanecem inalteradas (SHA-256 468fd382… e 74bc6f3a…, verificados).

## 1. Quadro comparativo

| Aspecto | v2.2 | v2.3-exp | v2.4-exp |
|---|---|---|---|
| Base do veredicto | Defeitos de lista fechada, evidências E1 a E5 | Idem, mais Teste de Integridade e classes A a D | Integridade (passo 1) e mérito positivo (passo 2) separados, objeções com fundamento A, B ou C, regra de estado |
| Aprovar | E1 a E5 e nenhum defeito demonstrado | Idem, com B periférico | Quatro demonstrações positivas (segunda leitura, o que muda na foto, elemento específico, por que a objeção relevante não compromete) e teste de contribuição do gesto quando a associação comum se aplica |
| Mérito não demonstrado sem defeito | Não previsto (aprova se E1 a E5) | Não previsto | REVISAR se há núcleo promissor e intervenção localizada, senão REPROVADA com objeção estrutural fundamentada |
| Reprovar | Defeito estrutural ou eliminatória | Classe D ou eliminatória | Fundamento A estrutural, ou B com os três requisitos; C nunca |
| Objeção interpretativa (B) | Mistura com defeitos | Mistura com defeitos | Só bloqueia com argumento específico, confronto com a leitura favorável e demonstração de que atinge o núcleo; senão vira C |
| Preferências C | Não distingue | Não distingue | Declaradas como C; nunca decidem; C1 e C2 só aparecem como C |
| Defeito percebido e dispensado | Descarte livre | Descarte livre | Registrado como objeção periférica com justificativa em merito.por_que_nao_compromete |
| REVISAR | Defeito corrigível | Classe C | Exige o que preservar, a deficiência e a intervenção localizada |
| Divergência legítima | Ausente | Ausente | Condição registrada no campo divergencia_legitima (material só entre APROVADA e outro estado); não é um quarto veredicto |
| Plausibilidade física | Procedimento de contradição | Idem | Mesmo procedimento, mais a regra da interpretação mais natural e da intenção que não substitui o mecanismo |
| Previsão cega | Auxiliar | Auxiliar com corroboração separada | Auxiliar; também serve de evidência da leitura inicial quando as três coincidem; nunca defeito |
| Campos de saída (contando a instrução de revisão, condicional) | 19 | 21 | 22 (sai: evidencias_positivas, defeitos_demonstrados, eliminatorias, nota; entram: leitura_inicial, merito, objecoes, nucleo, divergencia_legitima) |

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

## 3. Escolhas minhas que exigem sua atenção

Declaro porque nem tudo está literalmente nas decisões e você pode vetar:

1. Teste de contribuição do gesto (retirar o detalhe e ver se a leitura convencional sobra). É a forma operacional que dei à sua decisão de que o gesto precisa contribuir significativamente. Não é um critério novo, mas é uma operacionalização.
2. Leitura inicial ancorada nas previsões cegas, quando coincidem. É a resposta ao diagnóstico de que a "leitura inicial" do Crítico não coincidia com a dos leitores. Pode reintroduzir peso de previsibilidade. A previsão continua proibida como defeito e como justificativa isolada de qualquer objeção.
3. Remoção de E1 a E5 e do campo nota. A função de E1 e E5 passa ao mérito, a de E2 a E4 à integridade. Removi a nota por ser pontuação de desempate sem função. A remoção reduz comparabilidade direta de campos com as versões anteriores; as comparações usam o veredicto e as justificativas.
4. Fundamento por categoria. Atribuí cada categoria a A, B ou a ambos. Distribuição é minha, derivada da sua descrição dos fundamentos.
5. O campo divergencia_legitima pode virar escudo (declarar divergência para não decidir). Mitiguei exigindo duas interpretações fundamentadas e limitando a divergência material a APROVADA contra outro estado; o protocolo de análise acompanha a taxa.

## 4. Riscos que antevejo

- Mais campos de saída podem aumentar a variância entre execuções, como aconteceu da v2.2 para a v2.3-exp. Não sei se a regra de estado, mais mecânica, compensa isso.
- O Crítico pode preencher os quatro elementos de mérito em tom fluente para aprovações indevidas. O julgador de motivos e a auditoria humana existem para isso, mas é o risco central ("aparência de profundidade").
- O requisito B pode ser cumprido apenas na forma, com uma "leitura alternativa" curta e conveniente. O validador emite aviso para leituras muito curtas, mas não julga qualidade.
- Pode haver subcorreção da fronteira B/C: objeções reais virarem C por faltar um requisito escrito, e passarem. Ou superaplicação: B bloqueando boas propostas. Só dados inéditos mostrarão em que direção.
- O prompt é mais longo que o da v2.3-exp, o que pode afetar a atenção do modelo.

## 5. O que não foi feito

Candidata não executada em nenhum item, real ou sintético. Nenhum teste com novos itens. O validador foi testado só com avaliações escritas à mão. Nada foi ajustado em função dos itens de validação, que não existem.
