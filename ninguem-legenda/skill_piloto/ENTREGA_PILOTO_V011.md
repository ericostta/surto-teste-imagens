# Entrega: PILOTO MANUAL v0.1.1 (revisão técnica mínima após auditoria)

Data: 23/10/2026. ZIP: `dist/o-que-ninguem-legenda-piloto-v0.1.1.zip` (SHA-256 7791524dbfa2787ae09cfb41254069f2e81de2b9c6c16a5ba363f722b8a6f301). A v0.1 foi preservada (SHA-256 970ad43c60f4315bb3b391d84add757dabd3ec1dae4d8a0cbc935ab4e8d20b8e). Nada foi publicado, integrado, comprado ou homologado. Layout, fonte Inter, dimensões e posições NÃO estão homologados.

## 1. Registro das correções

| # | Falha apontada | Correção | Prova |
|---|---|---|---|
| 1 | Estado PUBLICADO do documento não era carregado pelo filtro (só PUBLICADA/ARTE_VALIDADA) | Estados canônicos únicos (RASCUNHO, TEXTO_APROVADO, FOTO_APROVADA, ARTE_APROVADA, RESERVADO, PUBLICADO, LIBERADO, DESCARTADO); legados mapeados (ARTE_VALIDADA, NA_FILA, PUBLICADA, TEXTO_REPROVADO); estado desconhecido conta e avisa; o CSV nunca é alterado pela leitura | `testes_regressao/test_falhas_v01.py` extrai o filtros.py do ZIP v0.1 e mostra: v0.1 ignora PUBLICADO e deixa passar quase repetição; v0.1.1 carrega e barra |
| 2 | config.json com referências à v2.1 | v2.2 identificada como Crítico consultivo (não homologado), com hash; sem v2.1, sem caminhos `prompts/`, sem C1b | `verificar_skill.py` |
| 3 | Conferência do prompt fotográfico só lexical | Análise semântica obrigatória no passo 4; a conferência lexical passou a ser declarada auxiliar | SKILL.md, `references/prompt_fotografico.md` |
| 4 | Arte podia ser aprovada com texto longo ou invadindo zonas | Bloqueio técnico: sem PNG se o texto não cabe no mínimo de fonte ou invade zona de segurança, travessão, margem; texto nunca é alterado; `--rascunho` grava com faixa e continua reprovado | testes de composição |
| 5 | Número público e confirmados | `registro_numeracao.py` (reservar, confirmar, liberar, listar, verificar); número só é consumido ao confirmar publicação; confirmado não volta nem pode ser adulterado (CSV mais arquivo lateral append-only); a composição exige número RESERVADO; LAB- não consome número; recusa o registro.csv do laboratório | testes de numeração |
| 6 | Licença das fontes | `assets/fonts/OFL.txt` (SIL OFL 1.1, The Inter Project Authors) incluída no ZIP; NOTICE.txt removido | `verificar_skill.py` |

## 2. Testes e integridade (todos executados)

- `testes/test_piloto.py` (dentro da skill): 23 testes, OK, também a partir da cópia extraída do ZIP.
- `testes_regressao/test_falhas_v01.py`: 4 testes, OK.
- `scripts/verificar_skill.py`: "skill íntegra" (hash da v2.2 468fd382…, config coerente, sem travessão, estados do documento = estados do script, OFL e fontes, frontmatter, um só SKILL.md).
- `quick_validate.py`: válido. ZIP sem erros, 25 arquivos, sem `__pycache__`.
- `verificar_c1b.py`: todas as verificações passaram; nenhum arquivo congelado alterado (git diff vazio nos caminhos congelados).

## 3. Propostas visuais (simulação, LAB-001, com MARCADOR no lugar da foto real)

Arquivos em `pilotos/LAB-001/`: `LAB-001_proposta_A.png`, `LAB-001_proposta_B.png` e versões `_guias`. O marcador (`marcador_guarda_chuva.png`) é ilustrativo e carimbado; a foto real será a que você fizer no Gemini com `prompt_gemini_L8CFD.txt`.

- A: composição atual como referência (degradê mais forte, FORA 56 px Medium, assinatura y=1522).
- B: degradê mais leve, mais foto visível, FORA mais moderado (50 px Regular, NA FOTO 44 px), assinatura mais afastada da zona inferior da interface (y=1456, folga maior até a zona de 340 px).
Ambas: ordem NA FOTO, depois FORA; assinatura exclusiva @surtodelucidez; aprovação técnica SIM nas duas; aprovação visual pendente de você. Com o marcador, o contraste real do texto sobre a foto não pode ser julgado: conferir com a foto verdadeira.

## 4. L8CFD

Circunstância registrada em `verificacao_c1b/REGISTRO_CIRCUNSTANCIA_L8CFD.md` (possível contaminação da referência cega, sem alterar item congelado nem substituir história). As 72 avaliações seguem suspensas; qualquer mudança na participação de L8CFD exige sua autorização expressa.

## 5. Intocados

n8n, grade, fila, contador real, registro.csv do laboratório, `prompts/`, validador, M1/G1/G2/G3, arquivos lacrados e privados da verificação C1b, v2.2 original. Nenhuma avaliação executada, nenhum número real consumido.

## 6. Pendências suas

1. Escolher A, B ou pedir ajuste; homologar (ou não) fonte, dimensões e posições.
2. Enviar a foto real do guarda-chuva para a composição final (com número reservado só quando for publicar).
3. Confirmar formalmente a classificação de L8CFD e decidir se as 72 avaliações retomam.
4. Gatilho `12!` e zonas de segurança (250/340 px) ainda provisórios.
5. Classificação das doze inéditas (depois, o papel dos números nas seis).
