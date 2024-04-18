from project.db.database import read_db,write_db,update_db,delete_db
import os

USERS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"database","lista_de_espera.json")


def add_aluno(x,y,z):
    read_db()

