#!/usr/bin/env python3
"""Testes reproduzíveis da skill (PILOTO v0.1.1). Executar a partir da pasta da skill: python3 testes/test_piloto.py
Usam apenas arquivos temporários. Nunca tocam o registro.csv do laboratório nem o contador real."""
import csv, hashlib, importlib, io, json, os, subprocess, sys, tempfile, unittest
from contextlib import redirect_stderr
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SC = RAIZ / "scripts"
sys.path.insert(0, str(SC))
import filtros
import registro_numeracao as rn
import compor_story

CAMPOS = "id,numero,data,estado,tema,situacao,mecanismo,emocao,tipo_contraste,abertura_fora,na_foto,fora_do_enquadramento,conceito_foto,rosto,avaliacao,justificativa_rejeicao,status_publicacao".split(",")
NA = "Um relógio parado na parede da sala."
FORA = "Parou no minuto em que o último morador se mudou, e ninguém teve coragem de trocar a pilha."
SHA = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def escrever(caminho, linhas):
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, lineterminator="\n"); w.writeheader()
        for l in linhas:
            w.writerow({c: l.get(c, "") for c in CAMPOS})


def linha(id_, estado, **k):
    base = dict(id=id_, estado=estado, tema="t", situacao="s", mecanismo="M03", emocao="cotidiano", tipo_contraste="presenca_vs_ausencia",
                abertura_fora="parou no minuto", na_foto=NA, fora_do_enquadramento=FORA, conceito_foto="c", rosto="false", status_publicacao="")
    base.update(k); return base


def cand(**k):
    c = dict(id="LAB-900", tema="x", situacao="y", mecanismo="M05", emocao="afeto", tipo_contraste="cena_vs_autor_da_cena",
             na_foto=NA, fora=FORA, conceito_foto="Relógio de parede parado. Sem texto.", rosto=False)
    c.update(k); return c


