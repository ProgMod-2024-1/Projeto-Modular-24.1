import unittest
from project.blueprints.lista_de_espera.listaDeEsperaService import cria_lista_espera_service, consulta_lista_espera_service, add_aluno_lista_espera_service, remove_aluno_lista_espera_service, exclui_lista_espera_service

class TestListaEsperaService(unittest.TestCase):

    def setUp(self):
        self.service = ListaEsperaService()

    def test_verificaSeAlocaOnline_aloca_online(self):
        result = self.service.verificaSeAlocaOnline("LE123")
        self.assertEqual(result, 1)

    def test_verificaSeAlocaOnline_nao_aloca_tempo_nao_atingido(self):
        result = self.service.verificaSeAlocaOnline("LE123")
        self.assertEqual(result, 0)

    def test_verificaSeAlocaOnline_nao_aloca_lista_vazia(self):
        result = self.service.verificaSeAlocaOnline("LE123")
        self.assertEqual(result, 0)

    def test_verificaSeAlocaOnline_lista_inexistente(self):
        result = self.service.verificaSeAlocaOnline("LE999")
        self.assertEqual(result, -1)

    def test_rotinaVerificaSeAlocaOnline_sucesso_com_alocacao(self):
        result = self.service.rotinaVerificaSeAlocaOnline()
        self.assertGreater(result, 0)

    def test_rotinaVerificaSeAlocaOnline_sucesso_sem_alocacao(self):
        result = self.service.rotinaVerificaSeAlocaOnline()
        self.assertEqual(result, 0)

    def test_rotinaVerificaSeAlocaOnline_falha_consulta(self):
        result = self.service.rotinaVerificaSeAlocaOnline()
        self.assertEqual(result, -1)

    def test_addAlunoListEsp_sucesso_adicao(self):
        result = self.service.addAlunoListEsp(12345, "LE123")
        self.assertEqual(result, 9)

    def test_addAlunoListEsp_falha_aluno_inexistente(self):
        result = self.service.addAlunoListEsp(99999, "LE123")
        self.assertEqual(result, 70)

    def test_addAlunoListEsp_falha_lista_inexistente(self):
        result = self.service.addAlunoListEsp(12345, "LE999")
        self.assertEqual(result, 71)

    def test_addAlunoListEsp_falha_aluno_invalido(self):
        result = self.service.addAlunoListEsp(-1, "LE123")
        self.assertEqual(result, 80)

    def test_addAlunoListEsp_falha_lista_invalida(self):
        result = self.service.addAlunoListEsp(12345, "LE_INVALID")
        self.assertEqual(result, 81)

    def test_removeAlunoListEsp_sucesso_exclusao(self):
        result = self.service.removeAlunoListEsp(12345, "LE123")
        self.assertEqual(result, 9)

    def test_removeAlunoListEsp_falha_aluno_inexistente(self):
        result = self.service.removeAlunoListEsp(99999, "LE123")
        self.assertEqual(result, 100)

    def test_removeAlunoListEsp_falha_lista_inexistente(self):
        result = self.service.removeAlunoListEsp(12345, "LE999")
        self.assertEqual(result, 101)

    def test_removeAlunoListEsp_falha_aluno_invalido(self):
        result = self.service.removeAlunoListEsp(-1, "LE123")
        self.assertEqual(result, 110)

    def test_removeAlunoListEsp_falha_lista_invalida(self):
        result = self.service.removeAlunoListEsp(12345, "LE_INVALID")
        self.assertEqual(result, 111)

    def test_consultaListEsp_sucesso_consulta(self):
        result = self.service.consultaListEsp("LE123")
        self.assertEqual(result, 3)

    def test_consultaListEsp_falha_lista_inexistente(self):
        result = self.service.consultaListEsp("LE999")
        self.assertEqual(result, 4)

    def test_consultaListEsp_falha_lista_invalida(self):
        result = self.service.consultaListEsp("LE_INVALID")
        self.assertEqual(result, 5)

    def test_excluiListEsp_sucesso_exclusao_sem_criaTurma(self):
        result = self.service.excluiListEsp("LE123", False)
        self.assertEqual(result, 9)

    def test_excluiListEsp_sucesso_exclusao_com_criaTurma(self):
        result = self.service.excluiListEsp("LE123", True)
        self.assertEqual(result, 9)

    def test_excluiListEsp_falha_lista_inexistente_sem_criaTurma(self):
        result = self.service.excluiListEsp("LE999", False)
        self.assertEqual(result, 10)

    def test_excluiListEsp_falha_lista_inexistente_com_criaTurma(self):
        result = self.service.excluiListEsp("LE999", True)
        self.assertEqual(result, 10)

    def test_excluiListEsp_falha_lista_invalida_sem_criaTurma(self):
        result = self.service.excluiListEsp("LE_INVALID", False)
        self.assertEqual(result, 11)

    def test_excluiListEsp_falha_lista_invalida_com_criaTurma(self):
        result = self.service.excluiListEsp("LE_INVALID", True)
        self.assertEqual(result, 11)

    def test_criaListEsp_sucesso_criacao(self):
        result = self.service.criaListEsp("CS101", 10001, "Gavea", "09:00")
        self.assertEqual(result, 0)

    def test_criaListEsp_falha_lista_ja_existente(self):
        result = self.service.criaListEsp("CS101", 10001, "Main", "09:00")
        self.assertEqual(result, 1)

    def test_criaListEsp_falha_dados_invalidos(self):
        result = self.service.criaListEsp("", -1, "", "")
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
