from project.blueprints.avaliacao.avaliacaoRepo import get_all_avaliacoes, registra_avaliacao, seek_avaliacao, muda_avaliacao

#Retorna todas as avalçiações presentes no json
def get_avaliacoes():
    return get_all_avaliacoes()


#Registra uma nova avaliação
def registra_avaliacoes(turma,codAval,curso,perguntas):
    result = registra_avaliacao(turma=turma, codAval=codAval,curso=curso, perguntas=perguntas)
    if result == 1:
        return {
                "success": 1,
                "message": "Avaliação criada com sucesso",
                "user":{"curso":curso,"turma":turma}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta avaliação ja existe.",
                "user":{"curso":curso,"turma":turma}
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao criar a avaliação. Tente novamente mais tarde",
                "user":{"curso":curso,"turma":turma}
                }


#Retorna uma avaliação específica com os dados fornecidos   
def seek_avaliacoes(turma, codAval, curso):
    return seek_avaliacao(turma, codAval, curso)


#Atualiza os dados de uma avaliação existente   
def muda_avaliacoes(turma,codAval,curso,perguntas, instancias, corretor):
    result = muda_avaliacao(turma=turma, codAval=codAval,curso=curso, perguntas=perguntas, instancias=instancias, corretor=corretor)
    if result == 1:
        return {
                "success": 1,
                "message": "Questões alteradas com sucesso",
                "user":{"curso":curso,"turma":turma}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Nao achou o objeto.",
                "user":{"curso":curso,"turma":turma}
                }
    elif result == -2:
        return {
                "success": 0,
                "message": "Erro nao mapeado.",
                "user":{"curso":curso,"turma":turma}
                }
    elif result == -3:
        return {
                "success": 0,
                "message": "Objeto a ser inserido tem chaves diferentes dos do banco.",
                "user":{"curso":curso,"turma":turma}
                }
    else:
        return {
                "success": 0,
                "message": "Nao achou db.",
                "user":{"curso":curso,"turma":turma}
                }