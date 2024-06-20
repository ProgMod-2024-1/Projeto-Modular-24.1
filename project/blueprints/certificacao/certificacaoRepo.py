import os
from typing import List
from project.db.database import read_db, write_db, update_db, delete_db

# Retorna todas as certificações presentes no json
def get_all_certificacoes() -> List[object]:
    return read_db("certificacao")

# Registra uma nova certificação
def registra_certificacao(novaCert: object) -> int:
    return write_db([novaCert], "codAluno", "certificacao")

# Retorna um aluno e suas certificações
def seek_certificacoes_aluno(codAluno: str) -> object:
    data = read_db("certificacao")
    for certificacao in data:
        if (certificacao["codAluno"] == codAluno):
            return certificacao
    return None

# Atualiza os dados de uma certificação existente
def muda_certificacao(certAtualizada: object) -> int:
    return update_db(certAtualizada, "codAluno", "certificacao")

# Retorna uma certificação específica com os dados fornecidos
def seek_certificacao(codAluno: str, formacao: str) -> object:
    data = read_db("certificacao")
    for certificacao in data:
        if (certificacao["codAluno"] == codAluno):
            for certificado in certificacao["certificados"]:
                if (certificado["formacao"] == formacao):
                    return certificado
    return None

