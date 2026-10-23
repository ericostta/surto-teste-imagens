# Etapa G1: condições documentais

Data: 22/10/2026. Fase A. Preparação documental apenas. Nada foi gerado, nada foi lacrado, nenhum avaliador ou Crítico foi executado. A G1 só começa com autorização expressa de Eri.

Escopo da G1 (conforme o rev2, seção 13): geração de itens, sem execução de Crítico e sem rotulagem. Os controles especiais não fazem parte da G1 (decisão 9 de Eri).

## 1. Situação de cada condição da G1

| # | Condição | Situação |
|---|---|---|
| 1 | Alternativa de rotulagem escolhida e limitação registrada | Definida: Alternativa 2 (sem confirmação expressa de acesso a outra família). Limitação: um único avaliador externo, de uma família só, mais referência humana parcial. Se Eri confirmar acesso a Gemini ou outro, muda para a Alternativa 1 antes da G2. |
| 2 | Tamanho e divisão; lista de conceitos de foto | Tamanho definido: 30 de fluxo e 30 de desafio. Lista de conceitos: PENDENTE (ver seção 3, P1). |
| 3 | Regras de seleção, inclusão, exclusão e log de excluídos | Texto-base pronto (seção 2). Lacre por hash só na autorização da G1, junto com a lista de conceitos. |
| 4 | Células da amostra de desafio | Quatro células propostas (seção 2.3); distribuição PENDENTE de confirmação (ver P2). Controles especiais fora da G1. |
| 5 | Separação entre lote de desenvolvimento e lote de validação | Proposta (seção 2.5): os 60 itens da G1 formam o lote de validação. Os instrumentos são ensaiados com material já queimado (W01 a W30), sem gerar lote novo. |
| 6 | Recursos | Sem gasto pago, sem conexão de conta, sem crédito visual. Nenhum recurso externo será usado sem autorização. |

## 2. Texto-base para lacrar na G1

Este texto só será lacrado por SHA-256 no momento da autorização da G1. Até lá é rascunho documental.

### 2.1 Fonte dos itens

Fonte A (Criador do projeto, processo normal de criação), com independência de procedência baixa em relação ao Crítico, declarada. Fontes B, C e E só entram se Eri as fornecer e o acesso for real. Fonte D (edições anteriores) não entra como caso independente. Procedência, processo de criação e qualidade editorial são campos separados no mapa privado.

### 2.2 Amostra de fluxo (30 itens)

- Lista de 30 conceitos de foto fixada antes da geração (P1).
- Todo candidato que o processo normal entregaria para cada conceito entra, na ordem de produção, até completar 30.
- Nenhuma triagem por rótulo, por Crítico ou por impressão de qualidade.
- As proporções de BOA, AMBÍGUA e RUIM saem como saírem. Estratos pequenos são descritos, não usados como prova.
- Leitura com contagens e intervalos, não só percentuais.

### 2.3 Amostra de desafio (30 itens), células por intenção de projeto

1. Sentimentalismo implícito.
2. Ausência de segunda leitura.
3. Correção pontual (núcleo promissor, falha localizada).
4. Divergência editorial legítima.

A classe real do item é a atribuída pelo avaliador e por Eri, não a intenção. Item que não saiu como pretendido fica sob a classe real. Sem rodadas extras para preencher células depois de conhecer rótulos, salvo uma segunda rodada pré-registrada e declarada. Células pequenas são descritas, não são prova. Nada da amostra de desafio é apresentado como representativo do fluxo.

### 2.4 Inclusão e exclusão

Inclusão, todos obrigatórios:
1. Formato completo da série (foto, NA FOTO, FORA DO ENQUADRAMENTO) e dentro dos limites de tamanho da série.
2. Procedência, processo de criação e data registrados no mapa privado.
3. Nunca visto por Crítico, avaliador ou redator de Crítico; não derivado de W01 a W30 nem das edições usadas no desenvolvimento; W05, W15 e W19 excluídos.
4. Conceito de foto sem repetição no conjunto.
5. Produzido e congelado por hash antes de qualquer rótulo.

Exclusão: apenas por razões técnicas listadas aqui (formato inválido, duplicata, conhecimento prévio comprovado, violação de segurança do conteúdo). Proibida por qualidade, rótulo ou resultado de Crítico. Cada exclusão entra num log com item, motivo, quem decidiu e quando, antes de qualquer rótulo. O relatório informa candidatos produzidos, incluídos e excluídos por motivo.

### 2.5 Lotes

Os 60 itens da G1 são o lote de validação: produzidos depois do protocolo, nunca vistos por quem redige a versão sob teste ou o julgador, usados uma vez. Se a versão for alterada depois de ver resultados, o lote fica queimado e o novo teste exige outro. Os instrumentos (pacotes cegos, lacre, procedimento do julgador, auditoria) são ensaiados com W01 a W30, já queimados, sem ajuste de prompt e sem gerar lote novo.

### 2.6 Amostragem humana, definida antes

- Triagem (Alternativa 2): subagentes Claude produzem predições cegas lacradas; itens em que a predição contraria o rótulo do ChatGPT vão para exame humano. A predição é sinal de triagem, nunca rótulo.
- Controle humano: 20% dos itens sem conflito de triagem, mínimo de 10, sorteados com semente registrada antes dos rótulos. Eri os classifica às cegas, e só depois confronta com o rótulo do ChatGPT. Discordância relevante obriga discussão explícita da confiabilidade da referência.
- Auditoria do julgador de motivos (G3): pelo menos 20% das avaliações, mínimo de 10, com sorteados mais cobertura dos principais tipos de veredicto; seleção definida antes. Erro sistemático invalida a contagem do julgador. O limite de 15% de inconclusivos é alarme, e concentração por categoria, origem ou tipo de defeito pode invalidar a conclusão correspondente mesmo abaixo disso.

## 3. Pendências que realmente impedem a G1

Apenas duas. As demais condições têm padrão adotado e não impedem nada.

P1. Lista dos 30 conceitos de foto do fluxo. Preciso saber como será obtida: (a) Eri fornece ou aprova a lista; ou (b) autoriza um sorteio com semente registrada sobre uma relação de conceitos que eu proponho e você aprova antes. Sem isso a amostra de fluxo não tem procedimento de seleção fechado.

P2. Distribuição dos 30 itens de desafio entre as quatro células, e confirmação de que os controles especiais ficam fora desses 30 (e fora da G1). Padrão que adotarei se Eri não indicar outro: 8, 8, 8 e 6 itens nas células 1, 2, 3 e 4, com a divergência legítima em menor número por ser a mais difícil de produzir de propósito. Mudança de quantidade não afeta o resto do plano.

Não são pendências, por terem padrão adotado: acesso a segundo avaliador (Alternativa 2 vigente até confirmação expressa); fonte dos itens (fonte A, com limitação declarada); versão candidata (só precisa ser definida antes da G3; a G1 não depende dela); semente do sorteio de controle (registrada no ato do lacre).

## 4. Ordem que se seguirá, quando Eri autorizar

G1, geração e congelamento dos itens com hash, sem rótulo e sem Crítico. G2, pacotes cegos, rótulos lacrados, triagem, exame humano, controle humano. G3, versão e controles travados, protocolo de análise lacrado, execuções, julgador, auditoria. Cada etapa exige autorização escrita própria. Permanecem intocáveis as dez janelas editoriais (início às 06h00, intervalo fixo de 1h30), a grade, o n8n, a fila, as publicadas e as skills existentes. Nenhuma publicação é ativada. Nenhuma versão é homologada.
