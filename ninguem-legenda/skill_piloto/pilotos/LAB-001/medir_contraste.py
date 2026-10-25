#!/usr/bin/env python3
"""Mede o contraste EFETIVO do texto do perfil B sobre a foto (render sem texto, com degradê). Fora da skill.
Uso: medir_contraste.py FOTO"""
import sys, json
import numpy as np
sys.path.insert(0, "../../o-que-ninguem-legenda-piloto/scripts")
import compor_story as cs
foto = sys.argv[1]; L = cs.PERFIS["B"]
base = cs.degrade(cs.fundo_foto(foto).convert("RGBA"), L).convert("RGB")
bg = np.asarray(base, float) / 255
def lum(c):
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4); return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]
caixas = {"titulo": ((85, 295, 620, 328), 255), "numero": ((850, 295, 1000, 328), 255),
          "rotulo NA FOTO": ((85, 957, 245, 983), L["rotulo_alpha"]), "NA FOTO texto": ((85, 1005, 605, 1105), L["na_foto_alpha"]),
          "rotulo FORA": ((85, 1166, 575, 1190), L["rotulo_alpha"]), "FORA texto": ((85, 1215, 845, 1390), L["fora_alpha"]), "assinatura": ((85, 1462, 375, 1488), 165)}
res = {}
for nome, ((x0, y0, x1, y1), al) in caixas.items():
    b = bg[y0:y1, x0:x1]; a = al / 255
    t = a * 1.0 + (1 - a) * b
    cr = (lum(t) + 0.05) / (lum(b) + 0.05)
    res[nome] = dict(media=round(float(cr.mean()), 2), pior_decil=round(float(np.percentile(cr, 10)), 2))
print(json.dumps(res, ensure_ascii=False, indent=1))
