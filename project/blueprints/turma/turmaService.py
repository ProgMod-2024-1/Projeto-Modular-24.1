from project.blueprints.turma.turmaRepo import geraCodTurma, validaTurma
import json


def criaTurma(dadosTurma: dict, pathToFile) -> dict:
    with open(pathToFile, mode="r") as jsonFile:
        turmas_data = json.load(jsonFile)

    nova_turma = {
        "cod_curso": dadosTurma["cod_curso"],
        "professor": dadosTurma["professor"],
        "horario": dadosTurma["horario"],
        "online": dadosTurma["online"],
        "filia": dadosTurma["filia"],
        "matricula_aluno": dadosTurma["matricula_aluno"]
    }

    for turma in turmas_data["data"]:
        turma_copy = turma.copy()
        turma_copy.pop("cod_turma")
        if turma_copy == nova_turma:
            return {
                "success": 1,
                "message": "Falha turma já existente"
            }

    nova_turma["cod_turma"] = geraCodTurma()
    turmas_data["data"].append(nova_turma)

    with open(pathToFile, mode="w") as jsonFile:
        json.dump(turmas_data, jsonFile, indent=4)

    return {
        "success": 0,
        "message": "Sucesso na criação"
    }


def consultaTurma(codTurma: str, pathToFile) -> dict:
    if not validaTurma(codTurma):
        return {
            "success": 5,
            "message": "Falha turma inválida",
            "turma": {}
        }

    with open(pathToFile, mode="r") as jsonFile:
        turmas_data = json.load(jsonFile)


    turma = next((turma for turma in turmas_data["data"] if turma["cod_turma"] == codTurma), None)
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

    with open(pathToFile, mode="r") as jsonFile:
        turmas_data = json.load(jsonFile)

    turma = next((turma for turma in turmas_data["data"] if turma["cod_turma"] == codTurma), None)
    if not turma:
        return {
            "success": 10,
            "message": "Falha turma inexistente"
        }
    turmas_data["data"].remove(turma)

    with open(pathToFile, mode="w") as jsonFile:
        json.dump(turmas_data, jsonFile, indent=4)

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

    with open(pathToFile, mode="r") as jsonFile:
        turmas_data = json.load(jsonFile)

    index = next((i for i, turma in enumerate(turmas_data["data"]) if turma["cod_turma"] == codTurma), None)
    if index is None:
        return {
            "success": 7,
            "message": "Falha turma inexistente"
        }

    turmas_data["data"][index].update(dadosTurma)

    with open(pathToFile, mode="w") as jsonFile:
        json.dump(turmas_data, jsonFile, indent=4)

    return {
        "success": 6,
        "message": "Sucesso atualização"
    }

