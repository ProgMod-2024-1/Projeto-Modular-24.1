import os
from typing import List
from project.db.database import read_db, write_db
from flask import session

def get_all_users()-> List[object]:
    return read_db("users")

def create_user(username: str, password: str, permission:int)->int:
    return write_db([{"username": username, "password": password, "permission":permission}],"username", "users")

def get_user(username:str)-> object:
    data = read_db("users")
    for user in data:
        if(user["username"]==username):
            return user
        
    return None