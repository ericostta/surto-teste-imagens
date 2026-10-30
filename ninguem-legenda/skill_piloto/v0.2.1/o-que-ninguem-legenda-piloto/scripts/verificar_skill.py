#!/usr/bin/env python3
"""Verificação de integridade da skill (PILOTO v0.2.1). Executar a partir da pasta da skill: python3 scripts/verificar_skill.py
Confere: Crítico v2.2 idêntico ao hash congelado e identificado no config; ausência de referências ativas à v2.1; estados do
documento de numeração iguais aos do script; licença OFL e fontes presentes; SKILL.md com frontmatter; um único SKILL.md;
ausência de travessão nos documentos; hashes de REGISTRO_VERSAO (quando presente). Saída 1 se falhar."""
import hashlib, json, re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from filtros import ESTADOS_CANONICOS, ESTADOS_LEGADOS, ESTADOS_QUE_CONTAM
HASH_V22 = "468fd3823f83909dd87127d7a4affd835df4be09c7601e62c37b38dc54b553a3"
falhas = []
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

if sha(RAIZ / "references/critico_v2_2_referencia.md") != HASH_V22: falhas.append("critico_v2_2_referencia.md difere do Crítico v2.2 congelado")
cfg = json.loads((RAIZ / "scripts/config.json").read_text(encoding="utf-8"))
if cfg.get("versao_critico") != "v2.2": falhas.append(f"config.versao_critico = {cfg.get('versao_critico')}, esperado v2.2")
cc = cfg.get("critico_consultivo", {})
if cc.get("sha256") != HASH_V22 or cc.get("referencia") != "references/critico_v2_2_referencia.md": falhas.append("config.critico_consultivo não aponta para a v2.2 do piloto")
if not (RAIZ / cc.get("referencia", "x")).exists(): falhas.append("caminho do Crítico no config não existe")
if "critico_experimental" in cfg or "prompts/" in json.dumps(cfg): falhas.append("config ainda contém caminho do laboratório (prompts/) ou critico_experimental")
for f in list((RAIZ / "references").glob("*.md")) + [RAIZ / "SKILL.md"]:
    if f.name == "critico_v2_2_referencia.md": continue
    t = f.read_text(encoding="utf-8")
    if re.search(r"v2\.1|critico_v2_1", t) and "histór" not in t.lower(): falhas.append(f"{f.name}: referência à v2.1 sem contexto histórico")
    if "—" in t: falhas.append(f"{f.name}: travessão")
doc = (RAIZ / "references/assinatura_numeracao.md").read_text(encoding="utf-8")
m = re.search(r"Estados canônicos do registro: ([A-Z_, ]+)\.", doc)
if not m or tuple(x.strip() for x in m.group(1).split(",")) != ESTADOS_CANONICOS: falhas.append("estados canônicos do documento diferem dos do script")
m = re.search(r"Estados legados lidos como equivalentes: ([A-Z_>, -]+)\.", doc)
if not m: falhas.append("estados legados ausentes no documento")
else:
    par = dict(x.strip().split("->") for x in m.group(1).split(","))
    if par != ESTADOS_LEGADOS: falhas.append("estados legados do documento diferem dos do script")
m = re.search(r"Estados que entram no controle de similaridade, repetição e diversidade: ([A-Z_, ]+)\.", doc)
if not m or tuple(x.strip() for x in m.group(1).split(",")) != ESTADOS_QUE_CONTAM: falhas.append("estados que contam diferem entre documento e script")
fontes = RAIZ / "assets/fonts"
for n in ("Inter-Regular.otf", "Inter-Medium.otf", "Inter-SemiBold.otf", "OFL.txt", "EBGaramond-SemiBold.ttf", "OFL_EBGaramond.txt"):
    if not (fontes / n).exists(): falhas.append(f"assets/fonts/{n} ausente")
ofl = (fontes / "OFL.txt").read_text(encoding="utf-8") if (fontes / "OFL.txt").exists() else ""
for chave in ("SIL OPEN FONT LICENSE", "PERMISSION & CONDITIONS", "DISCLAIMER", "Inter Project Authors"):
    if chave not in ofl: falhas.append(f"OFL.txt sem '{chave}'")
ofl2 = (fontes / "OFL_EBGaramond.txt").read_text(encoding="utf-8") if (fontes / "OFL_EBGaramond.txt").exists() else ""
for chave in ("SIL OPEN FONT LICENSE", "PERMISSION & CONDITIONS", "DISCLAIMER", "EB Garamond Project Authors"):
    if chave not in ofl2: falhas.append(f"OFL_EBGaramond.txt sem '{chave}'")
sk = (RAIZ / "SKILL.md").read_text(encoding="utf-8")
if not re.match(r"---\nname: o-que-ninguem-legenda-piloto\ndescription: .+\n---\n", sk): falhas.append("frontmatter do SKILL.md inválido")
if len(list(RAIZ.rglob("SKILL.md"))) != 1: falhas.append("deve haver exatamente um SKILL.md")
import compor_story
if compor_story.PERFIL_PADRAO not in compor_story.PERFIS: falhas.append("perfil padrão do layout inexistente")
if "padrao_fotografico" not in cfg or "provisoria" not in cfg["padrao_fotografico"].get("status", ""): falhas.append("config.padrao_fotografico ausente ou não marcado como provisório")
if cfg.get("rodadas", {}).get("max_geracoes_imagem_por_texto") != 2 or not cfg["rodadas"].get("excecao_ao_limite_exige_autorizacao_expressa_de_eri_registrada"): falhas.append("limite de duas correções ou exigência de exceção documentada ausente no config")
if "o gerador de imagem escolhido por Eri" not in sk or re.search(r"(apenas|somente|exclusivamente) (no )?Gemini", sk): falhas.append("SKILL.md impõe gerador de imagem exclusivo")
if "v0.2.1" not in sk: falhas.append("SKILL.md não identifica a versão v0.2.1")
if cfg.get("padrao_fotografico", {}).get("layout_padrao") != compor_story.PERFIL_PADRAO: falhas.append("config.layout_padrao difere do perfil padrão do compositor")
if not (RAIZ / "scripts/medir_inclinacao.py").exists(): falhas.append("scripts/medir_inclinacao.py ausente")
print("FALHAS:\n" + "\n".join(falhas) if falhas else "skill íntegra")
sys.exit(1 if falhas else 0)
