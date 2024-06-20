from project.blueprints.avaliacao.avaliacaoRepo import get_all_avaliacao, registra_avaliacao, seek_avaliacao, muda_avaliacao, deleta_avaliacao
#from project.blueprints.curso.cursoRepo import consultar_curso

#Retorna todas as avalçiações presentes no json
def get_all_avaliacoes():
    return get_all_avaliacao()


def get_avaliacoes(user):
    avaliacoes = get_all_avaliacao()
    avaliacoes_professor = []

    for avaliacao in avaliacoes:
        if avaliacao["corretor"] == user.id:
            avaliacoes_professor.append(avaliacao)

    return avaliacoes_professor
            


#Registra uma nova avaliação
def registra_avaliacoes(novaAval):

    """ consulta = consultar_curso(novaAval["curso"])
    if type(consulta) == str:
        return {"success": 0,
                "message": "Dados inseridos são inválidos"} """
    
    #consulta se aluno existe

    #consulta se turma existe

    result = registra_avaliacao(novaAval)
    if result == 1:
        return {
                "success": 1,
                "message": "Avaliação criada com sucesso"
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta avaliação ja existe."
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao criar a avaliação. Tente novamente mais tarde"
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
                "message": "Alterações realizadas com sucesso"
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Nao achou o objeto."
                }
    elif result == -2:
        return {
                "success": 0,
                "message": "Erro nao mapeado."
                }
    elif result == -3:
        return {
                "success": 0,
                "message": "Objeto a ser inserido tem chaves diferentes dos do banco."
                }
    else:
        return {
                "success": 0,
                "message": "Nao achou db."
                }
    
#Deleta uma avaliação
def deleta_avaliacoes(avaliacao):
    result = deleta_avaliacao(avaliacao)
    if result == 1:
        return {
                "success": 1,
                "message": "Avaliação deletada com sucesso"
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao deletar a avaliação. Tente novamente mais tarde"
                }
    

#Lança uma avaliação
def lanca_avaliacoes(turma, codAval, user):

    aval = seek_avaliacao(turma, codAval)

    if aval["corretor"] != user.id or aval["lancada"]:
        return {
                "success": 1,
                "message": "Ocorreu um erro ao lançar a avaliação. Tente novamente mais tarde"
                }

    for correcao in aval["correcoes"]:
        #!chamada da função addAvalAluno
        pass

    aval["lancada"] = True
    muda_avaliacao(aval)

    result = 1

    if result == 1:
        return {
                "success": 1,
                "message": "Avaliação lançada com sucesso"
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao lançar a avaliação. Tente novamente mais tarde"
                }