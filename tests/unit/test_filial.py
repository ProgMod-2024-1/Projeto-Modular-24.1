from project.blueprints.filial.filialService import *

def test_add_filial():
   
   result = add_filiais(nome = "Teste2", endereco="Rua da mentira", cep="22222-222",nAlunos=20)
   assert(result["success"],1)

def test_update_filial():
   ## Update filial com codigo certo
   result = update_filias({"codigo":"01799297","nome": "lalala", "endereco": "teste", "cep": "222", "min_alunos_p_turma": 52, "turmas": {"2024": ["teste"]}})
   assert(result["success"],1)
   
   ## Update filial com codigo errado
   result = update_filias({"codigo":"0","nome": "lalala", "endereco": "teste", "cep": "222", "min_alunos_p_turma": 52, "turmas": {"2024": ["teste"]}})
   assert(result["success"],0)

def test_delete_filial():
   ## Update filial com codigo Errado
   result = delete_filiais("01799297")
   assert(result["success"],1)

   ## Update filial com codigo Certo
   result = delete_filiais("0")
   assert(result["success"],0)