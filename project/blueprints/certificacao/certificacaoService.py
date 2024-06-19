from project.blueprints.certificacao.certificacaoRepo import cria_certificacao_vazia, get_all_certificacoes, registra_certificacao, seek_certificacao, muda_certificacao

# Retorna todas as certificações presentes no json
def get_certificacoes():
    return get_all_certificacoes()

# Registra uma nova certificação
def cria_certificacao(codAluno, codForm, dataConc):

    novaCert = {"formacao": codForm, "dataConc": dataConc}

    cert = seek_certificacoes(codAluno)

    if cert == None:
        novo_aluno = {"codAluno": codAluno, "certificados": [novaCert]}
        result = cria_certificacao_vazia(novo_aluno)
    else:
        cert["certificados"].append(novaCert)
        result = registra_certificacao(novaCert)

    if result == 1:
        return {
            "success": 1,
            "message": "Certificação criada com sucesso"
        }
    elif result == -1:
        return {
            "success": 0,
            "message": "Esta Certificação já existe."
        }
    else:
        return {
            "success": 0,
            "message": "Ocorreu um erro ao criar a Certificação. Tente novamente mais tarde"
        }

# Retorna uma certificação específica com os dados fornecidos
def seek_certificacoes(codAluno):
    return seek_certificacao(codAluno)

# Atualiza os dados de uma certificação existente
def muda_certificacoes(certAtualizada):
    result = muda_certificacao(certAtualizada)
    if result == 1:
        return {
            "success": 1,
            "message": "Certificação alterada com sucesso"
        }
    elif result == -1:
        return {
            "success": 0,
            "message": "Não achou o objeto."
        }
    elif result == -2:
        return {
            "success": 0,
            "message": "Erro não mapeado."
        }
    elif result == -3:
        return {
            "success": 0,
            "message": "Objeto a ser inserido tem chaves diferentes dos do banco."
        }
    else:
        return {
            "success": 0,
            "message": "Não achou db."
        }