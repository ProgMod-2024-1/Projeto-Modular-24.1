from project.db.database import read_db, write_db, update_db, delete_db
FORMACAO_DB_URI = "formacao"

def criaFormacao(dadosForm):
    return write_db(dadosForm,"codigo",FORMACAO_DB_URI)

def excluiFormacao(dadosForm):
    return delete_db(dadosForm,"codigo",FORMACAO_DB_URI)

def atualizaFormacao(dadosForm):
    return update_db(dadosForm,"codigo",FORMACAO_DB_URI)

def consultaFormacao(cod: str):
    formacoes = consultaTodasFormacoes()
    for i,formacao in enumerate(formacoes):
        print(formacao)
        if cod == formacao["codigo"]:
            return formacao
    return None

def consultaTodasFormacoes():
    return read_db(FORMACAO_DB_URI)