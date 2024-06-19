import random
from alunoRepo import criaAluno, excluiAluno, consultaAluno, consultaTodosAlunos, atualizaAluno
from project.blueprints.formacao.formacaoService import *
def geraNovaMatricula():
    alunos = consultaTodosAlunos()
    tentativas = 0
    while tentativas < 1000:
        sufixo = 2410000
        matricula = sufixo + random.randint(0, 9999) 
        if not any(aluno['matricula'] == matricula for aluno in alunos):
            return matricula
        tentativas += 1

    print("Não foi possível gerar uma matrícula única em 1000 tentativas.")
    return None

def insereAluno(dadosAluno):
    retorno = criaAluno(dadosAluno)
    if retorno == 1:
        return {
            "codigo": 1,
            "mensagem": "Novo aluno inserido com sucesso"
        }
    elif retorno == -1:
        return {
            "codigo": 2,
            "mensagem": "Dados inválidos"
        }
    else:
        return {
            "codigo": 0,
            "mensagem": "Erro ao inserir novo aluno"
        }
    
def mudaAluno(dadosAluno):
    retorno = atualizaAluno(dadosAluno)
    if retorno == 1:
        return {
            "codigo": 6,
            "mensagem": "Aluno atualizado com sucesso"
        }
    elif retorno == -1:
        return {
            "codigo": 7,
            "mensagem": "Aluno não encontrado"
        }
    else:
        return {
            "codigo": 8,
            "mensagem": "Erro ao atualizar aluno"
        }
    
def deletaAluno(dadosAluno):
    retorno = excluiAluno(dadosAluno)
    if retorno == 1:
        return {
            "codigo": 9,
            "mensagem": "Aluno excluído com sucesso"
        }
    else:
        return {
            "codigo": 10,
            "mensagem": "Erro ao excluir aluno"
        }
    
def buscaAluno(dadosAluno):
    retorno = consultaAluno(dadosAluno)
    if retorno == None: 
        return {
            "codigo": 7,
            "mensagem": "Erro ao consultar aluno"
        }
    else:
        return {
            "codigo": 6,
            "mensagem": "Aluno buscado com sucesso",
            "dados": retorno
        }

def addCursosAluno(matrAluno: int, listaCursos): #espera uma lista de codigos de curso 
    dadosAluno = consultaAluno(matrAluno)
    if dadosAluno == None:
        return {
            "codigo": 7,
            "mensagem": "Erro ao consultar aluno"
        }
    else:
        cursosAluno = []
        for curso in listaCursos:
            cursosAluno.append({
                "curso":curso,
                "status": True,
                "nota": ""
                }
            ) 
        dadosAluno['cursos'] = cursosAluno
        return mudaAluno(dadosAluno)

def addAvalAluno(matrAluno:int, dadosAval):
    dadosAluno = consultaAluno(matrAluno)
    if dadosAluno == None:
        return {
            "codigo": 7,
            "mensagem": "Erro ao consultar aluno"
        }
    else:
        if "avaliacao" not in dadosAluno:
            dadosAluno["avaliacao"] = []
        dadosAluno["avaliacao"].append(dadosAval)
        return mudaAluno(dadosAluno)
    
