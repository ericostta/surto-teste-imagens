# Relatório de calibração 3: Crítico v2.1 (originalidade e três previsões cegas)

Data: 22/10/2026. Fase A, só texto. Registro anterior à rotulagem de Eri no conjunto 2.

## O que foi executado

- Três previsões cegas independentes por item (previsoes_a/b/c.json), feitas por leitores que viram só a descrição da foto e o NA FOTO.
- Crítico v2.1 (prompts/critico.md, cópia em execucao_3/prompt_critico_v2_1.md, SHA-256 do prompt 9910c786f6f006122fda1e88deab9ff99aa1f71382b9cef49e97bbf1b4792c15) em dois subagentes de contexto limpo, um por conjunto, sem filtros, sem justificativa do Criador.
- Validação determinística (validar_avaliacao.py): 0 de 18 inconsistências no conjunto 1 e 0 de 18 no conjunto 2.
- Veredictos do v2 no conjunto 2 intactos (gabarito_claude2.json, SHA-256 3ae5baf3...1558, recalculado e conferido).
- Veredictos do v2.1 no conjunto 2 travados em gabarito_claude2_1.json, SHA-256 c2b1f55fbc0cc5ceea550a2e672cfc7716af35fb6f2aaa23ee874d129caa3e4a, antes dos rótulos de Eri.

## Conjunto 1 (diagnóstico, não evidência)

| | v1 | v2 | v2.1 |
|---|---|---|---|
| Concordância exata com Eri | 11/18 (61%) | 12/18 (67%) | 15/18 (83%) |
| Divergências polares | 0 | 0 | 0 |

Ressalva obrigatória: o T10 foi desenhado a partir de marmita e escovas, que estão neste conjunto. O ganho é em-amostra e não prova melhora. Divergências restantes: K01 e K03 (v2.1 mais severo que Eri) e K15 (mais brando).

## Conjunto 2 (inédito)

Resultados não revelados neste relatório. Serão comparados com os rótulos de Eri depois que ela rotular J01 a J18, sem alterar nada do que está travado.

## Limitações

- Os três preditores e o Crítico são o mesmo modelo: erros correlacionados. Três previsões reduzem ruído de uma tentativa única, mas não criam independência real.
- Amostra de 18 itens: qualquer percentual tem margem larga.
- Critério de sucesso (definido por Eri): não é 80% de concordância, e sim identificar melhor os itens realmente bons, aprovar menos clichês e preservar propostas promissoras para revisão. REVISAR nunca segue para imagem ou publicação.
