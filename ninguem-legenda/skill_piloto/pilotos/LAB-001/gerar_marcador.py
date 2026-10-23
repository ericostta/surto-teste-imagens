#!/usr/bin/env python3
"""Gera uma imagem-MARCADOR (não é a foto real, não é arte aprovada) para comparar os perfis A e B de composição.
Fica fora da skill. Carimbada como marcador. A foto real do guarda-chuva será feita por Eri no Gemini."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1080, 1920
img = Image.new("RGB", (W, H), (150, 150, 146))
d = ImageDraw.Draw(img)
for y in range(H):  # parede cinza clara no alto, piso de porcelana mais claro embaixo
    t = y / H
    c = (int(158 - 24 * t), int(158 - 24 * t), int(154 - 26 * t)) if y < 1250 else (int(176 - 30 * (t - .65)), int(174 - 30 * (t - .65)), int(168 - 30 * (t - .65)))
    d.line([(0, y), (W, y)], fill=c)
d.rectangle([0, 1250, W, H], fill=None)
d.polygon([(0, 1250), (W, 1180), (W, H), (0, H)], fill=(190, 188, 180))
d.rectangle([760, 380, 1000, 1180], fill=(120, 120, 118))  # porta entreaberta desfocada
# guarda-chuva aberto (marcador): canopy escuro inclinado + cabo
d.pieslice([140, 560, 900, 1320], 180, 360, fill=(28, 28, 30))
d.line([(520, 940), (560, 1380)], fill=(20, 20, 20), width=14)
d.arc([520, 1340, 640, 1440], 0, 180, fill=(20, 20, 20), width=14)
d.ellipse([360, 1400, 760, 1470], fill=(150, 150, 148))  # poça
img = img.filter(ImageFilter.GaussianBlur(3))
d = ImageDraw.Draw(img)
f = ImageFont.truetype("../o-que-ninguem-legenda-piloto/assets/fonts/Inter-Medium.otf", 34)
d.text((40, 1830), "MARCADOR ILUSTRATIVO: NÃO É A FOTO REAL", font=f, fill=(255, 60, 60))
img.save(sys.argv[1] if len(sys.argv) > 1 else "marcador_guarda_chuva.png")
