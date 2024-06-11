import os
import json
from project.db.database import read_db, write_db, update_db, delete_db

USERS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "lista_de_espera.json")

def lista_espera_existe_repo(codLE):
    listas_espera = read_db(USERS_DB_URI)
    if isinstance(listas_espera, list):
        return any(lista_espera["codLE"] == codLE for lista_espera in listas_espera)
    return False

def cria_lista_espera_repo(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
    if lista_espera_existe_repo(codLE):
        return 1  # Lista de espera já existe // database.py >write_db->return == -1
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

def consulta_lista_espera_repo(codLE):
    listas_espera = read_db(USERS_DB_URI)
    if isinstance(listas_espera, list):
        for lista_espera in listas_espera:
            if lista_espera["codLE"] == codLE:
                return lista_espera
    return {}

def aluno_existe_repo(matrAluno):
    # ver se aluno existe no banco de dados, nn na lista de espera
    #sucesso -> return True // database.py >read_db->return == 1
    #falha -> return False // database.py >read_db->return == -1
    #falha: nao achou banco de dados-> return False // database.py >read_db->return == -4
    return True

def add_aluno_lista_espera_repo(matrAluno, codLE):
    listas_espera = read_db(USERS_DB_URI)
    if isinstance(listas_espera, list):
        for lista_espera in listas_espera:
            if lista_espera["codLE"] == codLE:
                if matrAluno not in lista_espera["alunos"]:
                    lista_espera["alunos"].append(matrAluno)
                    return update_db(lista_espera, "codLE", USERS_DB_URI)
                return 80  # Aluno já está na lista // database.py >write_db->return == -1

    return 71  # Lista de espera não encontrada // database.py >update_dp->return == -4

def remove_aluno_lista_espera_repo(matrAluno, codLE):
    listas_espera = read_db(USERS_DB_URI)
    if isinstance(listas_espera, list):
        for lista_espera in listas_espera:
            if lista_espera["codLE"] == codLE:
                if matrAluno in lista_espera["alunos"]:
                    lista_espera["alunos"].remove(matrAluno)
                    return update_db(lista_espera, "codLE", USERS_DB_URI) #sucesso // database.py >update->return == 1
                return 100  # Aluno não está na lista // database.py >update->return == -1
    return 101  # Lista de espera não encontrada // database.py >update_dp->return == -1

def exclui_lista_espera_repo(codLE, cria_turma):
    listas_espera = read_db(USERS_DB_URI)
    if isinstance(listas_espera, list):
        for lista_espera in listas_espera:
            if lista_espera["codLE"] == codLE:
                return delete_db(lista_espera, "codLE", USERS_DB_URI) #sucesso // database.py >delete_db->return == 1
    return 10  # Lista de espera não encontrada // database.py >delete_db->return == -1
    