class Estados(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp(); self.reg = Path(self.d) / "registro_piloto.csv"

    def hist(self, estado):
        escrever(self.reg, [linha("LAB-001", estado)])
        filtros.REGISTRO = self.reg
        return filtros.carregar_historico()

    def test_estados_que_contam_entram_no_historico(self):
        for e in ("TEXTO_APROVADO", "FOTO_APROVADA", "ARTE_APROVADA", "RESERVADO", "PUBLICADO", "LIBERADO", "ARTE_VALIDADA", "NA_FILA", "PUBLICADA"):
            with self.subTest(estado=e):
                self.assertEqual(len(self.hist(e)), 1, f"{e} deveria contar no controle")

    def test_estados_que_nao_contam(self):
        for e in ("RASCUNHO", "DESCARTADO", "TEXTO_REPROVADO"):
            with self.subTest(estado=e):
                self.assertEqual(len(self.hist(e)), 0)

    def test_minusculas_e_espacos(self):
        self.assertEqual(len(self.hist(" publicado ")), 1)

    def test_estado_desconhecido_conta_e_avisa(self):
        avisos = []
        escrever(self.reg, [linha("LAB-001", "PUBLICADOS")]); filtros.REGISTRO = self.reg
        with redirect_stderr(io.StringIO()):
            h = filtros.carregar_historico(avisos)
        self.assertEqual(len(h), 1); self.assertTrue(avisos)

    def test_similaridade_com_publicada_e_publicado(self):
        for e in ("PUBLICADO", "PUBLICADA", "ARTE_APROVADA", "ARTE_VALIDADA", "RESERVADO"):
            with self.subTest(estado=e):
                h = self.hist(e)
                r = filtros.avaliar(cand(), h, [cand()])
                self.assertTrue(any("quase repetição" in f for f in r["falhas"]), f"{e}: repetição não detectada {r['falhas']}")

    def test_repeticao_estrutural_mecanismo_abertura(self):
        h = self.hist("PUBLICADO")
        r = filtros.avaliar(cand(mecanismo="M03", fora="Parou no minuto exato em que a casa esvaziou, e a pilha segue lá dentro."), h, [])
        txt = " ".join(r["alertas"])
        self.assertIn("mecanismo M03", txt); self.assertIn("abertura sintática repetida", txt)

    def test_concentracao_emocional(self):
        escrever(self.reg, [linha(f"LAB-{i:03d}", "PUBLICADO", emocao="melancolia", na_foto=f"n{i}", fora_do_enquadramento=f"f{i} unico{i}") for i in range(1, 11)])
        filtros.REGISTRO = self.reg
        r = filtros.avaliar(cand(emocao="melancolia", fora="Texto totalmente diferente sobre outra situação qualquer da vida."), filtros.carregar_historico(), [])
        self.assertTrue(any("concentração emocional" in a for a in r["alertas"]))

    def test_cota_de_rostos(self):
        escrever(self.reg, [linha(f"LAB-{i:03d}", "PUBLICADO", rosto="true", na_foto=f"a{i}", fora_do_enquadramento=f"b{i} z{i}") for i in (1, 2)])
        filtros.REGISTRO = self.reg
        r = filtros.avaliar(cand(rosto=True, fora="Fala completamente outra coisa agora sobre algo distinto."), filtros.carregar_historico(), [])
        self.assertTrue(any("cota de rostos" in f for f in r["falhas"]))

    def test_leitura_nao_altera_o_csv(self):
        escrever(self.reg, [linha("LAB-001", "PUBLICADA")]); antes = SHA(self.reg); filtros.REGISTRO = self.reg
        filtros.carregar_historico(); self.assertEqual(antes, SHA(self.reg))


class Numeracao(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp(); self.reg = str(Path(self.d) / "registro_piloto.csv")
        escrever(self.reg, [linha("LAB-001", "ARTE_APROVADA"), linha("LAB-002", "TEXTO_APROVADO", na_foto="a", fora_do_enquadramento="b c"), linha("LAB-003", "TEXTO_APROVADO", na_foto="d", fora_do_enquadramento="e f")])

    def run_(self, *a):
        return rn.main(list(a) + ["--registro", self.reg])

    def linhas(self):
        return {l["id"]: l for l in rn.ler(self.reg)[0]}

    def test_reserva_sequencial_sem_duplicar(self):
        self.run_("reservar", "--id", "LAB-001"); self.run_("reservar", "--id", "LAB-002")
        L = self.linhas(); self.assertEqual((L["LAB-001"]["numero"], L["LAB-002"]["numero"]), ("001", "002"))
        with self.assertRaises(rn.Erro): self.run_("reservar", "--id", "LAB-001")

    def test_confirmar_exige_reserva_e_consome(self):
        with self.assertRaises(rn.Erro): self.run_("confirmar", "--id", "LAB-001")
        self.run_("reservar", "--id", "LAB-001"); self.run_("confirmar", "--id", "LAB-001")
        self.assertEqual(self.linhas()["LAB-001"]["estado"], "PUBLICADO")
        with self.assertRaises(rn.Erro): self.run_("liberar", "--id", "LAB-001")  # publicado nunca é liberado

    def test_liberar_reaproveita_numero_nao_confirmado(self):
        self.run_("reservar", "--id", "LAB-001"); self.run_("liberar", "--id", "LAB-001", "--motivo", "falha")
        self.run_("reservar", "--id", "LAB-002")
        self.assertEqual(self.linhas()["LAB-002"]["numero"], "001")

    def test_numero_confirmado_nunca_volta(self):
        self.run_("reservar", "--id", "LAB-001"); self.run_("confirmar", "--id", "LAB-001")
        self.run_("reservar", "--id", "LAB-002")
        self.assertEqual(self.linhas()["LAB-002"]["numero"], "002")
        # adulteração: apagar o estado PUBLICADO e reservar de novo
        linhas, campos = rn.ler(self.reg)
        for l in linhas:
            if l["id"] == "LAB-001": l["estado"] = "ARTE_APROVADA"; l["numero"] = ""
        rn.gravar(self.reg, linhas, campos)
        self.assertTrue(rn.verificar(self.reg))
        with self.assertRaises(rn.Erro): self.run_("reservar", "--id", "LAB-003")

    def test_duplicidade_detectada(self):
        self.run_("reservar", "--id", "LAB-001")
        linhas, campos = rn.ler(self.reg)
        for l in linhas:
            if l["id"] == "LAB-002": l["estado"] = "RESERVADO"; l["numero"] = "001"
        rn.gravar(self.reg, linhas, campos)
        self.assertTrue(any("duplicado" in f for f in rn.verificar(self.reg)))

    def test_recusa_registro_do_laboratorio(self):
        with self.assertRaises(rn.Erro): rn.main(["listar", "--registro", str(Path(self.d) / "registro.csv")])

    def test_compor_exige_reserva_para_numero_publico(self):
        out = str(Path(self.d) / "s.png"); k = dict(na_foto=NA, fora=FORA, saida=out, simulacao=True)
        r = compor_story.compor(None, numero="001", registro=self.reg, id_="LAB-001", **k)
        self.assertFalse(r["aprovacao_tecnica"]); self.assertFalse(Path(out).exists())
        self.run_("reservar", "--id", "LAB-001")
        r = compor_story.compor(None, numero="001", registro=self.reg, id_="LAB-001", **k)
        self.assertTrue(r["aprovacao_tecnica"], r); self.assertTrue(Path(out).exists())
        self.run_("confirmar", "--id", "LAB-001"); os.remove(out)
        r = compor_story.compor(None, numero="001", registro=self.reg, id_="LAB-001", **k)  # número já consumido: não pode compor de novo
        self.assertFalse(r["aprovacao_tecnica"]); self.assertFalse(Path(out).exists())

    def test_lab_nao_consome_numero(self):
        out = str(Path(self.d) / "l.png")
        r = compor_story.compor(None, NA, FORA, "LAB-001", out, simulacao=True)
        self.assertTrue(r["aprovacao_tecnica"]); self.assertEqual([l["numero"] for l in rn.ler(self.reg)[0]], ["", "", ""])


class Composicao(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def test_texto_que_nao_cabe_bloqueia_e_nao_altera_texto(self):
        longo = " ".join(["palavra"] * 60)
        for perfil in ("A", "B"):
            out = str(Path(self.d) / f"{perfil}.png")
            r = compor_story.compor(None, NA, longo, "LAB-001", out, perfil=perfil, simulacao=True)
            self.assertFalse(r["aprovacao_tecnica"]); self.assertFalse(Path(out).exists()); self.assertFalse(r["texto_alterado"])
            self.assertTrue(Path(out + ".checagem.json").exists())

    def test_rascunho_grava_com_faixa_e_continua_reprovada(self):
        out = str(Path(self.d) / "r.png")
        r = compor_story.compor(None, NA, " ".join(["palavra"] * 60), "LAB-001", out, simulacao=True, rascunho=True)
        self.assertFalse(r["aprovacao_tecnica"]); self.assertTrue(Path(out).exists())

    def test_travessao_bloqueia(self):
        r = compor_story.compor(None, NA, "Primeira parte — segunda parte da frase.", "LAB-001", str(Path(self.d) / "t.png"), simulacao=True)
        self.assertFalse(r["aprovacao_tecnica"])

    def test_zona_de_seguranca_bloqueia(self):
        original = dict(compor_story.PERFIS["A"]); compor_story.PERFIS["A"]["assinatura_y"] = 1600
        try:
            r = compor_story.compor(None, NA, FORA, "LAB-001", str(Path(self.d) / "z.png"), simulacao=True)
            self.assertFalse(r["aprovacao_tecnica"]); self.assertTrue(any("zona de segurança inferior" in f for f in r["falhas"]))
        finally:
            compor_story.PERFIS["A"].clear(); compor_story.PERFIS["A"].update(original)

    def test_perfis_a_e_b_aprovados_para_o_caso_do_piloto(self):
        for perfil in ("A", "B"):
            r = compor_story.compor(None, "Um guarda-chuva aberto secando no corredor.", "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar.", "LAB-001", str(Path(self.d) / f"{perfil}.png"), perfil=perfil, simulacao=True)
            self.assertTrue(r["aprovacao_tecnica"], r)


class Integridade(unittest.TestCase):
    def test_skill_integra(self):
        r = subprocess.run([sys.executable, str(SC / "verificar_skill.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
