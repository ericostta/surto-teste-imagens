#!/usr/bin/env python3
"""Testes dos instrumentos de G1/G3 com dados SINTÉTICOS (nenhum item real, nenhum item de validação)."""
import json, os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "instrumentos_g1"))
import montar_pacotes as M, varredura_vazamento as W, manifesto_hashes as H

res = []
def t(nome, cond): res.append((nome, bool(cond)))

itens = {f"S{i}": {"conceito_foto": f"foto sintetica {i}", "na_foto": f"na foto sintetica numero {i}",
                  "fora": f"fora sintetico numero {i} com texto longo o bastante", "rotulo": "RUIM", "origem": "X"} for i in range(8)}
prev = {k: ["p1", "p2", "p3"] for k in itens}
p1, m1 = M.pacote_critico(itens, prev, ["ant"], "semente", 1)
p2, m2 = M.pacote_critico(itens, prev, ["ant"], "semente", 2)
p1b, m1b = M.pacote_critico(itens, prev, ["ant"], "semente", 1)
t("determinístico para mesma semente e execução", p1 == p1b and m1 == m1b)
t("códigos diferem entre execuções", set(m1) != set(m2))
t("ordem difere entre execuções", [m1[p["codigo"]] for p in p1] != [m2[p["codigo"]] for p in p2])
t("pacote só tem campos permitidos", all(set(p) == M.CAMPOS_PACOTE_CRITICO for p in p1))
t("pacote não vaza rótulo, origem nem id", "RUIM" not in json.dumps(p1) and '"origem"' not in json.dumps(p1) and "S3" not in json.dumps(p1))
t("mapa cobre todos os itens", sorted(m1.values()) == sorted(itens))
try:
    M.pacote_critico(itens, {**prev, "S0": ["a"]}, [], "s", 1); t("rejeita previsões incompletas", False)
except ValueError:
    t("rejeita previsões incompletas", True)

ref = {"estado": "BOA", "motivo": "m", "tipo_fundamento": "A", "natureza": "mérito", "correcao_pontual": "", "contestado": False}
saida = {"codigo": "C1", "veredicto": "APROVADA", "versao_criterio": "v2.4-exp"}
pj = M.pacote_julgador("C1", itens["S0"], saida, ref, ["ant"])
t("julgador: pacote completo", not pj["inconclusivo_por_pacote"])
t("julgador: cego à versão", "versao_criterio" not in pj["saida_critico"] and "v2.4" not in json.dumps(pj))
t("julgador: sem textos anteriores é inconclusivo", M.pacote_julgador("C1", itens["S0"], saida, ref, None)["inconclusivo_por_pacote"])
t("julgador: sem foto é inconclusivo", M.pacote_julgador("C1", {**itens["S0"], "conceito_foto": ""}, saida, ref, [])["inconclusivo_por_pacote"])
t("julgador: contestado sem fundamentos é inconclusivo", M.pacote_julgador("C1", itens["S0"], saida, {**ref, "contestado": True}, [])["inconclusivo_por_pacote"])
t("julgador: lista vazia de anteriores é aceita", not M.pacote_julgador("C1", itens["S0"], saida, ref, [])["inconclusivo_por_pacote"])

with tempfile.TemporaryDirectory() as d:
    os.makedirs(os.path.join(d, "prompts")); os.makedirs(os.path.join(d, "validacao"))
    open(os.path.join(d, "prompts", "limpo.md"), "w").write("Nada de relevante aqui. Texto qualquer sobre critérios.")
    t("varredura limpa", W.varrer(itens, [d]) == [])
    open(os.path.join(d, "prompts", "sujo.md"), "w").write("Exemplo: Fora sintético número 3 com texto longo o bastante!")
    r = W.varrer(itens, [os.path.join(d, "prompts")])
    t("varredura detecta frase copiada (normalizada)", any(o["item"] == "S3" and o["campo"] == "fora" for o in r))
    t("varredura ignora pasta indicada", W.varrer(itens, [d], ignorar=[os.path.join(d, "prompts")]) == [])
    itens_h = {"S9": {"na_foto": "", "fora": "", "sha256": "ab" * 32}}
    open(os.path.join(d, "prompts", "hash.json"), "w").write('{"h": "' + "ab" * 32 + '"}')
    t("varredura detecta hash do manifesto", any(o["tipo"].startswith("hash:") for o in W.varrer(itens_h, [os.path.join(d, "prompts")])))
    a = os.path.join(d, "a.txt"); open(a, "w").write("um")
    cwd = os.getcwd(); os.chdir(d)
    m = H.gerar(["a.txt"]); t("manifesto íntegro", H.verificar(m) == [])
    open("a.txt", "w").write("dois"); t("manifesto detecta alteração", H.verificar(m) == [("a.txt", "hash diferente")])
    os.remove("a.txt"); t("manifesto detecta ausência", H.verificar(m) == [("a.txt", "ausente")])
    os.chdir(cwd)

for n, ok in res: print(("ok   " if ok else "FALHA"), n)
f = [n for n, ok in res if not ok]
print(f"\n{len(res) - len(f)} de {len(res)} conforme o esperado")
sys.exit(1 if f else 0)
