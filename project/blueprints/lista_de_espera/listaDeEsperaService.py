from .listaDeEsperaRepo import *
from ..turma.turmaService import criaTurma

#from ..filial.filialService import filial_existe_repo
#from ..professor.professorService import professor_existe_repo
#from ..curso.cursoService import curso_existe_repo
#from ..aluno.alunoService import aluno_existe_repo

def cria_lista_espera_service(codLE, filial, cod_curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao):
    if not lista_espera_existe_repo(codLE):  # caso a lista de espera n�o exista, ele cria
        # if not filial_existe_repo(filial):
        #     return 102  # Filial inexistente
        # if not curso_existe_repo(curso):
        #     return 103  # Curso inexistente
        # if not professor_existe_repo(matrProf):
        #     return 104  # Professor inexistente
        return cria_lista_espera_repo(codLE, filial, cod_curso, horario, matrProf, numMinimo, tempo_desde_ultima_adicao)  # sucesso
    return -1  # Lista de espera j� existe
    
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

    # Consulta a lista de espera antes de exclu�-la
    lista_espera = consulta_lista_espera_repo(codLE)
    if not lista_espera:
        return 101  # Lista de espera inexistente
    
    result = exclui_lista_espera_repo(codLE)
    
    if result == 1 and cria_turma:
        # Contar o n�mero de alunos na lista de espera
        num_alunos = len(lista_espera["alunos"])
        num_minimo = int(lista_espera["numMinimo"])

        # Determinar se a turma ser� online ou presencial
        if num_alunos >= num_minimo:
            online_status = 'off'  # Turma presencial
        else:
            online_status = 'on'  # Turma online

        # Criar turma com base nos dados da lista de espera
        dados_turma = {
            "curso": lista_espera["cod_curso"],
            "matrProf": lista_espera["matrProf"],
            "horario": lista_espera["horario"],
            "online": online_status,
            "filial": lista_espera["filial"],
            "alunos": lista_espera["alunos"]
        }

        criaTurma(dados_turma)
        return 9  # Sucesso
    elif result == 1:
        return 9  # Sucesso ao excluir a lista de espera
    else:
        return result  # Retorna o c�digo de erro diretamente