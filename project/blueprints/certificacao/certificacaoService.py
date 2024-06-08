from project.blueprints.certificacao.certificacaoRepo import get_all_certificacoes, registra_certificacao, seek_certificacao, muda_certificacao

#Retorna todas as certificacoes presentes no json
def get_certificacoes():
    return get_all_certificacoes()


#Registra uma nova certificacao
def registra_certificacoes(codCert, id_aluno, id_formacao, data_conclusao):
    result = registra_certificacao(codCert=codCert, id_aluno=id_aluno, id_formacao=id_formacao, data_conclusao=data_conclusao)
    if result == 1:
        return {
                "success": 1,
                "message": "Certificação criada com sucesso",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta Certificação já existe.",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao criar a Certificação.",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }


#Retorna uma certificacao específica com os dados fornecidos   
def seek_certificacoes(codCert, id_aluno, id_formacao):
    return seek_certificacao(codCert, id_aluno, id_formacao)


#Atualiza os dados de uma certificacao existente   
def muda_certificacoes(codCert, id_aluno, id_formacao, data_conclusao):
    result = muda_certificacao(codCert=codCert, id_aluno=id_aluno, id_formacao=id_formacao, data_conclusao=data_conclusao)
    if result == 1:
        return {
                "success": 1,
                "message": "Certificação alterada com sucesso",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Nao achou o objeto.",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }
    elif result == -2:
        return {
                "success": 0,
                "message": "Erro nao mapeado.",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }
    elif result == -3:
        return {
                "success": 0,
                "message": "Objeto a ser inserido tem chaves diferentes dos do banco.",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }
    else:
        return {
                "success": 0,
                "message": "Nao achou db.",
                "user":{"id_aluno":id_aluno,"id_formacao":id_formacao}
                }