import json
import os
from project.blueprints.certificacao.certificacaoService import get_certificacoes, registra_certificacoes, seek_certificacoes, muda_certificacoes

DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "project", "blueprints", "certificacao", "database", "certificacao.json")

# Dados iniciais para testes
initial_data = [
    {
        "info": {"codCert": "001", "id_aluno": "12345", "id_formacao": "67890"},
        "data_conclusao": "2022-06-01"
    },
    {
        "info": {"codCert": "002", "id_aluno": "54321", "id_formacao": "09876"},
        "data_conclusao": "2022-07-01"
    },
    {
        "info": {"codCert": "003", "id_aluno": "11223", "id_formacao": "33445"},
        "data_conclusao": "2022-08-01"
    }
]

# Carrega os dados originais para restauração após os testes
with open(DB_URI, 'r') as jsonFile:
    original_data = json.load(jsonFile)

# Função para restaurar o banco de dados ao estado original
def restore_db():
    with open(DB_URI, 'w') as jsonFile:
        json.dump(original_data, jsonFile)

# Função para configurar os dados iniciais de teste
def setup_initial_data():
    test_data = {"data": initial_data}
    with open(DB_URI, 'w') as jsonFile:
        json.dump(test_data, jsonFile)

# Teste para get_certificacoes
def test_get_certificacoes():
    print("Iniciando teste: test_get_certificacoes")
    setup_initial_data()
    result = get_certificacoes()
    print("Resultado:", result)
    assert isinstance(result, list), f"Falha no teste: O resultado deve ser uma lista, mas é {type(result)}"
    assert result == initial_data, f"Falha no teste: {result} != {initial_data}"
    print("Teste test_get_certificacoes passou.")

# Teste para registra_certificacoes quando a certificação é criada com sucesso
def test_registra_certificacoes_success():
    print("Iniciando teste: test_registra_certificacoes_success")
    setup_initial_data()
    nova_certificacao = {
        "info": {"codCert": "004", "id_aluno": "22334", "id_formacao": "55667"},
        "data_conclusao": "2022-09-01"
    }
    result = registra_certificacoes(nova_certificacao)
    print("Resultado:", result)
    assert result["success"] == 1, f"Falha no teste: {result['success']} != 1"
    assert result["message"] == "Certificação criada com sucesso", f"Falha no teste: {result['message']} != 'Certificação criada com sucesso'"
    assert result["user"]["id_aluno"] == "22334", f"Falha no teste: {result['user']['id_aluno']} != '22334'"
    assert result["user"]["id_formacao"] == "55667", f"Falha no teste: {result['user']['id_formacao']} != '55667'"
    print("Teste test_registra_certificacoes_success passou.")

# Teste para registra_certificacoes quando a certificação já existe
def test_registra_certificacoes_already_exists():
    print("Iniciando teste: test_registra_certificacoes_already_exists")
    setup_initial_data()
    nova_certificacao = {
        "info": {"codCert": "001", "id_aluno": "12345", "id_formacao": "67890"},
        "data_conclusao": "2022-06-01"
    }
    result = registra_certificacoes(nova_certificacao)
    print("Resultado:", result)
    assert result["success"] == 0, f"Falha no teste: {result['success']} != 0"
    assert result["message"] == "Esta Certificação já existe.", f"Falha no teste: {result['message']} != 'Esta Certificação já existe.'"
    assert result["user"]["id_aluno"] == "12345", f"Falha no teste: {result['user']['id_aluno']} != '12345'"
    assert result["user"]["id_formacao"] == "67890", f"Falha no teste: {result['user']['id_formacao']} != '67890'"
    print("Teste test_registra_certificacoes_already_exists passou.")

