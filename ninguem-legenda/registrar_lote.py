#!/usr/bin/env python3
"""Grava no registro.csv as candidatas de um lote já avaliadas (Fase A).

Uso: python3 registrar_lote.py lote/candidatas.json lote/avaliacao_critico.json AAAA-MM-DD

Não atribui número público (o número só é reservado na entrada da fila, Fase B).
Idempotente: ignora ids que já estão no registro.
"""
import csv
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REGISTRO = AQUI / "registro.csv"
CAMPOS = ["id", "numero", "data", "estado", "tema", "situacao", "mecanismo", "emocao", "tipo_contraste",
          "abertura_fora", "na_foto", "fora_do_enquadramento", "conceito_foto", "rosto", "avaliacao",
          "justificativa_rejeicao", "status_publicacao"]
ESTADO = {"APROVADA": "TEXTO_APROVADO", "REPROVADA": "TEXTO_REPROVADO", "REVISAR": "RASCUNHO"}


def main() -> int:
    cands = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    aval = {a["id"]: a for a in json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))["avaliacoes"]}
    data = sys.argv[3]
    existentes = set()
    if REGISTRO.exists():
        with REGISTRO.open(encoding="utf-8", newline="") as f:
            existentes = {r["id"] for r in csv.DictReader(f)}
    novas = []
    for c in cands:
        if c["id"] in existentes:
            continue
        a = aval[c["id"]]
        motivo = ""
        if a["veredicto"] != "APROVADA":
            partes = a.get("eliminatorias", []) + a.get("defeitos", [])
            motivo = " | ".join(partes)
            if a.get("o_que_mudaria"):
                motivo += " | mudaria: " + a["o_que_mudaria"]
        novas.append({
            "id": c["id"], "numero": "", "data": data, "estado": ESTADO[a["veredicto"]],
            "tema": c["tema"], "situacao": c["situacao"], "mecanismo": c["mecanismo"], "emocao": c["emocao"],
            "tipo_contraste": c["tipo_contraste"], "abertura_fora": " ".join(c["fora"].split()[:3]).lower(),
            "na_foto": c["na_foto"], "fora_do_enquadramento": c["fora"], "conceito_foto": c["conceito_foto"],
            "rosto": str(c["rosto"]).lower(),
            "avaliacao": f"{a['veredicto']} nota={a['nota']} previsao={a['grau_previsao']}",
            "justificativa_rejeicao": motivo, "status_publicacao": "laboratorio",
        })
    with REGISTRO.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writerows(novas)
    print(f"{len(novas)} registros adicionados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
