from project.blueprints.formacao.formacaoService import *
from project.blueprints.aluno.alunoRepo import criaAluno, excluiAluno, consultaAluno, consultaTodosAlunos, atualizaAluno
from project.blueprints.formacao.formacaoService import *
from project.blueprints.curso.cursoRepo import *
from datetime import datetime
import random


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

def addCursosAluno(matrAluno: int, curso): #espera uma lista de codigos de curso 
    dadosAluno = consultaAluno(matrAluno)
    if dadosAluno == None:
        return {
            "codigo": 7,
            "mensagem": "Erro ao consultar aluno"
        }
    else:
        if "cursos" not in dadosAluno:
            cursosAluno = []
        else:
            cursosAluno = dadosAluno["cursos"]
        
        cursosAluno.append({"curso":curso,"status": True,"nota": ""}) 
        print(cursosAluno)
        dadosAluno['cursos'] = cursosAluno
        print(dadosAluno)
        return mudaAluno(dadosAluno)

def buscaNotaCursoAluno(matrAluno: int, codCurso):
    dadosAluno = consultaAluno(matrAluno)
    if dadosAluno == None:
        return -1
    else:
        if "cursos" not in dadosAluno:
            return -1
        else:
            cursos = dadosAluno["cursos"]
            for curso in cursos:
                if codCurso == curso["codigo"]:
                    return curso["nota"]
            return -1

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

def defAprovadoCurso(matrAluno: int, codCurso: str):
    dadosAluno = consultaAluno(matrAluno)
    if dadosAluno == None:
        return {
            "codigo": 71,
            "mensagem": "Erro ao consultar aluno"
        }
    else:
        dadosCurso = get_curso(codCurso)
        if dadosCurso == None:
            return {
            "codigo": 72,
            "mensagem": "Erro ao consultar curso"
        }
        else:
            todasAvaliacoes = dadosAluno["avaliacao"]
            avaliacoesCurso = []
            for aval in todasAvaliacoes:
                if aval["curso"] == codCurso:
                    avaliacoesCurso.append(aval)
            media = 0
            for av in avaliacoesCurso:
                media += int(av["nota"])
            media = media / len(avaliacoesCurso)
            criterio = dadosCurso["criterios_aprovacao"]
            if media < criterio:
                return {
                    "codigo": 61,
                    "mensagem": "Aluno Não Aprovado no Curso"
                }
            else:
                return {
                    "codigo": 62,
                    "mensagem": "Aluno Aprovado no Curso"
                }

def defAprovadoForm(matrAluno: int, codForm: str):
    if not validaCodForm(codForm):
        return {
            "codigo":72,
            "mensagem":"Código de formação inválida"
        }
    dadosAluno = consultaAluno(matrAluno)
    if dadosAluno == None:
        return {
            "codigo": 71,
            "mensagem": "Erro ao consultar aluno"
        }
    else:
        dadosForm = consultaFormacao(codForm)
        gradeForm = dadosForm["grade"]
        for curso in gradeForm:
            dadosCurso = get_curso(curso)
            criterio = dadosCurso["criterios_aprovacao"]
            todasAvaliacoes = dadosAluno["avaliacao"]
            avaliacoesCurso = []
            for aval in todasAvaliacoes:
                if aval["curso"] == dadosCurso[""]:
                    avaliacoesCurso.append(aval)
            media = 0
            for av in avaliacoesCurso:
                media += int(av["nota"])
            media = media / len(avaliacoesCurso)
            if media < criterio:
                return {
                    "codigo": 61,
                    "mensagem": "Aluno Não Aprovado"
                }

        #cria_certificacao(matrAluno, dadosAluno["user"], codForm, datetime.now().strftime("%d-%m-%Y"))
        return {
            "codigo": 62,
            "mensagem": "Aluno Aprovado"
        }
