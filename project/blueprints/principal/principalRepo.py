import os
from typing import List
from project.db.database import read_db, write_db
#coment
USERS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"database","users.json")

def get_all_users()-> List[object]:
    return read_db(USERS_DB_URI)

def add_user(username: str, password: str, permission:int)->int:
    return write_db([{"username": username, "password": password, "permission":permission}],"username", USERS_DB_URI)
