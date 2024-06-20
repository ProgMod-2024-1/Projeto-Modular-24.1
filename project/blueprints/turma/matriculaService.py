from project.blueprints.turma.turmaService import validaTurma, json
from project.db.database import *


def consultaAuluno(matrAluno):  # mocking
    return {"matricula": matrAluno, "nome": "Aluno Teste"}


def addAlunoTurma(matrAluno: str, codTurma: str, pathToFile) -> dict:
    if not validaTurma(codTurma):
        return {
            "success": 81,
            "message": "Falha turma invalida"
        }

    turmas_data = read_db("turma")
    turma = next((turma for turma in turmas_data if turma["cod_turma"] == codTurma), None)
    if not turma:
        return {
            "success": 71,
            "message": "Falha na adicao turma inexistente"
        }

    aluno = consultaAuluno(matrAluno)
    if aluno == -1:
        return {
            "success": 70,
            "message": "Falha na adicao aluno inexistente"
        }

    turma["alunos"].append({"matrAluno": aluno["matricula"]})
    update_db(turma, "cod_turma", "turma")

    return {
        "success": 6,
        "message": "Sucesso na adicao"
    }


def removeAlunoTurma(matrAluno: str, codTurma: str, pathToFile) -> dict:
    if not validaTurma(codTurma):
        return {
            "success": 111,
            "message": "Falha turma invalida",
        }

    turmas_data = read_db("turma")

    turma = next((turma for turma in turmas_data if turma["cod_turma"] == codTurma), None)
    if not turma:
        return {
            "success": 101,
            "message": "Falha de turma inexistente"
        }

    aluno_index = next((index for index, aluno in enumerate(turma["alunos"])
                        if aluno["matrAluno"] == matrAluno), None)
    if aluno_index is None:
        return {
            "success": 10,
            "message": "Falha de aluno inexistente"
        }

    delete_db(turma["aluno"][aluno_index], "cod_turma", "turma")

    return {
        "success": 9,
        "message": "Sucesso na remoção"
    }
