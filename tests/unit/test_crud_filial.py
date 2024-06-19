from project.main import app
from project.blueprints.filial.filialRepo import get_all_filiais
from project.blueprints.filial.filialRepo import add_filial, update_filial, delete_filial, get_filial


def test_principal_endpoint():
    # Simulate a GET request to the /principal endpoint
    response = app.test_client().get("/principal")

    print(f"URL: {response.request.url}")
    print(f"Status Code: {response.status_code}")

    # Assert that the response status code is 200
    assert response.status_code == 308

def test_add_filiais_success():
    result = add_filial("12345678", "Nova Filial", "Rua Nova, 123", "12345-678", 10)
    assert result == 1

def test_update_filias_success():
    data = {
        "codigo": "12345678",
        "nome": "Novo Nome Filial",
        "endereco": "Nova Rua, 789",
        "cep": "54321-098",
        "min_alunos_p_turma": 25,
        "turmas": {"2024": []}
    }
    result = update_filial(data)
    assert result == 1

def test_delete_filiais_success():
    codigo = "12345678"
    result = delete_filial(codigo)
    assert result == 1

def test_get_filiais():
    filial_name = "Some Filial Name"
    result = get_filial(filial_name)
    assert result is not None