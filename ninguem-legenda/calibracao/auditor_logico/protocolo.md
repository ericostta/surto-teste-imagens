# Protocolo de teste do Auditor Lógico (pré-registrado)

Prompt v1: prompts/auditor_logico.md (SHA-256 registrado no commit). Nada é integrado ao fluxo.

## Fase 1: desenvolvimento (6 itens, falhas conhecidas por mim, registradas antes da execução)
Defeito conhecido esperado:
- LAB-005-r1: a revisão reenumerou objetos que a foto já mostra (foto_texto ou redundância com a foto)
- LAB-009-r1: pronomes ambíguos (referencia)
- NV-05-r1 (J01-r1): oração "nunca precisou correr para pegar um" admite leitura contraditória (causal ou referencia)
Consistentes (aprovadas pelo Crítico, sem defeito lógico conhecido): LAB-011-r1, LAB-004-r1, LAB-012-r1.
Regra: um único ajuste de prompt é permitido, apenas para reduzir reprovação artificial ou ambiguidade de formato, documentado com o diff. Depois a versão é travada por hash.

## Fase 2: validação (itens diferentes dos da Fase 1)
Gabarito de falhas esperadas escrito e commitado antes da execução. Duas execuções independentes. Métricas: detecção do defeito esperado (com evidência textual pertinente), achados eliminatórios em itens limpos (reprovação artificial), achados corrigíveis em itens limpos (ruído), concordância entre as duas execuções. Sem pontuação nova.
