from project.db import database
from os import path

dir_path = path.dirname(path.realpath(__file__)) + "/database/aluno.json"
base_dados = database.read_db(dir_path)