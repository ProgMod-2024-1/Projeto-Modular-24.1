from project.db import read_db, write_db, update_db, delete_db
import random
#import lista global
alunos = []

ALUNOS_DB_URI = "aluno"

def criaAluno(dadosAluno):
    return write_db(dadosAluno,"matricula",ALUNOS_DB_URI)

def excluiAluno(dadosAluno):
    return delete_db(dadosAluno,"matricula",ALUNOS_DB_URI)

def atualizaAluno(dadosAluno):
    return update_db(dadosAluno,"matricula",ALUNOS_DB_URI)

def consultaAluno(matrAluno: int):
    alunos = consultaTodosAlunos()
    for i,aluno in enumerate(alunos):
        if matrAluno == aluno["matricula"]:
            return aluno
    return None

def consultaTodosAlunos():
    return read_db(ALUNOS_DB_URI)