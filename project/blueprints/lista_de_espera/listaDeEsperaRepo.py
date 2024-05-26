import os
import json
from project.db.database import read_db, write_db, update_db, delete_db

USERS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "lista_de_espera.json")

def lista_espera_existe(codLE):
    listas_espera = read_db(USERS_DB_URI)
    return any(le["codLE"] == codLE for le in listas_espera)


def cria_lista_espera(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
    lista = {
        "codLE": codLE,
        "filial": filial,
        "curso": curso,
        "horario": horario,
        "matrProf": matrProf,
        "numMinimo": numMinimo,
        "tempo_desde_ultima_adicao": tempo_desde_ultima_adicao,
        "alunos": []
    }
    return write_db([lista], "codLE", USERS_DB_URI)

def consulta_lista_espera(codLE):
    listas_espera = read_db(USERS_DB_URI)
    for le in listas_espera:
        if le["codLE"] == codLE:
            return le
    return {}


def aluno_existe(matrAluno):
    return True


def add_aluno_lista_espera(matrAluno, codLE):
    listas_espera = read_db(USERS_DB_URI)
    for le in listas_espera:
        if le["codLE"] == codLE:
            if matrAluno not in le["alunos"]:
                le["alunos"].append(matrAluno)
                return update_db(le, "codLE", USERS_DB_URI)
            return 80  # Aluno ja esta na lista
    return 71  # Lista de espera nao encontrada


def remove_aluno_lista_espera(matrAluno, codLE):
    listas_espera = read_db(USERS_DB_URI)
    for le in listas_espera:
        if le["codLE"] == codLE:
            if matrAluno in le["alunos"]:
                le["alunos"].remove(matrAluno)
                return update_db(le, "codLE", USERS_DB_URI)
            return 100  # Aluno nao esta na lista
    return 101  # Lista de espera nao encontrada

def exclui_lista_espera(codLE, cria_turma):
    listas_espera = read_db(USERS_DB_URI)
    for le in listas_espera:
        if le["codLE"] == codLE:
            return delete_db(le, "codLE", USERS_DB_URI)
    return 10  # Lista de espera nao encontrada





