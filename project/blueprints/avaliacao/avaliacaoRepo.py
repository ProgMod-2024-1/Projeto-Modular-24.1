import os
import datetime
from typing import List
from project.db.database import read_db, write_db, update_db, delete_db

#Retorna todas as avalçiações presentes no json
def get_all_avaliacao()-> List[object]:
    return read_db("avaliacao")

#Registra uma nova avaliação
def registra_avaliacao(novaAval: object)->int:
    return write_db([novaAval], "info", "avaliacao")

#Retorna uma avaliação específica com os dados fornecidos
def seek_avaliacao(turma: str, codAval: str)-> object:
    data = read_db("avaliacao")

    for avaliacao in data:
        if(avaliacao["info"]["turma"]==turma and avaliacao["info"]["codAval"]==codAval):
            return avaliacao

    return None

#Atualiza os dados de uma avaliação existente
def muda_avaliacao(avalAtualizada: object)->int:
    return update_db(avalAtualizada, "info", "avaliacao")


#Deleta uma avaliação
def deleta_avaliacao(avaliacao: object)->int:
    return delete_db(avaliacao, "info", "avaliacao")