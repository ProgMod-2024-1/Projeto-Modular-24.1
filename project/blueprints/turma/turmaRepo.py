from project.db.database import read_db
import os


TURMA_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "turma.json")


def validaTurma(codTurma: str) -> bool:
    return codTurma.isdigit()


def geraCodTurma() -> str:
    turmas = read_db(TURMA_DB_URI)
    if not turmas:
        return "1"
    elif turmas == -4:
        return -1
    ultimoCod = int(turmas[-1]["cod_turma"])
    return str(ultimoCod + 1)
