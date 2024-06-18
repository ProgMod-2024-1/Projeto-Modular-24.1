from project.blueprints.filial.filialRepo import add_filial, delete_filial, update_filial, get_all_filiais, update_filial
import random
import string

def get_filiais():
    return get_all_filiais()

def add_filiais(nome,endereco,cep,nAlunos):

    filiais_existentes = (get_all_filiais())
    codigos_existentes = [filial["codigo"] for filial in filiais_existentes]

    while True:
        novo_codigo = ''.join(random.choices(string.digits, k=8))
        if novo_codigo not in codigos_existentes:
            break


    result = add_filial(codigo=novo_codigo,nome=nome, endereco=endereco,cep=cep, min_alunos_p_turma=int(nAlunos))
    if result == 1:
        return {
                "success": 1,
                "message": "Filial criada com sucesso",
                "data":{"nome":endereco,"endereco":endereco}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta filial ja existe. Tente novamente com outro nome",
                "data":{"nome":endereco,"endereco":endereco}
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao criar a filial. Tente novamente mais tarde",
                "data":{"nome":endereco,"endereco":endereco}
                }
    
def update_filias(data):
    
    filial_nova = {"codigo":data["codigoFilialEditada"],"nome": data["nomeFilialEditada"], "endereco": data["enderecoFilialEditada"], "cep": data["cepFilialEditada"], "min_alunos_p_turma": int(data["numeroDeAlunosFilialEditada"]), "turmas": {"2024": []}}
    filial_velha = {"nome": data["nomeFilialVelha"], "endereco": data["enderecoFilialVelha"], "cep": data["cepFilialVelha"], "min_alunos_p_turma": int(data["numeroDeAlunosFilialVelha"]), "turmas": {"2024": []}}
    result = update_filial(filial_nova)
    
    if result == 1:
        return {
                "success": 1,
                "message": "Filial editada com sucesso",
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao editar a filial. Tente novamente mais tarde",
                }

def delete_filiais(codigo: string):
    result = delete_filial(codigo)
    
    if result == 1:
        return {
                "success": 1,
                "message": "Filial removida com sucesso",
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao deletar a filial. Tente novamente mais tarde",
                }