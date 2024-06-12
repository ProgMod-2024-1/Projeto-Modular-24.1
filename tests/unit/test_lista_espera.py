import os
import json
from project.blueprints.lista_de_espera.listaDeEsperaService import *
from project.db.database import read_db, write_db, update_db, delete_db

# Caminho do banco de dados JSON
USERS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "project", "blueprints", "lista_de_espera", "database", "lista_de_espera.json")

# Funcao auxiliar para limpar o banco de dados JSON
def limpar_banco_de_dados():
    with open(USERS_DB_URI, 'w') as jsonFile:
        json.dump({"data": []}, jsonFile)

def test_cria_lista_espera():
    limpar_banco_de_dados()
    result = cria_lista_espera_service("LE123", "Filial1", "Curso1", "10:00", 101, 5, 0)
    assert result == 1  # Sucesso

    # Tentar criar uma lista de espera ja existente
    result = cria_lista_espera_service("LE123", "Filial1", "Curso1", "10:00", 101, 5, 0)
    assert result == -1  # Lista de espera ja existe

def test_consulta_lista_espera():
    limpar_banco_de_dados()
    # Consultar lista de espera inexistente
    result = consulta_lista_espera_service("LE999")
    assert result == 10  # Lista inexistente

    # Criar e consultar lista de espera existente
    cria_lista_espera_service("LE123", "Filial1", "Curso1", "10:00", 101, 5, 0)
    result = consulta_lista_espera_service("LE123")
    assert result["codLE"] == "LE123"

def test_add_aluno_lista_espera():
    limpar_banco_de_dados()
    # Adicionar aluno a uma lista de espera inexistente
    result = add_aluno_lista_espera_service(12345, "LE999")
    assert result == 71  # Lista de espera inexistente

    # Adicionar aluno inexistente a uma lista de espera existente //FALTA FAZER O RETORNO PARA ALUNO INEXISTENTE
    # cria_lista_espera_service("LE123", "Filial1", "Curso1", "10:00", 101, 5, 0)
    # result = add_aluno_lista_espera_service(99999, "LE123")
    # assert result == 70  # Aluno inexistente

    # Adicionar aluno valido a uma lista de espera existente
    # Aqui estamos assumindo que o mock de aluno_existe_repo esta configurado para retornar True para o teste
    aluno_existe_repo = lambda matrAluno: True
    result = add_aluno_lista_espera_service(12345, "LE123")
    assert result == 1  # Sucesso

    # Tentar adicionar o mesmo aluno novamente
    result = add_aluno_lista_espera_service(12345, "LE123")
    assert result == 80  # Aluno ja esta na lista

def test_remove_aluno_lista_espera():
    limpar_banco_de_dados()
    # Remover aluno de uma lista de espera inexistente
    result = remove_aluno_lista_espera_service(12345, "LE999")
    assert result == 101  # Lista de espera inexistente

    # Remover aluno inexistente de uma lista de espera existente
    cria_lista_espera_service("LE123", "Filial1", "Curso1", "10:00", 101, 5, 0)
    result = remove_aluno_lista_espera_service(99999, "LE123")
    assert result == 100  # Aluno inexistente

    # Adicionar e remover aluno de uma lista de espera existente
    aluno_existe_repo = lambda matrAluno: True
    add_aluno_lista_espera_service(12345, "LE123")
    result = remove_aluno_lista_espera_service(12345, "LE123")
    assert result == 1  # Sucesso

def test_exclui_lista_espera():
    limpar_banco_de_dados()
    # Excluir uma lista de espera inexistente
    result = exclui_lista_espera_service("LE999", True)
    assert result == 10  # Lista de espera inexistente

    # Criar e excluir uma lista de espera existente
    cria_lista_espera_service("LE123", "Filial1", "Curso1", "10:00", 101, 5, 0)
    result = exclui_lista_espera_service("LE123", True)
    assert result == 1  # Sucesso

if __name__ == '__main__':
    test_cria_lista_espera()
    test_consulta_lista_espera()
    test_add_aluno_lista_espera()
    test_remove_aluno_lista_espera()
    test_exclui_lista_espera()
