#!/usr/bin/env python3
"""Tratamento LIMITADO do piso de uma foto (cópia; o original nunca é alterado).
Reduz reflexos claros do piso com um ganho suave de baixa frequência (preserva a textura fina).
Fica fora da skill. Registra parâmetros. Uso: tratar_piso.py ORIGINAL SAIDA FORCA PERCENTIL RAIO"""
import sys, json, hashlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def tratar(origem, saida, forca=1.0, pct=40, raio=35):
    im = Image.open(origem).convert("RGB"); W, H = im.size
    rgb = np.asarray(im, float) / 255
    Y8 = im.convert("L")
    Yb = np.asarray(Y8.filter(ImageFilter.GaussianBlur(raio)), float) / 255
    m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
    # polígono do piso (abaixo do rodapé direito e da parte baixa do corredor), em coordenadas da v4 941 x 1672
    d.polygon([(0, 735), (110, 700), (560, 700), (640, 690), (941, 885), (941, H), (0, H)], fill=255)
    d.ellipse([430, 700, 720, 980], fill=0)          # protege cabo, poça, anéis e reflexo logo sob o cabo
    m = m.filter(ImageFilter.GaussianBlur(14)); M = np.asarray(m, float)[..., None] / 255
    T = np.percentile(Yb[np.asarray(m) > 200], pct)
    gain = np.where(Yb > T, T / np.maximum(Yb, 1e-3), 1.0); gain = 1 - forca * (1 - gain)
    out = np.clip(rgb * (1 - M + M * gain[..., None]), 0, 1)
    Image.fromarray((out * 255 + .5).astype("uint8")).save(saida)
    return dict(origem=origem, saida=saida, forca=forca, percentil=pct, raio=raio, alvo_luminancia=round(float(T), 3), saida_sha256=hashlib.sha256(open(saida, "rb").read()).hexdigest())

if __name__ == "__main__":
    print(json.dumps(tratar(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])), ensure_ascii=False))
