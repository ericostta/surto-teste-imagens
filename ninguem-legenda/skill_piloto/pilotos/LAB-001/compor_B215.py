#!/usr/bin/env python3
"""Composição de TESTE do perfil B com rótulos em transparência 215/255 (a skill e o perfil B oficial NÃO são alterados).
Uso: compor_B215.py FOTO SAIDA [--guias]"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "../../o-que-ninguem-legenda-piloto/scripts")
import compor_story as cs
cs.PERFIS["B215"] = dict(cs.PERFIS["B"], rotulo_alpha=215)
NA_FOTO = "Um guarda-chuva aberto secando no corredor."
FORA = "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar."
r = cs.compor(sys.argv[1], NA_FOTO, FORA, "LAB-001", sys.argv[2], perfil="B215", simulacao=True, guias="--guias" in sys.argv)
print(r if not isinstance(r, dict) else {k: r[k] for k in ("aprovacao_tecnica", "falhas", "texto_alterado") if k in r})