# Teste para registra_certificacoes quando ocorre um erro ao criar a certificação
def test_registra_certificacoes_error():
    print("Iniciando teste: test_registra_certificacoes_error")
    # Renomear temporariamente o arquivo de banco de dados para simular "não encontrado"
    temp_db_uri = DB_URI + ".bak"
    os.rename(DB_URI, temp_db_uri)

    nova_certificacao = {
        "info": {"codCert": "005", "id_aluno": "33445", "id_formacao": "77889"},
        "data_conclusao": "2022-10-01"
    }
    try:
        result = registra_certificacoes(nova_certificacao)
    except Exception as e:
        result = {"success": 0, "message": "Ocorreu um erro ao criar a Certificação. Tente novamente mais tarde"}
    
    # Restaurar o nome do arquivo de banco de dados
    os.rename(temp_db_uri, DB_URI)
    
    print("Resultado:", result)
    assert result["success"] == 0, f"Falha no teste: {result['success']} != 0"
    assert result["message"] == "Ocorreu um erro ao criar a Certificação. Tente novamente mais tarde", f"Falha no teste: {result['message']} != 'Ocorreu um erro ao criar a Certificação. Tente novamente mais tarde'"
    assert result["user"]["id_aluno"] == "33445", f"Falha no teste: {result['user']['id_aluno']} != '33445'"
    assert result["user"]["id_formacao"] == "77889", f"Falha no teste: {result['user']['id_formacao']} != '77889'"
    print("Teste test_registra_certificacoes_error passou.")

# Teste para seek_certificacoes quando a certificação é encontrada
def test_seek_certificacoes_found():
    print("Iniciando teste: test_seek_certificacoes_found")
    setup_initial_data()
    codCert = "001"
    id_aluno = "12345"
    id_formacao = "67890"
    result = seek_certificacoes(codCert, id_aluno, id_formacao)
    print("Resultado:", result)
    expected = {
        "info": {"codCert": "001", "id_aluno": "12345", "id_formacao": "67890"},
        "data_conclusao": "2022-06-01"
    }
    assert result == expected, f"Falha no teste: {result} != {expected}"
    print("Teste test_seek_certificacoes_found passou.")

# Teste para seek_certificacoes quando a certificação não é encontrada
def test_seek_certificacoes_not_found():
    print("Iniciando teste: test_seek_certificacoes_not_found")
    setup_initial_data()
    codCert = "999"
    id_aluno = "00000"
    id_formacao = "11111"
    result = seek_certificacoes(codCert, id_aluno, id_formacao)
    print("Resultado:", result)
    expected = None  # Ou pode ser uma mensagem de erro dependendo da implementação
    assert result == expected, f"Falha no teste: {result} != {expected}"
    print("Teste test_seek_certificacoes_not_found passou.")

# Teste para muda_certificacoes quando a certificação é atualizada com sucesso
def test_muda_certificacoes_success():
    print("Iniciando teste: test_muda_certificacoes_success")
    setup_initial_data()
    certificacao_atualizada = {
        "info": {"codCert": "001", "id_aluno": "12345", "id_formacao": "67890"},
        "data_conclusao": "2023-01-01"
    }
    result = muda_certificacoes(certificacao_atualizada)
    print("Resultado:", result)
    assert result["success"] == 1, f"Falha no teste: {result['success']} != 1"
    assert result["message"] == "Certificação alterada com sucesso", f"Falha no teste: {result['message']} != 'Certificação alterada com sucesso'"
    assert result["user"]["id_aluno"] == "12345", f"Falha no teste: {result['user']['id_aluno']} != '12345'"
    assert result["user"]["id_formacao"] == "67890", f"Falha no teste: {result['user']['id_formacao']} != '67890'"

    # Verifica se a certificação foi atualizada
    certificacao = seek_certificacoes("001", "12345", "67890")
    assert certificacao["data_conclusao"] == "2023-01-01", f"Falha no teste: {certificacao['data_conclusao']} != '2023-01-01'"
    print("Teste test_muda_certificacoes_success passou.")

# Chamando os testes
if __name__ == "__main__":
    try:
        setup_initial_data()
        test_get_certificacoes()
        test_registra_certificacoes_success()
        test_registra_certificacoes_already_exists()
        test_registra_certificacoes_error()
        test_seek_certificacoes_found()
        test_seek_certificacoes_not_found()
        test_muda_certificacoes_success()
        print("Todos os testes passaram.")
    finally:
        restore_db()
        print("Banco de dados restaurado ao estado original.")
