# Como operar o Crítico consultivo (piloto v0.1)

O Crítico do piloto é o v2.2 (references/critico_v2_2_referencia.md, cópia literal do prompts/critico_v2_2.md do laboratório, SHA-256 468fd382…). É referência PROVISÓRIA e CONSULTIVA. Nunca é portão automático: quem aprova é Eri.

## Procedimento
1. Rode os filtros determinísticos: `python3 scripts/filtros.py candidatas.json --registro registro_piloto.csv`. Falha dura elimina a candidata antes do Crítico (reescreva ou descarte).
2. Previsões cegas: use as ferramentas de agente, se existirem, para lançar TRÊS agentes novos e isolados, cada um instruído a ler apenas references/preditor_cego.md e um arquivo com (codigo, conceito_foto, na_foto) da candidata, SEM o FORA. Salve as três previsões. Sem ferramenta de agente, produza as três previsões você mesma, em sequência, declarando que NÃO são cegas de verdade (você conhece o FORA) e que isso enfraquece o teste.
3. Avaliação: um agente novo e isolado (ou, sem agentes, você mesma, declarando a perda de independência) lê apenas references/critico_v2_2_referencia.md e o pacote: codigo, conceito_foto, na_foto, fora, previsoes_cegas (3), textos_anteriores (vazio ou textos anteriores do registro). Nada mais: sem justificativa do Criador, sem tema, sem mecanismo.
4. A saída do Crítico é o JSON definido no prompt (versao_criterio "v2.2"). Traduza para Eri em poucas linhas: veredicto, as duas frases de justificativa, defeitos com trecho, e a instrução de revisão se REVISAR.
5. Isolamento é documental, não técnico, e o avaliador é da mesma família de modelos que cria. Diga isso quando relevante.

## Limitações conhecidas da v2.2 (declare sempre que apresentar um veredicto)
- Em experimento de laboratório (G3 reduzida, 60 itens, 4 execuções), a v2.2 aprovou nas quatro execuções histórias que Eri classificou depois como AMBÍGUA. APROVADA da v2.2 NÃO significa BOA.
- O veredicto oscilou entre execuções em parte dos itens. Uma única leitura é frágil.
- Padrões a observar por conta própria, como PERGUNTAS para Eri e nunca como veredicto: (a) detalhe numérico (número, idade, quantidade) que particulariza mas não muda a leitura da foto; (b) última oração que declara o motivo; (c) FORA que só desfaz a leitura que as previsões fizeram sem se apoiar em elemento da cena; (d) FORA que repete o NA FOTO. Detalhe numérico que é o próprio mecanismo da segunda leitura é legítimo.
- A candidata C1b (variação experimental do Crítico) NÃO faz parte do piloto, permanece isolada e não promovida. Não aplique suas regras como se fossem do Crítico.
- Divergência razoável de interpretação não é defeito. Se houver dúvida material sobre elegibilidade, apresente as interpretações em competição e deixe Eri decidir.

## O que dizer a Eri
APROVADA: "Crítico consultivo aprovou. Isso não garante BOA; segue sua decisão". REVISAR: defeito, trecho e correção mínima. REPROVADA: o defeito estrutural e, se houver, a nova candidata sugerida. Em qualquer caso, termine pedindo: aprovar, revisar ou descartar.
