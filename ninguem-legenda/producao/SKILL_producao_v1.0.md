---
name: o-que-ninguem-legenda
description: Série O QUE NINGUÉM LEGENDA de @surtodelucidez (v1.0, produção autônoma): Stories 9:16 com fotografia documental, NA FOTO e FORA DO ENQUADRAMENTO, gerada diariamente para as 18h00. Gatilho 12!.
---

# O QUE NINGUÉM LEGENDA v1.0 (produção autônoma)

Decisão de Eri em 02/11/2026: série homologada para produção, publicação diária às 18h00 pelo n8n, regime AUTÔNOMO TOTAL (sem aprovação humana diária), fotos pela Kairogen com GPT Image 2. A v0.2.1 (piloto manual) fica preservada em skill_piloto/ no repositório. Idioma: português do Brasil. Sem travessão no meio de frases.

Gatilho: `12!` sozinho. Em conversa, produz UMA edição e entrega a Eri (título, NA FOTO, FORA, arte PNG, relatório); só enfileira se Eri mandar. A tarefa diária das 6h47 (Claude) roda o mesmo fluxo sozinha e enfileira.

## A série em uma frase
Fotografia realista e documental, sem rosto, mais NA FOTO (o que se vê, até 10 palavras) e FORA DO ENQUADRAMENTO (a informação ausente que transforma a leitura da foto, 6 a 22 palavras). A segunda leitura precisa ser genuína e sustentada por algo da cena. Detalhe em references/identidade_editorial.md e references/criador.md.

## Fluxo diário (resumo; passo a passo em references/producao_autonoma.md)
1. Criador: 3 candidatas, filtros (`scripts/filtros.py`), apresenta a melhor.
2. Crítico v2.2 (references/critico_operacao.md, previsões cegas): só segue com veredicto BOA. AMBÍGUA ou REVISAR: até 2 ciclos de revisão; se não virar BOA, não publica nesse dia.
3. Prompt fotográfico (references/prompt_fotografico.md, `scripts/checar_prompt.py`).
4. Foto pela Kairogen: model `gpt-image-2`, `aspect_ratio` "9:16", `extra_params {"resolution":"2k"}`, `expected_credits` 5, `wait_for_completion` true (5 créditos por foto, R$0,80). Até 3 gerações por história (15 créditos). Mais que isso, não publica.
5. Análise da foto (references/analise_visual.md, `scripts/analisar_foto.py`): APTA, AJUSTAR ou REFAZER. Só APTA segue.
6. Número: `scripts/registro_numeracao.py reservar` no registro de produção (ninguem-legenda/producao/registro_producao.csv do repositório). Composição `scripts/compor_story.py ... --perfil D --registro ... --id NL-NNN --numero NNN`. Só grava com APROVAÇÃO TÉCNICA. Nunca altere o texto para caber.
7. Enfileirar: `fila/AAAAMMDD_1800_ninguemlegenda.png` no repositório ericostta/surto-teste-imagens. Registrar a linha no CSV de produção.
8. Confirmar números: o n8n move o arquivo para `publicadas/` depois de publicar. No início de cada execução, para cada número RESERVADO cujo arquivo já está em `publicadas/`, rode `confirmar`. Falha ou arquivo que não foi publicado: `liberar` somente depois de verificar o n8n e avisar Eri.

## Regras que não mudam
- A foto não antecipa a revelação do FORA. Sem rosto, sem pessoa. Padrão de Excelência Fotográfica sem afrouxar (suporte físico plausível, sem texto legível salvo exceção expressa de Eri).
- Prompts de imagem entregues a Eri em bloco de código.
- Layout: perfil D da v0.2.1 (título em duas linhas, traço divisor, "001" sob o S e o U da assinatura, só @surtodelucidez), 1080x1920.
- Número público 001, 002, ... só consome com publicação confirmada; testes, falhas e descartes não consomem.
- Produção insuficiente reduz a oferta: nunca force uma história fraca. Se qualquer etapa falhar, NÃO enfileire nada, não improvise, e avise Eri por push com o motivo.
- Não repetir tema, situação nem mecanismo do registro; não usar textos do laboratório como molde.
- Eri decidiu não rotular as imagens como geradas por IA. Se o Instagram passar a rotular as peças da série (selo "Info de IA"), PARE a série (não enfileire) e avise Eri.
- Modelo de foto fixo: gpt-image-2. Não trocar de modelo por conta própria.

## Registro de edições
Fonte da verdade: ninguem-legenda/producao/registro_producao.csv (repositório) e o espelho em assets/ desta skill (pode estar defasado).
- 001 | 03/11/2026 | guarda-chuva secando | arte aprovada, na fila às 18h
- 002 | 04/11/2026 | carteira escolar riscada | arte aprovada, na fila às 18h
- 003 em diante: produção autônoma a partir de 05/11/2026.

## Limitações
Crítico v2.2 provisório (mesma família de modelos), sem auditoria humana independente; homologação por decisão de Eri, não por validação externa. Ver references/versao_limitacoes.md.
