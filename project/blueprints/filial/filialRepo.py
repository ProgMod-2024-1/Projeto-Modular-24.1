import os
import datetime
from typing import List
from project.db.database import read_db, write_db, update_db, delete_db


FILIAIS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"database","filial.json")

def get_all_filiais()-> List[object]:
    return read_db(FILIAIS_DB_URI)

def get_filial(filial_name:str)-> object:
    data = read_db(FILIAIS_DB_URI)
    for filial in data:
        if(filial["name"]==filial_name):
            return filial
        
    return None

def get_filial_by_codigo(filial_codigo:str)-> object:
    data = read_db(FILIAIS_DB_URI)
    for filial in data:
        if(filial["codigo"]==filial_codigo):
            return filial
        
    return None

def add_filial(codigo:str,nome: str, endereco: str, cep:str, min_alunos_p_turma: int)->int:
    ano_de_criacao = str(datetime.datetime.now().year)
    return write_db([{"codigo": codigo,"nome": nome, "endereco": endereco, "cep":cep, "min_alunos_p_turma":min_alunos_p_turma,"turmas":{ano_de_criacao:[]}}],"codigo", FILIAIS_DB_URI)

def update_filial_velho(filial_velha:object,filial_nova:object)-> int:
    result_update = update_db(filial_nova,"codigo", FILIAIS_DB_URI)
    result_delete = delete_db(filial_velha, "nome", FILIAIS_DB_URI)
    result_add = write_db(obj_list=[filial_nova],primaryKey="nome",pathToFile=FILIAIS_DB_URI)
    
    if(result_add==1 and result_delete==1):
        return 1
    
    elif(result_add==1):
        delete_db(filial_nova,"nome", FILIAIS_DB_URI)
        return -2
    
    elif(result_delete==1):
        write_db(obj_list=[filial_velha],primaryKey="nome",pathToFile=FILIAIS_DB_URI)
        return -1
    
    else:
        return -3
    
def update_filial(filial_nova:object)-> int:
    return update_db(filial_nova,"codigo", FILIAIS_DB_URI)
    

def delete_filial(codigo:str)-> int:
    return delete_db({"codigo":codigo}, "codigo", FILIAIS_DB_URI)