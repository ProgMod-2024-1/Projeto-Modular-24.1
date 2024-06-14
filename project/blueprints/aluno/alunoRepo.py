import json
import os

from os import path

dir_path = path.dirname(path.realpath(__file__)) + "/database/aluno.json"
MAX_Alunos = 1000  # Limite máximo de alunos
Num_Matricula = "0001"



def salvar_aluno(aluno):
    try:
        if os.path.exists(dir_path):
            with open(dir_path, 'r+', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = []  # Inicializa como uma lista se não for uma lista válida
                except json.JSONDecodeError:
                    data = []  # Em caso de erro de decodificação

                data.append(aluno)

                file.seek(0)
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            with open(dir_path, 'w', encoding='utf-8') as file:
                json.dump([aluno], file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        with open(dir_path, 'w', encoding='utf-8') as file:
            json.dump([aluno], file, indent=4, ensure_ascii=False)




def criar_aluno(aluno) -> int:
    if len(dir_path) >= MAX_Alunos:
        return 0
   
    """
    tipos = [str, str, str, str, list, list, list, list, list]
    tiposAluno = [type(i) for i in aluno.values()]
    if tipos != tiposAluno:
        print("dados invalidos")
        return 2
    """
    
    aluno['matricula'] = gera_matricula()
    salvar_aluno(aluno)
    return 1
   
    
def gera_matricula()-> str:
    global Num_Matricula
    nova_matricula = Num_Matricula
    Num_Matricula = incrementar_matricula(Num_Matricula)
    return nova_matricula


def incrementar_matricula(num_matricula):
    
    numero = int(num_matricula)
    numero += 1
    nova_matricula = f"{numero:04d}"
    return nova_matricula
