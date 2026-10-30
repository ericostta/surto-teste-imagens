# Decisões editoriais de Eri registradas durante o LAB-001 (24/10/2026)

Registro para a v0.2. A skill v0.1.1 NÃO foi alterada. Estas decisões ainda não estão incorporadas ao perfil B oficial nem ao compositor; hoje valem só no perfil de teste `compor_B215.py`.

| Decisão | Origem | Estado |
|---|---|---|
| Perfil B como base provisória (nome da série no topo à esquerda, NA FOTO e depois FORA, assinatura exclusiva @surtodelucidez) | Parecer de 18:21 | Provisório, sem homologação |
| Número da série colado ao nome da série (à direita dele), não na margem direita | 23:50 | Aplicado no perfil de teste; v0.2 |
| Assinatura @surtodelucidez menor (22 px no teste, antes 27) | 23:50 | Aplicado no perfil de teste; v0.2 |
| Número real exibido só como "001", sem "Nº" (LAB-NNN só em peças de teste) | 23:54 | Decidido; v0.2 (hoje o compositor usa "Nº NNN") |
| Rótulos NA FOTO e FORA DO ENQUADRAMENTO com transparência 215/255 (antes 170) | 23:45 | Aplicado no perfil de teste; v0.2 |
| Degradê do topo reforçado (0,65 até y 480; oficial 0,34 até y 420) | 23:47 | Aplicado no perfil de teste; v0.2 |
| Manter o mesmo padrão de excelência fotográfica, sem afrouxar critérios | 22:52 | Vigente |
| Foto-base do LAB-001: v10 tratada | 23:45 | Aprovada para seguir; aprovação visual da arte pendente |

## Atualização de 30/10/2026
- v10 e v11/v12 reprovadas por plausibilidade física (Eri observou a violação da gravidade; auditoria confirmou). v13 e v14: haste com o topo em direção à parede, escada apoiada.
- **Foto v14 aprovada visualmente por Eri (30/10, 00:12)** como foto-base. Aprovação da arte final, do layout inteiro e do texto: pendente. Esta aprovação não homologa layout, fonte, limiares nem o padrão fotográfico.
- Tratamento aplicado na v14 (só tom, ver tratamento_v14.json): ganho de luminância 0,80 atrás do rótulo NA FOTO. Resultado: rótulo NA FOTO média 4,67 e pior decil 3,63; demais blocos passam nos limiares provisórios.
- Número: formato "001", sem "Nº", abaixo de @surtodelucidez, alinhado à esquerda; tamanho pequeno e sutil. Variante D (11 px, mesmo tom da assinatura, alfa 165) é a candidata. Substitui a redução de "20%" (24 px), considerada grande demais por Eri. Assinatura mantida em 22 px (última composição vista); confirmação do tamanho final pendente.
- Layout "número colado ao título no topo" (24/10) fica substituído por este.

- Correção de 30/10/2026: o ajuste de tom atrás do rótulo NA FOTO na v14 não era necessário pelo critério do perfil C (v14 original: rótulo NA FOTO média 5,24, pior decil 3,74). A medição anterior usou os parâmetros do perfil B. A prévia aprovada usa a foto tratada.

## Atualização de 30/10/2026 (madrugada, 00:44 a 01:11): fechamento do LAB-001 e decisões de Eri
- Layout: Modelo A como base, escurecimento suave E1 e título N4 (LEGENDA em EB Garamond SemiBold, serifa reta, sem itálico), traço divisor de largura total, "001" sob o S e o U. Incorporado como perfil D da skill v0.2.1 (v0.2 e v0.1.1 preservadas). Layout, fonte e valores do escurecimento seguem não homologados.
- **Arte final do LAB-001 aprovada por Eri (30/10/2026, 01:04):** `pilotos/LAB-001/LAB-001_arte_001_v021_perfilD_para_aprovacao.png` (SHA-256 1f1cc15924bdee299f3b165693a5d620dbf8c5b8873d668ff2013663067c6355), gerada pela v0.2.1 com a foto-base `foto_real_L8CFD_chatgpt_v14_tratada.png` (SHA-256 1dfebbe1988b0d0c8c4dbf7a9c19fefc70b6717ab280a88c5d4ac51b0a9288e2). Esta aprovação NÃO homologa layout, fonte, limiares nem o Padrão de Excelência Fotográfica, e NÃO autoriza publicação. O número 001 continua apenas reservado em registro temporário de teste; só será consumido quando Eri confirmar publicação manual.
- **L8CFD: Eri escolheu a opção A (manter e registrar a limitação)** em 30/10/2026, 01:11. Ver `REGISTRO_L8CFD_OPCAO_A.md`. Nenhum item lacrado foi alterado.
- **Rotulagem de IA: Eri decidiu, por ora, NÃO rotular as imagens como geradas por IA** (01:11). Condição declarada por ela: se o Instagram passar a rotular as peças, a série é interrompida e a decisão é revista. A política de plataformas continua sem verificação primária (as páginas oficiais da Meta não puderam ser abertas na pesquisa de 30/10); a arte final não carrega marcas de proveniência nos metadados. A skill não oculta nem manipula metadados de propósito, e não toma nenhuma ação de rotulagem por conta própria.
