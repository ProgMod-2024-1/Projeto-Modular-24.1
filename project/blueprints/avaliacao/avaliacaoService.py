from project.blueprints.avaliacao.avaliacaoRepo import get_all_avaliacoes, registra_avaliacao, seek_avaliacao, muda_avaliacao, deleta_avaliacao
from project.blueprints.curso.cursoRepo import consultar_curso

#Retorna todas as avalçiações presentes no json
def get_avaliacoes():
    return get_all_avaliacoes()


#Registra uma nova avaliação
def registra_avaliacoes(novaAval):

    consulta = consultar_curso(novaAval["curso"])
    if type(consulta) == str:
        return {"success": 0,
                "message": "Dados inseridos são inválidos"}

    result = registra_avaliacao(novaAval)
    if result == 1:
        return {
                "success": 1,
                "message": "Avaliação criada com sucesso",
                "user":{}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta avaliação ja existe.",
                "user":{}
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao criar a avaliação. Tente novamente mais tarde",
                "user":{}
                }


#Retorna uma avaliação específica com os dados fornecidos   
def seek_avaliacoes(turma, codAval):
    return seek_avaliacao(turma, codAval)


#Atualiza os dados de uma avaliação existente   
def muda_avaliacoes(avalAtualizada):
    result = muda_avaliacao(avalAtualizada)
    if result == 1:
        return {
                "success": 1,
                "message": "Alterações realizadas com sucesso",
                "user":{}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Nao achou o objeto.",
                "user":{}
                }
    elif result == -2:
        return {
                "success": 0,
                "message": "Erro nao mapeado.",
                "user":{}
                }
    elif result == -3:
        return {
                "success": 0,
                "message": "Objeto a ser inserido tem chaves diferentes dos do banco.",
                "user":{}
                }
    else:
        return {
                "success": 0,
                "message": "Nao achou db.",
                "user":{}
                }
    
#Deleta uma avaliação
def deleta_avaliacoes(avaliacao):
    result = deleta_avaliacao(avaliacao)
    if result == 1:
        return {
                "success": 1,
                "message": "Avaliação deletada com sucesso",
                "user":{}
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao deletar a avaliação. Tente novamente mais tarde",
                "user":{}
                }
    

#Lança uma avaliação
def lanca_avaliacoes(turma, codAval):

    aval = seek_avaliacao(turma, codAval)

    for correcao in aval["correcoes"]:
        #!chamada da função addAvalAluno
        pass

    result = 1

    if result == 1:
        return {
                "success": 1,
                "message": "Avaliação lançada com sucesso",
                "user":{}
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao lançar a avaliação. Tente novamente mais tarde",
                "user":{}
                }