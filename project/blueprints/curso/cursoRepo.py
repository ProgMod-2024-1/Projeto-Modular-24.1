import os
from typing import List
from project.db.database import read_db, write_db

CURSOS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "cursos.json")

def get_all_cursos() -> List[object]:
    return read_db(CURSOS_DB_URI)

def add_curso(curso: dict) -> int:
    return write_db([curso], "id", CURSOS_DB_URI)

def get_curso(codCurs: str) -> object:
    data = read_db(CURSOS_DB_URI)
    for curso in data:
        if curso["id"] == codCurs:
            return curso
    return None

def update_curso(updated_curso: dict) -> bool:
    data = read_db(CURSOS_DB_URI)
    for idx, curso in enumerate(data):
        if curso["id"] == updated_curso["id"]:
            data[idx] = updated_curso
            write_db(data, "id", CURSOS_DB_URI, overwrite=True)
            return True
    return False

