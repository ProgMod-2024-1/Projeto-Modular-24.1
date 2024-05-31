from .listaDeEsperaRepo import lista_espera_existe_repo, cria_lista_espera_repo , consulta_lista_espera_repo , aluno_existe_repo , add_aluno_lista_espera_repo , remove_aluno_lista_espera_repo , exclui_lista_espera_repo 


def cria_lista_espera_service(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
    if not lista_espera_existe_repo(codLE):
        return cria_lista_espera_repo(codLE, filial, curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao)
    return 1  # Lista de espera ja existe

def consulta_lista_espera_service(codLE):
    return consulta_lista_espera_repo(codLE)

def add_aluno_lista_espera_service(matrAluno, codLE):
    if aluno_existe_repo(matrAluno) and lista_espera_existe_repo(codLE):
        return add_aluno_lista_espera_repo(matrAluno, codLE)
    return 70 if not aluno_existe_repo(matrAluno) else 71

def remove_aluno_lista_espera_service(matrAluno, codLE):
    if aluno_existe_repo(matrAluno) and lista_espera_existe_repo(codLE):
        return remove_aluno_lista_espera_repo(matrAluno, codLE)
    return 100 if not aluno_existe_repo(matrAluno) else 101

def exclui_lista_espera_service(codLE, cria_turma):
    if lista_espera_existe_repo(codLE):
        return exclui_lista_espera_repo(codLE, cria_turma)
    return 10  # Lista inexistente
