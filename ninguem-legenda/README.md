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
- prompts/critico.md é a versão v2 (critico_v1.md preservado). prompts/preditor.md é o leitor cego que prevê a revelação a partir da foto e do NA FOTO.
- calibracao/execucao_2/: pacotes, previsões, avaliações e mapas da segunda rodada. calibracao/conjunto2/: conjunto inédito, gabarito travado (gabarito_claude2.json e .sha256) e arquivo para Eri.
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
