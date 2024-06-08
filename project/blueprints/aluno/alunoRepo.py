import aluno 

aluno_atualizado = {
    "matricula": "123",
    "nome": "joao",
    "endereco": "rua",
    "status": 1,
    "preferencia_filiais": [],
    "cursos_e_formacoes_feitas":[],
    "cursos_avulsos": [],
    "formacoes_atuais": [],
    "listas_espera": []
}

def atualizaAluno(dadosAluno: object, matrAluno: str) -> int:
    # checa se os dados são válidos
    tipos = [str, str, str, int, list, list, list, list, list]
    tiposAluno = [type(i) for i in dadosAluno.values()]
    if tipos != tiposAluno:
        return 8

    # checa se a matrícula existe
    index = None
    for i in range(len(aluno.base_dados)):
        if aluno.base_dados[i].get("matricula") == matrAluno:
            index = i
            break
    if index == None:
        return 7

    print(aluno.database.update_db(dadosAluno, "matricula", aluno.dir_path))

    return index

print(atualizaAluno(aluno_atualizado, "123"))