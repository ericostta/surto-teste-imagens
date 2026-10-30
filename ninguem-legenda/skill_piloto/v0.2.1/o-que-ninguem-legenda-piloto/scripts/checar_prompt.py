#!/usr/bin/env python3
"""Confere se o prompt fotográfico vaza o conteúdo do FORA (PILOTO v0.1).
Uso: python3 checar_prompt.py --fora "texto do FORA" --prompt-arquivo prompt.txt [--na-foto "texto do NA FOTO"]
Lista palavras de conteúdo do FORA presentes no prompt. Conferência AUXILIAR: não garante ausência de antecipação (sinônimos, pistas visuais e relações implícitas passam). Ocorrência não é prova de erro (pode ser objeto já presente no NA FOTO),
mas exige justificativa."""
import argparse, re, unicodedata


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9\s]", " ", t)


STOP = set("a o as os um uma de do da dos das em no na nos nas por para com sem sobre ate e ou mas que se como mais menos muito pouco ja so ainda nem nao sim ele ela eles elas seu sua seus suas dele dela isso esse essa este esta foi era ser ter tem ha vez quem qual onde quando todo toda todos todas cada outro outra nunca sempre antes depois hoje".split())


def conteudo(t):
    return [p for p in norm(t).split() if len(p) > 3 and p not in STOP]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fora", required=True); ap.add_argument("--prompt-arquivo", required=True); ap.add_argument("--na-foto", default="")
    a = ap.parse_args()
    prompt = open(a.prompt_arquivo, encoding="utf-8").read()
    pp = set(conteudo(prompt)); nf = set(conteudo(a.na_foto))
    achados = sorted({p for p in conteudo(a.fora) if p in pp})
    novos = [p for p in achados if p not in nf]
    print("palavras do FORA presentes no prompt:", achados or "nenhuma")
    if novos: print("ATENÇÃO (não estão no NA FOTO):", novos)
    if "—" in prompt: print("ATENÇÃO: travessão no prompt")
    if re.search(r"\b(irm[aã]o|pai|m[aã]e|filho|devolv|lembran|saudade|historia)\w*", norm(prompt)): print("ATENÇÃO: termo de vínculo ou narrativa no prompt; confira se antecipa a revelação")


if __name__ == "__main__":
    main()
