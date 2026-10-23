# Alterações da v2.3-exp em relação à v2.2

Data: 22/10/2026. Texto consolidado em prompts/critico_v2_3_exp.md. A v2.2 (prompts/critico_v2_2.md, SHA-256 468fd3823f83909d...) permanece inalterada. Diff literal em alteracoes_prompt.diff; hash da v2.3-exp em prompt_travado.sha256. Nada foi executado.

## 1. Previsões cegas (decisão 1 de 22/10)
- Previsão, mesmo unânime, nunca constitui sozinha cliche_efetivo, redundancia ou falta de originalidade.
- Esses defeitos exigem demonstração narrativa independente, escrita sem citar as previsões. A previsão só entra depois, numa frase iniciada por "Corroboração:".
- Teste: sem a frase de corroboração a demonstração deve se sustentar; senão o defeito vai para observacoes_descartadas.
- T1 reescrito: previsão é apenas corroboração.

## 2. Contradição (decisão 2)
- Antes de apontar, o Crítico escreve a interpretação alternativa mais natural. Se for plausível e natural, não há contradição.
- Interpretação meramente possível, mas artificial ou muito improvável, não salva o texto. A incompatibilidade precisa ser demonstrada com o próprio conteúdo.
- A demonstração leva "Alternativa natural:" e "Por que não vale:".

## 3. Teste de Integridade Narrativa (decisão de 22/10, versão refinada por Eri)
Substitui a seção "Informação implícita não é defeito automático" da v2.2.
- Seis perguntas respondidas no novo campo integridade: transformação central; relação sustentadora; implícitos; necessidade dos ausentes; plausibilidade sem invenção; efeito na segunda leitura.
- Quatro classes: A omissão legítima (não é defeito, vai para observacoes_descartadas); B imprecisão periférica (novo campo imprecisoes_perifericas, sem bloqueio); C imprecisão central corrigível (defeito, REVISAR); D obscuridade estrutural (defeito, REPROVADA).
- Regra de materialidade: não bloquear por imperfeição periférica; a importância concreta do defeito deve ser demonstrada.
- Cada defeito: trecho, relacao_comprometida, demonstracao, gravidade, justificativa_veredicto, mais classe C ou D. Afirmações vagas ("falta contexto", "a relação não está clara") sem demonstração não são aceitas.
- Veredicto mecânico: D ou eliminatória gera REPROVADA; senão C gera REVISAR; senão só A e B, aprova se E1 a E5.
- Preservação da sutileza escrita no prompt: não exigir motivação explicada, identificação completa nem causa explícita de todo acontecimento.
- Distinção operacional: lacuna é o texto calar algo; imprecisão é o texto afirmar algo que não fecha.

## Ferramentas
- validar_avaliacao.py: novo modo "v2.3-exp" (v2.1 e v2.2 idênticos; reverificado: 0 de 24 inconsistências nas três avaliações anteriores). calibracao/v2_3_exp/teste_validador.py: 12 testes sintéticos, todos passam. Avisos: demonstração vaga curta; cliché ou redundância parecendo apoiado só na previsão.
- Sem novos agentes: a v2.3-exp continua sendo um único Crítico, com as mesmas entradas da v2.2.

## Pontos que o refinamento deixa em aberto (para sua análise)
- A classe B não bloqueia. Se o Crítico classificar como B uma falha que o avaliador externo vê como central, a permissividade pode continuar. A fronteira B/C é o ponto de maior risco, e é onde mais haverá divergência entre execuções.
- Q22 (VÓ antecipando o campo emocional) continua dependendo de redundância, não do teste de integridade.
- Sem convergência garantida entre execuções: a v2.3-exp tenta estabilizar por critérios citáveis, e isso só se mede em validação.
