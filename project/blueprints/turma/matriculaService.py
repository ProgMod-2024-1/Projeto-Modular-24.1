from project.blueprints.turma.turmaService import validaTurma, json


def consultaAuluno(matrAluno):  # mocking
    return {"matricula": matrAluno, "nome": "Aluno Teste"} if matrAluno == "VALIDO" else -1


def addAlunoTurma(matrAluno: str, codTurma: str, pathToFile) -> dict:
    if not validaTurma(codTurma):
        return {
            "success": 81,
            "message": "Falha turma inválida"
        }

    with open(pathToFile, mode="r") as jsonFile:
        turmas_data = json.load(jsonFile)

    turma = next((turma for turma in turmas_data["data"] if turma["cod_turma"] == codTurma), None)
    if not turma:
        return {
            "success": 71,
            "message": "Falha na adição turma inexistente"
        }

    aluno = consultaAuluno(matrAluno)
    if aluno == -1:
        return {
            "success": 70,
            "message": "Falha na adição aluno inexistente"
        }

    turma["alunos"].append(aluno)

    with open(pathToFile, mode="w") as jsonFile:
        json.dump(turmas_data, jsonFile, indent=4)

    return {
        "success": 6,
        "message": "Sucesso na adição"
    }


def removeAlunoTurma(matrAluno: str, codTurma: str, pathToFile) -> dict:
    with open(pathToFile, mode="r") as jsonFile:
        turmas_data = json.load(jsonFile)

    if not validaTurma(codTurma):
        return {
            "success": 111,
            "message": "Falha turma inválida",
        }

    turma = next((turma for turma in turmas_data["data"] if turma["cod_turma"] == codTurma), None)
    if not turma:
        return {
            "success": 101,
            "message": "Falha de turma inexistente"
        }

    aluno_index = next((index for index, aluno in enumerate(turma["alunos"])
                        if aluno["matricula"] == matrAluno), None)
    if aluno_index is None:
        return {
            "success": 10,
            "message": "Falha de aluno inexistente"
        }

    turma["alunos"].pop(aluno_index)

    with open(pathToFile, mode="w") as jsonFile:
        json.dump(turmas_data, jsonFile, indent=4)

    return {
        "success": 9,
        "message": "Sucesso na remoção"
    }

