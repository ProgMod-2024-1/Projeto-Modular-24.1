from project.blueprints.formacao.formacaoRepo import criaFormacao, atualizaFormacao, consultaFormacao, consultaTodasFormacoes, excluiFormacao

#Codigo deve ser uma string de tamanho 6 contendo apenas letras maiusculas
def validaCodForm(cod: str):
    if len(cod) != 6:
        return False
    if not cod.isupper():
        return False
    if not cod.isalpha():
        return False
    return True

def insereFormacao(dadosForm):
    retorno = criaFormacao(dadosForm)
    if retorno == 1:
        return {
            "codigo": 1,
            "mensagem": "Nova formação inserida com sucesso"
        }
    elif retorno == -1:
        return {
            "codigo": 2,
            "mensagem": "Dados inválidos"
        }
    else:
        #print(retorno)
        return {
            "codigo": 0,
            "mensagem": "Erro ao inserir nova formação"
        }
    
def mudaFormacao(dadosForm):
    retorno = atualizaFormacao(dadosForm)
    if retorno == 1:
        return {
            "codigo": 6,
            "mensagem": "Formação atualizada com sucesso"
        }
    elif retorno == -1:
        return {
            "codigo": 7,
            "mensagem": "Formação não encontrada"
        }
    else:
        return {
            "codigo": 8,
            "mensagem": "Erro ao atualizar formação"
        }
    
def deletaFormacao(dadosForm):
    retorno = excluiFormacao(dadosForm)
    if retorno == 1:
        return {
            "codigo": 9,
            "mensagem": "Formação excluída com sucesso"
        }
    else:
        return {
            "codigo": 10,
            "mensagem": "Erro ao excluir formação"
        }
    
def buscaFormacao(codForm: str):
    if not validaCodForm(codForm):
        return {
            "codigo": 7,
            "mensagem": "Erro ao consultar formação"
        }
    
    retorno = consultaFormacao(codForm)
    if retorno == None: 
        return {
            "codigo": 7,
            "mensagem": "Erro ao consultar formação"
        }
    else:
        return {
            "codigo": 6,
            "mensagem": "Formação buscada com sucesso",
            "dados": retorno
        }