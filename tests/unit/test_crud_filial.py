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



# Caso de teste 1: Adição de uma nova filial com sucesso
def test_add_filiais_success():
    nome = "Nova Filial"
    endereco = "Rua Nova, 123"
    cep = "12345-678"
    nAlunos = 50

    result = add_filial(nome, endereco, cep, nAlunos)

    assert result["success"] == 1
    assert result["message"] == "Filial criada com sucesso"

# Caso de teste 2: Tentativa de adicionar uma filial que já existe
def test_add_filiais_duplicate():
    # Vamos assumir que a filial com esses dados já existe no banco de dados
    nome = "Filial Existente"
    endereco = "Rua Existente, 456"
    cep = "98765-432"
    nAlunos = 30

    result = add_filial(nome, endereco, cep, nAlunos)

    assert result["success"] == 0
    assert result["message"] == "Esta filial ja existe. Tente novamente com outro nome"

# Caso de teste 3: Tentativa de adicionar uma filial com dados inválidos
def test_add_filiais_invalid_data():
    nome = ""
    endereco = "Rua Sem Nome"
    cep = "12345-678"
    nAlunos = 10

    result = add_filial(nome, endereco, cep, nAlunos)

    assert result["success"] == 0
    assert result["message"] == "Ocorreu um erro ao criar a filial. Tente novamente mais tarde"

# Caso de teste 1: Atualização de uma filial existente com sucesso
def test_update_filias_success():
    data = {
        "codigoFilialEditada": "12345678",
        "nomeFilialEditada": "Novo Nome Filial",
        "enderecoFilialEditada": "Nova Rua, 789",
        "cepFilialEditada": "54321-098",
        "numeroDeAlunosFilialEditada": "25",
        "nomeFilialVelha": "Nome Antigo Filial",
        "enderecoFilialVelha": "Rua Antiga, 456",
        "cepFilialVelha": "12345-678",
        "numeroDeAlunosFilialVelha": "20"
    }

    result = update_filial(data)

    assert result["success"] == 1
    assert result["message"] == "Filial editada com sucesso"

# Caso de teste 2: Tentativa de atualizar uma filial que não existe
def test_update_filias_filial_nao_existe():
    data = {
        "codigoFilialEditada": "88888888",
        "nomeFilialEditada": "Nome Inexistente",
        "enderecoFilialEditada": "Rua Inexistente, 999",
        "cepFilialEditada": "00000-000",
        "numeroDeAlunosFilialEditada": "30",
        "nomeFilialVelha": "Nome Antigo Filial",
        "enderecoFilialVelha": "Rua Antiga, 456",
        "cepFilialVelha": "12345-678",
        "numeroDeAlunosFilialVelha": "20"
    }

    result = update_filial(data)

    assert result["success"] == 0
    assert result["message"] == "Ocorreu um erro ao editar a filial. Tente novamente mais tarde"


    # Importações necessárias para simular o contexto
from project.blueprints.filial.filialRepo import delete_filial

# Caso de teste 1: Remoção de uma filial existente com sucesso
def test_delete_filiais_success():
    codigo = "12345678"

    result = delete_filial(codigo)

    assert result["success"] == 1
    assert result["message"] == "Filial removida com sucesso"

# Caso de teste 2: Tentativa de remover uma filial que não existe
def test_delete_filiais_filial_nao_existe():
    codigo = "88888888"

    result = delete_filial(codigo)

    assert result["success"] == 0
    assert result["message"] == "Ocorreu um erro ao deletar a filial. Tente novamente mais tarde"


# Importações necessárias para simular o contexto
from project.blueprints.filial.filialRepo import get_all_filiais

# Caso de teste: Verificar se a função retorna uma lista de filiais
def test_get_filiais():
    result = get_filial()

    assert isinstance(result, list)
    for filial in result:
        assert isinstance(filial, dict)
        assert "codigo" in filial
        assert "nome" in filial
        assert "endereco" in filial
        assert "cep" in filial
        assert "min_alunos_p_turma" in filial
