# O QUE NINGUÉM LEGENDA: laboratório da Fase A

Série de @surtodelucidez. Foto + NA FOTO / FORA DO ENQUADRAMENTO, Stories 1080x1920.

## Escopo desta pasta (Fase A, só texto)

Esta pasta é um laboratório isolado. Nada aqui é lido pelo n8n.

Não toca: fila/, publicadas/, fila-eri/, fila-threads/, frases/, scripts/, agendamentos, skills existentes, créditos de imagem.

## Conteúdo

- config.json: limites e parâmetros experimentais (todos ajustáveis na homologação)
- taxonomia.json: mecanismos narrativos, emoções, vetos temáticos, regras de rosto
- registro.csv: memória editorial (estados, campos do DNA item 11)
- filtros.py: filtros determinísticos e comparação com o histórico
- prompts/criador.md: instruções do Criador (3 candidatas por rodada)
- prompts/critico.md: instruções do Crítico isolado (4 testes)
- lote/: candidatas, resultado dos filtros, avaliação do Crítico
- calibracao/: conjunto para Eri rotular (para_eri.md, sem veredictos) e gabarito do Claude (gabarito_claude.json). Quem rotula não deve abrir o gabarito antes de responder.
- registrar_lote.py: grava candidatas avaliadas no registro.csv (idempotente, sem número público)
- validar_avaliacao.py: confere a coerência interna das avaliações do Crítico (APROVADA exige E1 a E4, REVISAR exige instrução, REPROVADA exige eliminatória). Roda depois do Crítico e antes da seleção.
- prompts/critico.md é a versão v2.1 (critico_v1.md e critico_v2.md preservados). prompts/preditor.md é o leitor cego que prevê a revelação a partir da foto e do NA FOTO.
- calibracao/execucao_2/: pacotes, previsões, avaliações e mapas da segunda rodada. calibracao/conjunto2/: conjunto inédito, gabarito travado (gabarito_claude2.json e .sha256) e arquivo para Eri.
- calibracao/execucao_3/: três previsões cegas, pacotes e avaliações do v2.1. calibracao/conjunto2/gabarito_claude2_1.json (+ .sha256): veredictos v2.1 travados antes dos rótulos de Eri. relatorio_calibracao_3.md.
- calibracao/revisao_fase_a/: ciclo REVISAR de J01 e J15, análise de J06, auditoria das reprovações e relatorio_revisao.md.
- prompts/auditor_logico.md e calibracao/auditor_logico/: Auditor Lógico v1 (somente testes), protocolo, resultados e relatório.
- calibracao/revisao_fase_a/proposta_regra_revisar.md e decisoes_externas_3.json: proposta mínima da regra A/B/C (não implementada).
- prompts/critico_v2_2.md e calibracao/v2_2/: Crítico v2.2 EXPERIMENTAL (não homologado), alterações, protocolo de validação e conjunto inédito (aguardando rótulos externos).
- REVISAR nunca segue para imagem. Volta ao Criador (até 2 ciclos) e é reavaliado em contexto limpo.

## Estados do registro

RASCUNHO, TEXTO_APROVADO, TEXTO_REPROVADO, ARTE_VALIDADA, NA_FILA, PUBLICADA, FALHA_PUBLICACAO.

Na Fase A só ocorrem RASCUNHO, TEXTO_APROVADO e TEXTO_REPROVADO. O número público (001, 002...) só é reservado na entrada da fila, nunca antes. Na Fase A o campo numero fica vazio e os registros usam id de laboratório (LAB-001...).

## Uso dos filtros

    python3 ninguem-legenda/filtros.py ninguem-legenda/lote/candidatas.json

Saída em JSON: falhas (eliminam), alertas (sinalizam) e similaridade com o histórico.

## Limites conhecidos da Fase A

- Ortografia: não há corretor determinístico neste ambiente. Fica com o Auditor (Fase B).
- O Crítico desta fase foi executado no mesmo ambiente do Criador, em pacote cego. Não é isolamento real. A calibração com rótulos de Eri mede o quanto isso importa.
