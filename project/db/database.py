import json
import os
from typing import List
from project.cache import cache


def read_db_json(pathToFile: str) -> List:
    if os.path.isfile(pathToFile) and os.access(pathToFile, os.R_OK):
        try:
            with open(pathToFile, mode = "r") as jsonFile:
                database = json.load(jsonFile)

            return database # Sucesso
        
        except Exception as ex:
            print(ex)
            return [] # Nao achou o banco
    else:
        return [] # Nao achou o banco

def read_db(memory_storage) -> List:
    try:
        return cache.get(memory_storage)["data"] # Sucesso
    
    except Exception as ex:
        print(ex)
        return [] # Nao achou o banco

def write_db(obj_list: List[object], primaryKey, memory_storage) -> int:
    data = cache.get(memory_storage)
    newData = data

    try:

        if len(data["data"]) > 0:
            first_obj_keys = set(data["data"][0].keys())
        else:
            first_obj_keys = None

        for obj in obj_list:
            new_obj_keys = set(obj.keys())

            if first_obj_keys != new_obj_keys and first_obj_keys != None:
                return -3  # Objeto a ser inserido tem chaves diferentes dos do banco
            
            if any(item[primaryKey] == obj[primaryKey] for item in newData["data"]):
                return -1 # Essa chave primaria ja existe

            newData["data"].append(obj)

        cache.set(memory_storage,newData)

        return 1 # Sucesso
    
    except Exception as ex:
        print(ex)
        cache.set(memory_storage,data)
        return -2 # Erro nao mapeado, nao salva nada
 
def update_db(obj: object, primaryKey: str, memory_storage) -> int:

    data = cache.get(memory_storage)

    if len(data["data"]) > 0:
        first_obj_keys = set(data["data"][0].keys())
        new_obj_keys = set(obj.keys())
        if first_obj_keys != new_obj_keys:
            return -3  # Objeto a ser inserido tem chaves diferentes dos do banco

    index = next((i for i, item in enumerate(data["data"]) if item[primaryKey] == obj[primaryKey]), None)

    if index is not None:
        data["data"][index] = obj
    else:
        return -1 # Nao achou o objeto

    cache.set(memory_storage,data)

    return 1 # Sucesso
    
def delete_db(object:object, primaryKey:str,  memory_storage) -> int:

    data = cache.get(memory_storage)
    
    index = next((i for i, item in enumerate(data["data"]) if item[primaryKey] == object[primaryKey]), None)
    
    if index is not None:
        del data["data"][index]
    else:
        return -1
    
    cache.set(memory_storage,data)
    
    return 1

def save_cache(memory_storage, pathToFile):
    if os.path.isfile(pathToFile) and os.access(pathToFile, os.R_OK):
        with open(pathToFile, mode="r") as jsonFile:
            data = json.load(jsonFile)
        try:
            with open(pathToFile, mode="w") as jsonFile:
                json.dump(cache.get(memory_storage), jsonFile)

            return 1 # Sucesso
        
        except Exception as ex:
            print(ex)
            with open(pathToFile, mode="w") as jsonFile:
                json.dump(data, jsonFile, indent=4)
            return -2 # Erro nao mapeado, nao salva nada
    else:
        return -4 # Nao achou db
        


