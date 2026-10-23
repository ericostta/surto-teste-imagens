#!/usr/bin/env python3
"""Varredura de vazamento de itens de validação (instrumento; rascunho G0; não executado sobre itens reais).

Procura, nos diretórios indicados, o texto de cada item (frase por frase, normalizado) e os hashes do manifesto.
Só detecta cópia de texto, não influência indireta. Uma ocorrência bloqueia a etapa e vira registro de possível contaminação.
Uso: varredura_vazamento.py itens.json DIR [DIR ...] [--ignorar CAMINHO ...]
"""
import json, os, re, sys, unicodedata

EXT = {".md", ".json", ".py", ".txt", ".csv", ".jsonl", ".sha256"}
MIN_CHARS = 25


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9 ]+", " ", re.sub(r"\s+", " ", s)).strip()


def frases(texto: str):
    for f in re.split(r"[.!?;\n]+", texto):
        n = norm(f)
        if len(n) >= MIN_CHARS:
            yield n


def varrer(itens: dict, dirs, ignorar=()):
    alvo = {}
    for i, it in itens.items():
        for campo in ("na_foto", "fora"):
            for f in frases(it.get(campo, "")):
                alvo[f] = (i, campo)
    hashes = {it.get("sha256") for it in itens.values() if it.get("sha256")}
    ocorr = []
    ignorar = [os.path.abspath(x) for x in ignorar]
    for d in dirs:
        for raiz, _, arqs in os.walk(d):
            if any(os.path.abspath(raiz).startswith(x) for x in ignorar):
                continue
            for a in arqs:
                if os.path.splitext(a)[1] not in EXT:
                    continue
                p = os.path.join(raiz, a)
                try:
                    t = open(p, encoding="utf-8", errors="ignore").read()
                except OSError:
                    continue
                nt = norm(t)
                for f, (i, campo) in alvo.items():
                    if f in nt:
                        ocorr.append({"arquivo": p, "item": i, "campo": campo, "tipo": "frase"})
                for h in hashes:
                    if h and h in t:
                        ocorr.append({"arquivo": p, "item": None, "campo": None, "tipo": "hash:" + h[:12]})
    return ocorr


def main():
    args = sys.argv[1:]
    ign = []
    if "--ignorar" in args:
        k = args.index("--ignorar"); ign = args[k + 1:]; args = args[:k]
    itens = json.load(open(args[0], encoding="utf-8"))
    r = varrer(itens, args[1:], ign)
    print(json.dumps({"ocorrencias": r, "limpo": not r}, ensure_ascii=False, indent=1))
    sys.exit(1 if r else 0)

if __name__ == "__main__":
    main()
