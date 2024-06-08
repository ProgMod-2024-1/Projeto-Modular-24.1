from .listaDeEsperaRepo import *

def cria_lista_espera_service(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
    if not lista_espera_existe_repo(codLE): #caso a lista de espera não exista, ele cria
        return cria_lista_espera_repo(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao) # sucesso // database.py >write_db->return == 1
    return -1  # Lista de espera ja existe // database.py >write_db->return == -1   

def consulta_lista_espera_service(codLE):
    if not lista_espera_existe_repo(codLE):
        return 10  # Lista inexistente // database.py >read_db->return == -1
    return consulta_lista_espera_repo(codLE) # sucesso // database.py >read_db->return == 1

def add_aluno_lista_espera_service(matrAluno, codLE): 
    #Optei por fazer verificacao condicional separada para tratar os retornos com mais clareza
    if not aluno_existe_repo(matrAluno):
        return 70  # Aluno inexistente // database.py >read_db->return == -1

    if not lista_espera_existe_repo(codLE):
        return 71  # Lista de espera inexistente // database.py >read_db->return == -1

    return add_aluno_lista_espera_repo(matrAluno, codLE) # Sucesso // database.py >update_dp->return == 1

def remove_aluno_lista_espera_service(matrAluno, codLE):
    if not aluno_existe_repo(matrAluno):
        return 100  # Aluno inexistente // database.py >read_db->return == -1

    if not lista_espera_existe_repo(codLE):
        return 101  # Lista de espera inexistente // database.py >read_db->return == -1

    return remove_aluno_lista_espera_repo(matrAluno, codLE) # sucesso // database.py >delete_db->return == 1

def exclui_lista_espera_service(codLE, cria_turma):
    if not lista_espera_existe_repo(codLE):
        return 10  # Lista inexistente // database.py >read_db->return == -1

    return exclui_lista_espera_repo(codLE, cria_turma) # sucesso // database.py >delete_db->return == 1
