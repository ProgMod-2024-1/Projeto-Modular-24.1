from project.blueprints.certificacao.certificacaoRepo import get_all_certificacoes, registra_certificacao, seek_certificacao, muda_certificacao

# Retorna todas as certificações presentes no json
def get_certificacoes():
    return get_all_certificacoes()

# Registra uma nova certificação
def registra_certificacoes(novaCert):
    result = registra_certificacao(novaCert)
    if result == 1:
        return {
            "success": 1,
            "message": "Certificação criada com sucesso",
            "user": {
                "id_aluno": novaCert["info"]["id_aluno"],
                "id_formacao": novaCert["info"]["id_formacao"]
            }
        }
    elif result == -1:
        return {
            "success": 0,
            "message": "Esta Certificação já existe.",
            "user": {
                "id_aluno": novaCert["info"]["id_aluno"],
                "id_formacao": novaCert["info"]["id_formacao"]
            }
        }
    else:
        return {
            "success": 0,
            "message": "Ocorreu um erro ao criar a Certificação. Tente novamente mais tarde",
            "user": {
                "id_aluno": novaCert["info"]["id_aluno"],
                "id_formacao": novaCert["info"]["id_formacao"]
            }
        }

# Retorna uma certificação específica com os dados fornecidos
def seek_certificacoes(codCert, id_aluno, id_formacao):
    return seek_certificacao(codCert, id_aluno, id_formacao)

# Atualiza os dados de uma certificação existente
def muda_certificacoes(certAtualizada):
    result = muda_certificacao(certAtualizada)
    if result == 1:
        return {
            "success": 1,
            "message": "Certificação alterada com sucesso",
            "user": {
                "id_aluno": certAtualizada["info"]["id_aluno"],
                "id_formacao": certAtualizada["info"]["id_formacao"]
            }
        }
    elif result == -1:
        return {
            "success": 0,
            "message": "Não achou o objeto.",
            "user": {
                "id_aluno": certAtualizada["info"]["id_aluno"],
                "id_formacao": certAtualizada["info"]["id_formacao"]
            }
        }
    elif result == -2:
        return {
            "success": 0,
            "message": "Erro não mapeado.",
            "user": {
                "id_aluno": certAtualizada["info"]["id_aluno"],
                "id_formacao": certAtualizada["info"]["id_formacao"]
            }
        }
    elif result == -3:
        return {
            "success": 0,
            "message": "Objeto a ser inserido tem chaves diferentes dos do banco.",
            "user": {
                "id_aluno": certAtualizada["info"]["id_aluno"],
                "id_formacao": certAtualizada["info"]["id_formacao"]
            }
        }
    else:
        return {
            "success": 0,
            "message": "Não achou db.",
            "user": {
                "id_aluno": certAtualizada["info"]["id_aluno"],
                "id_formacao": certAtualizada["info"]["id_formacao"]
            }
        }