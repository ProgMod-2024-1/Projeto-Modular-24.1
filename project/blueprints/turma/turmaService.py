from project.blueprints.turma.turmaRepo import geraCodTurma, validaTurma
from project.db.database import *
from project.blueprints.filial.turmasFIlialService import insere_turmasFilial, remove_turmasFilial
import json


def criaTurma(dadosTurma: dict) -> dict:
    turmas_data = read_db("turma")

    nova_turma = {
        "cod_curso": dadosTurma["curso"],
        "matrProf": dadosTurma["matrProf"],
        "horario": dadosTurma["horario"],
        "online": dadosTurma["online"],
        "filial": dadosTurma["filial"],
        "alunos": dadosTurma["alunos"]
    }
    print(nova_turma)

    for turma in turmas_data:
        turma_copy = turma.copy()
        turma_copy.pop("cod_turma")
        if turma_copy == nova_turma:
            return {
                "success": 1,
                "message": "Falha turma ja existente"
            }

    nova_turma["cod_turma"] = geraCodTurma()


    write_db([nova_turma], "cod_turma", "turma")

    return {
        "success": 0,
        "message": "Sucesso na criacao"
    }

def consultaTurma(codTurma: str, pathToFile) -> dict:
    if not validaTurma(codTurma):
        return {
            "success": 5,
            "message": "Falha turma inválida",
            "turma": {}
        }

    turmas_data = read_db("turma")

    turma = next((turma for turma in turmas_data if turma["cod_turma"] == codTurma), None)
    if turma:
        return {
            "success": 3,
            "message": "Sucesso na consulta",
            "turma": turma
        }

    return {
        "success": 4,
        "message": "Falha turma inexistente",
        "turma": {}
    }


def excluiTurma(codTurma: str, pathToFile) -> dict:
    if not validaTurma(codTurma):
        return {
            "success": 5,
            "message": "Falha turma inválida"
        }

    turmas_data = read_db("turma")

    turma = next((turma for turma in turmas_data if turma["cod_turma"] == codTurma), None)
    if not turma:
        return {
            "success": 10,
            "message": "Falha turma inexistente"
        }
    delete_db(turma, "cod_turma", "turma")

    return {
        "success": 9,
        "message": "Sucesso na exclusão"
    }


def atualizaDadosTurma(codTurma: str, dadosTurma: dict, pathToFile) -> dict:
    if not validaTurma(codTurma):
        return {
            "success": 5,
            "message": "Falha turma inválida"
        }

    turmas_data = read_db("turma")

    index = next((i for i, turma in enumerate(turmas_data) if turma["cod_turma"] == codTurma), None)
    if index is None:
        return {
            "success": 7,
            "message": "Falha turma inexistente"
        }

    turmas_data[index].update(dadosTurma)
    update_db(turmas_data[index], "cod_turma", "turma")

    return {
        "success": 6,
        "message": "Sucesso atualização"
    }

