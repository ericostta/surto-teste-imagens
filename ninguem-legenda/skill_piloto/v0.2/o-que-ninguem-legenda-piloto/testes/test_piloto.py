#!/usr/bin/env python3
"""Testes reproduzíveis da skill (PILOTO v0.2). Executar a partir da pasta da skill: python3 testes/test_piloto.py
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
import medir_inclinacao
from PIL import Image, ImageDraw

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
            r = compor_story.compor(None, NA, FORA, "LAB-001", str(Path(self.d) / "z.png"), perfil="A", simulacao=True)
            self.assertFalse(r["aprovacao_tecnica"]); self.assertTrue(any("zona de segurança inferior" in f for f in r["falhas"]))
        finally:
            compor_story.PERFIS["A"].clear(); compor_story.PERFIS["A"].update(original)

    def test_perfis_a_b_e_c_aprovados_para_o_caso_do_piloto(self):
        for perfil in ("A", "B", "C"):
            r = compor_story.compor(None, "Um guarda-chuva aberto secando no corredor.", "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar.", "LAB-001", str(Path(self.d) / f"{perfil}.png"), perfil=perfil, simulacao=True)
            self.assertTrue(r["aprovacao_tecnica"], r)


FOTO_NA = "Um guarda-chuva aberto secando no corredor."
FOTO_FORA = "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar."


def foto_sintetica(cor, caminho):
    Image.new("RGB", (941, 1672), cor).save(caminho)
    return caminho


class PerfilCNumeroSutil(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def test_perfil_padrao_e_c(self):
        self.assertEqual(compor_story.PERFIL_PADRAO, "C")

    def test_numero_abaixo_da_assinatura_a_esquerda_e_menor(self):
        L = compor_story.PERFIS["C"]
        r = compor_story.compor(None, FOTO_NA, FOTO_FORA, "LAB-001", str(Path(self.d) / "c.png"), perfil="C", simulacao=True)
        self.assertTrue(r["aprovacao_tecnica"], r)
        n, s = r["caixas"]["numero"], r["caixas"]["assinatura"]
        self.assertEqual(round(n[0]), L["margem"]); self.assertEqual(round(s[0]), L["margem"])      # alinhados à esquerda
        self.assertGreaterEqual(n[1], s[1] + L["assinatura_px"])                                      # abaixo da assinatura
        self.assertLess(L["numero_px"], L["assinatura_px"])                                           # menor que a assinatura
        self.assertLessEqual(n[3], 1920 - L["zona_base"])                                             # dentro da zona de segurança
        self.assertEqual(L["assinatura_px"], 22); self.assertEqual(L["numero_px"], 11)

    def test_numero_nao_aparece_no_topo_no_perfil_c(self):
        r = compor_story.compor(None, FOTO_NA, FOTO_FORA, "LAB-001", str(Path(self.d) / "c.png"), perfil="C", simulacao=True)
        self.assertGreater(r["caixas"]["numero"][1], 1400)

    def test_perfis_a_e_b_mantem_numero_no_topo_a_direita(self):
        for perfil in ("A", "B"):
            r = compor_story.compor(None, FOTO_NA, FOTO_FORA, "LAB-001", str(Path(self.d) / f"{perfil}.png"), perfil=perfil, simulacao=True)
            self.assertLess(r["caixas"]["numero"][1], 400)
            self.assertAlmostEqual(r["caixas"]["numero"][2], 1080 - compor_story.PERFIS[perfil]["margem"], delta=2)

    def test_numero_real_exibido_sem_n_e_exige_reserva(self):
        reg = str(Path(self.d) / "registro_piloto.csv")
        escrever(reg, [linha("LAB-001", "TEXTO_APROVADO", na_foto="a", fora_do_enquadramento="b c")])
        out = str(Path(self.d) / "r.png")
        r = compor_story.compor(None, FOTO_NA, FOTO_FORA, "001", out, perfil="C", simulacao=True, registro=reg, id_="LAB-001")
        self.assertFalse(r["aprovacao_tecnica"])                                                      # sem reserva: bloqueia
        rn.main(["reservar", "--id", "LAB-001", "--registro", reg])
        r = compor_story.compor(None, FOTO_NA, FOTO_FORA, "001", out, perfil="C", simulacao=True, registro=reg, id_="LAB-001")
        self.assertTrue(r["aprovacao_tecnica"], r); self.assertEqual(r["numero_exibido"], "001")
        self.assertNotIn("Nº", json.dumps(r, ensure_ascii=False))
        self.assertNotIn("Nº", (RAIZ / "scripts/compor_story.py").read_text(encoding="utf-8").split("def compor")[1])


class ContrasteEfetivo(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def test_sem_foto_nao_mede(self):
        r = compor_story.compor(None, FOTO_NA, FOTO_FORA, "LAB-001", str(Path(self.d) / "s.png"), simulacao=True)
        self.assertIsNone(r["contraste"])

    def test_foto_clara_gera_aviso_e_nao_bloqueia(self):
        f = foto_sintetica((235, 235, 230), str(Path(self.d) / "clara.png"))
        r = compor_story.compor(f, FOTO_NA, FOTO_FORA, "LAB-001", str(Path(self.d) / "c.png"), perfil="C", simulacao=True)
        self.assertTrue(r["aprovacao_tecnica"])                                                       # contraste é aviso, nunca bloqueio
        self.assertTrue(any(v["abaixo_do_limite"] for v in r["contraste"].values()))
        self.assertTrue(any("contraste efetivo" in a for a in r["avisos"]))

    def test_foto_escura_nao_gera_aviso_de_contraste(self):
        f = foto_sintetica((25, 25, 28), str(Path(self.d) / "escura.png"))
        r = compor_story.compor(f, FOTO_NA, FOTO_FORA, "LAB-001", str(Path(self.d) / "e.png"), perfil="C", simulacao=True)
        self.assertFalse(any(v["abaixo_do_limite"] for v in r["contraste"].values()), r["contraste"])
        self.assertEqual(set(r["contraste"]), {"titulo", "numero", "rotulo NA FOTO", "NA FOTO texto", "rotulo FORA", "FORA texto", "assinatura"})


class Inclinacao(unittest.TestCase):
    def linha_escura(self, x_topo, x_base):
        im = Image.new("L", (400, 700), 200); d = ImageDraw.Draw(im)
        d.line([(x_topo, 100), (x_base, 600)], fill=10, width=6)
        p = str(Path(tempfile.mkdtemp()) / "h.png"); im.save(p); return p

    def test_haste_vertical(self):
        r = medir_inclinacao.medir(self.linha_escura(200, 200), 200, 100, 200, 600, "esquerda")
        self.assertEqual(r["sentido"], "praticamente vertical"); self.assertLessEqual(r["graus_com_a_vertical"], 3)

    def test_topo_em_direcao_a_parede_esquerda_e_afastado(self):
        p = self.linha_escura(150, 250)                                   # topo mais à esquerda
        r = medir_inclinacao.medir(p, 150, 100, 250, 600, "esquerda")
        self.assertEqual(r["sentido"], "topo em direção à parede"); self.assertAlmostEqual(r["graus_com_a_vertical"], 11.3, delta=1.5)
        self.assertEqual(medir_inclinacao.medir(p, 150, 100, 250, 600, "direita")["sentido"], "topo afastado da parede")

    def test_sem_pixels_escuros_falha_com_mensagem(self):
        p = str(Path(tempfile.mkdtemp()) / "vazio.png"); Image.new("L", (400, 700), 200).save(p)
        with self.assertRaises(ValueError): medir_inclinacao.medir(p, 200, 100, 200, 600, "esquerda")


class PadraoFotograficoEConfig(unittest.TestCase):
    def setUp(self):
        self.cfg = json.loads((SC / "config.json").read_text(encoding="utf-8"))

    def test_padrao_fotografico_provisorio_e_limites(self):
        pf = self.cfg["padrao_fotografico"]
        self.assertIn("provisoria", pf["status"]); self.assertEqual(pf["resultados"], ["APTA", "AJUSTAR", "REFAZER"])
        self.assertEqual(len(pf["defeitos_impeditivos"]), 9)
        self.assertEqual(pf["contraste_limites_provisorios"], {"blocos_media": 4.5, "blocos_pior_decil": 3.0, "discretos_media": 3.0})

    def test_limite_de_duas_correcoes_com_excecao_documentada(self):
        r = self.cfg["rodadas"]
        self.assertEqual(r["max_geracoes_imagem_por_texto"], 2); self.assertTrue(r["excecao_ao_limite_exige_autorizacao_expressa_de_eri_registrada"])

    def test_gerador_de_imagem_nao_exclusivo(self):
        textos = (RAIZ / "SKILL.md").read_text(encoding="utf-8") + (RAIZ / "references/prompt_fotografico.md").read_text(encoding="utf-8")
        self.assertIn("nenhum é exigido", textos)
        self.assertNotIn("Eri gera a foto manualmente** no Gemini/Nano Banana.", textos)

    def test_controles_preservados(self):
        self.assertEqual(self.cfg["versao_critico"], "v2.2"); self.assertFalse(self.cfg["critico_consultivo"]["homologada"])
        self.assertEqual(self.cfg["historico"]["janela_mecanismo"], 5); self.assertEqual(self.cfg["historico"]["janela_emocao"], 30)
        self.assertEqual(self.cfg["limites_texto"]["fora_max_palavras"], 22)
        self.assertEqual(SHA(RAIZ / "references/critico_v2_2_referencia.md"), "468fd3823f83909dd87127d7a4affd835df4be09c7601e62c37b38dc54b553a3")

    def test_proibicoes_continuam_no_skill_md(self):
        sk = (RAIZ / "SKILL.md").read_text(encoding="utf-8").lower()
        for chave in ("não integrar ao n8n", "não inserir na fila", "não alterar a grade", "não publicar", "não modificar o contador real", "não promover a candidata C1b", "não executar as 72 avaliações"):
            self.assertIn(chave.lower(), sk)


class Integridade(unittest.TestCase):
    def test_skill_integra(self):
        r = subprocess.run([sys.executable, str(SC / "verificar_skill.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
