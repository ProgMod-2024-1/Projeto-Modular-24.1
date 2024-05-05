from project.blueprints.filial.filialRepo import add_filial, delete_filial, update_filial, get_all_filiais, update_filial


def get_filiais():
    return get_all_filiais()

def add_filiais(nome,endereco,cep,nAlunos):
    result = add_filial(nome=nome, endereco=endereco,cep=cep, min_alunos_p_turma=int(nAlunos))
    if result == 1:
        return {
                "success": 1,
                "message": "Filial criada com sucesso",
                "user":{"nome":endereco,"endereco":endereco}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta filial ja existe. Tente novamente com outro nome",
                "user":{"nome":endereco,"endereco":endereco}
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao criar a filial. Tente novamente mais tarde",
                "user":{"nome":endereco,"endereco":endereco}
                }
    
def update_filias(data):
    
    filial_nova = {"nome": data["nomeFilialEditada"], "endereco": data["enderecoFilialEditada"], "cep": data["cepFilialEditada"], "min_alunos_p_turma": int(data["numeroDeAlunosFilialEditada"]), "turmas": {"2024": []}}
    filial_velha = {"nome": data["nomeFilialVelha"], "endereco": data["enderecoFilialVelha"], "cep": data["cepFilialVelha"], "min_alunos_p_turma": int(data["numeroDeAlunosFilialVelha"]), "turmas": {"2024": []}}
    result = update_filial(filial_velha, filial_nova)
    
    if result == 1:
        return {
                "success": 1,
                "message": "Filial editada com sucesso",
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta filial ja existe. Tente novamente com outro nome",
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao editar a filial. Tente novamente mais tarde",
                }

def delete_filiais(filial_velha: object, filial_nova:object):
    result = delete_filial(filial_velha, filial_nova)
    
    if result == 1:
        return {
                "success": 1,
                "message": "Filial removida com sucesso",
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Esta filial ja existe. Tente novamente com outro nome",
                }
    else:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao editar a filial. Tente novamente mais tarde",
                }