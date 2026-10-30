# Entrega: skill O QUE NINGUÉM LEGENDA, piloto manual v0.2.1 (30/10/2026)

Pacote: `dist/o-que-ninguem-legenda-piloto-v0.2.1.zip` (SHA-256 10b6729ea0a0..., valor completo em `REGISTRO_VERSAO_v0.2.1.json`), idêntico à fonte em `v0.2.1/o-que-ninguem-legenda-piloto/`. A v0.2 e a v0.1.1 permanecem intactas (hashes dos zips conferidos no registro).

Status: desenvolvimento técnico do piloto manual. NÃO é homologação editorial, do layout, da fonte nem autorização operacional. Nada foi publicado, integrado ao n8n, à fila, à grade ou ao contador real. O número 001 continua RESERVADO apenas em registro temporário de teste; não foi consumido.

## O que mudou (e por quê)

Origem: rodada visual de 30/10/2026, com escolhas de Eri (Modelo A como base, escurecimento E1, título N4).

| Alteração | Arquivos | Justificativa |
|---|---|---|
| Perfil D, novo padrão (A, B e C continuam disponíveis e geram arte idêntica à da v0.2, conferido por hash com e sem foto) | scripts/compor_story.py, config.json, SKILL.md | Layout aprovado visualmente por Eri |
| Blocos de texto cerca de 70 px mais baixos | perfil D | Dar mais destaque à foto; o limite é a zona inferior provisória de 340 px |
| Traço divisor de largura total (2 px, alfa 175) | perfil D | Pedido de Eri a partir do Modelo A |
| "001" sob o S e o U de @surtodelucidez (começa depois do "@"), 22 px e 11 px preservados | perfil D | Pedido de Eri; tamanhos aprovados mantidos |
| Escurecimento suave localizado: mancha preta de contorno esfumado atrás do título (36%) e do bloco inferior (42%), sem degradê inferior; texto à esquerda | perfil D, função `mancha` | Escolha E1 de Eri |
| Título em duas linhas: O QUE NINGUÉM (Inter SemiBold 27 px) e LEGENDA (EB Garamond SemiBold 108 px, serifa reta, sem itálico) | perfil D | Escolha N4 de Eri |
| Fonte EB Garamond SemiBold com licença OFL própria | assets/fonts/EBGaramond-SemiBold.ttf, OFL_EBGaramond.txt | Licença aberta (Copyright 2017 The EB Garamond Project Authors); arquivo vindo da série Permissão do Dia |
| Verificador e testes ampliados | verificar_skill.py, testes/test_piloto.py | 46 testes (39 da v0.2 mais 7 do perfil D), todos OK; verificação íntegra a partir do zip extraído |

## Conferência da arte
A arte do LAB-001 com o número real "001" gerada pelo compositor da v0.2.1 (`pilotos/LAB-001/LAB-001_arte_001_v021_perfilD_para_aprovacao.png`) é idêntica byte a byte ao protótipo que Eri escolheu (SHA-256 1f1cc15924bd...). Aprovação técnica sem falhas nem avisos. Contraste efetivo (média): título 14,8; NA FOTO 8,3; FORA 11,3; assinatura 6,1; número 5,7 (limite provisório dos discretos: 3,0).

## Não alterado
Crítico v2.2 (hash conferido), preditor cego, criador, filtros e janelas de repetição, taxonomia, estados e registro de numeração, Padrão de Excelência Fotográfica, SKILLs de outras séries, n8n, horários, fila, grade, contador real, arquivos congelados, lacres, registro.csv do laboratório, C1b, Emenda 2 e as 72 avaliações (suspensas).

## Pendências de Eri (nada aqui bloqueia o piloto manual)
- Aprovação final da arte LAB-001 (história, foto e arte).
- Homologação do layout, da fonte, dos limiares de contraste e do Padrão de Excelência Fotográfica.
- Decisão A/B/C/D sobre a L8CFD, separada e pendente.
- Política de rotulagem de conteúdo gerado por IA antes de qualquer publicação.

## Limitações novas
A mancha foi calibrada para uma cena; em fotos muito claras ou muito escuras o contraste pode exigir ajuste. O contraste segue apenas medido e avisado, nunca garantido. A fonte serifada vem de outra série de Eri e foi copiada com a licença aberta.
