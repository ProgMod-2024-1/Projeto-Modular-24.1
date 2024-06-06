import os
import datetime
from typing import List
from project.db.database import read_db, write_db, update_db, delete_db


AVALIACOES_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"database","avaliacao.json")

#Retorna todas as avalçiações presentes no json
def get_all_avaliacoes()-> List[object]:
    return read_db(AVALIACOES_DB_URI)

#Registra uma nova avaliação
def registra_avaliacao(turma: str, codAval: str, curso:str, perguntas: object)->int:

    return write_db([{"perguntas":perguntas, "instancias":[], "info": {"turma": turma, "codAval": codAval, "curso": curso, "corretor":""}}], "info", AVALIACOES_DB_URI)

#Retorna uma avaliação específica com os dados fornecidos
def seek_avaliacao(turma: str, codAval: str, curso:str)-> object:
    data = read_db(AVALIACOES_DB_URI)

    for avaliacao in data:
        if(avaliacao["info"]["turma"]==turma and avaliacao["info"]["codAval"]==codAval and avaliacao["info"]["curso"]==curso):
            return avaliacao

    return None

#Atualiza os dados de uma avaliação existente
def muda_avaliacao(turma: str, codAval: str, curso:str, perguntas: object, instancias: object, corretor: str)->int:

    return update_db({"perguntas":perguntas, "instancias":instancias, "info": {"turma": turma, "codAval": codAval, "curso": curso, "corretor":corretor}}, "info", AVALIACOES_DB_URI)