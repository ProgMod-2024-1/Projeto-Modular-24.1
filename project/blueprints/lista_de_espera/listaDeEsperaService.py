from .listaDeEsperaRepo import *

# from ..nomeFili.nomeFiliRepo import nomeFili_existe_repo
# from ..professor.professorRepo import professor_existe_repo
# from ..codCurso.codCursoRepo import codCurso_existe_repo

def cria_lista_espera_service(codLE, nomeFili, codCurso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
    if not lista_espera_existe_repo(codLE):  # caso a lista de espera não exista, ele cria
        # if not nomeFili_existe_repo(nomeFili):
        #     return 102  # Filial inexistente
        # if not codCurso_existe_repo(codCurso):
        #     return 103  # Curso inexistente
        # if not professor_existe_repo(matrProf):
        #     return 104  # Professor inexistente
        return cria_lista_espera_repo(codLE, nomeFili, codCurso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao)  # sucesso
    return -1  # Lista de espera já existe


def consulta_lista_espera_service(codLE):
    lista_espera = consulta_lista_espera_repo(codLE)
    return lista_espera

def add_aluno_lista_espera_service(matrAluno, codLE): 
    result = add_aluno_lista_espera_repo(matrAluno, codLE)
    if result == 1:
        return 9
    else:
        return result 

def remove_aluno_lista_espera_service(matrAluno, codLE):
    if not aluno_existe_repo(matrAluno):
        return 100  # Aluno inexistente

    if not lista_espera_existe_repo(codLE):
        return 101  # Lista de espera inexistente

    result = remove_aluno_lista_espera_repo(matrAluno, codLE)
    if result == 1:
        return 9  # Sucesso
    else:
        return result  # Retorna o codigo de erro diretamente

def exclui_lista_espera_service(codLE, cria_turma):
    if not lista_espera_existe_repo(codLE):
        return 101  # Lista de espera inexistente

    result = exclui_lista_espera_repo(codLE)
    
    if result == 1:
        return 9  # Sucesso
    else:
        return result  # Retorna o código de erro diretamente

