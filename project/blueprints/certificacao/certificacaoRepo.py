import os
from typing import List
from project.db.database import read_db, write_db, update_db, delete_db

CERTIFICACOES_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"database","certificacao.json")

# Retorna todas as certificações presentes no json
def get_all_certificacoes() -> List[object]:
    return read_db(CERTIFICACOES_DB_URI)

# Registra uma nova certificação
def registra_certificacao(novaCert: object) -> int:
    return write_db([novaCert], "info", CERTIFICACOES_DB_URI)

# Retorna uma certificação específica com os dados fornecidos
def seek_certificacao(codCert: str, id_aluno: str, id_formacao: str) -> object:
    data = read_db(CERTIFICACOES_DB_URI)
    for certificacao in data:
        if (certificacao["info"]["codCert"] == codCert and certificacao["info"]["id_aluno"] == id_aluno and certificacao["info"]["id_formacao"] == id_formacao):
            return certificacao
    return None

# Atualiza os dados de uma certificação existente
def muda_certificacao(certAtualizada: object) -> int:
    return update_db(certAtualizada, "info", CERTIFICACOES_DB_URI)
