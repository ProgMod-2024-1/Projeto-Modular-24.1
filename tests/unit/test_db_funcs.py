from project.db.database import write_db, delete_db, update_db, read_db
import json,os
from project.cache import cache

TEST_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"db","test_db.json")
TEST_URI_INEXITENTE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"db","falso.json")

def test_db_read():
    test_data = {"data":[
        { 
            "id": 1,
            "nome": "Joao"
        },
        {
            "id": 2,
            "nome": "Antonio"
        }
    ]}
    cache.set("test")
    cache.add("test", test_data)

    data_from_db = {"data":read_db("test")}

    assert(data_from_db == test_data)

def test_db_write():
    test_data = {"data":[
        { 
            "id": 1,
            "nome": "Joao"
        },
        {
            "id": 2,
            "nome": "Antonio"
        }
    ]}

    cache.set("test")
    cache.add("test", test_data)

    assert(write_db([{"id": 2, "nome": "Joao"}],"id","test") == -1)
    assert(write_db([{"id": 4, "nome": "Joao", "telefone":234343343}],"id", "test") == -3)
    assert(write_db([{"id": 3, "nome": "Maria"}], "id", "test") == 1)

def test_db_update():
    test_data = {"data":[
        { 
            "id": 1,
            "nome": "Joao",
            "telefone": 2
        },
        {
            "id": 2,
            "nome": "Antonio",
            "telefone": 22
        },
        {
            "id": 3,
            "nome": "Maria",
            "telefone": 33
        }
    ]}

    cache.set("test")
    cache.add("test", test_data)

    assert(update_db({"id": 5, "nome": "Joao", "telefone":11},"id","test") == -1)
    assert(update_db({"id": 5, "nome": "Joao", "telefone":11, "endereco": "Gavea"},"id","test") == -3)
    assert(update_db({"id": 1, "nome": "Joao", "telefone":11},"id","test") == 1)
    

def test_db_delete():
    test_data = {"data":[
        { 
            "id": 1,
            "nome": "Joao",
            "telefone": 11
        },
        {
            "id": 2,
            "nome": "Antonio",
            "telefone": 22
        },
        {
            "id": 3,
            "nome": "Maria",
            "telefone": 33
        }
    ]}

    cache.set("test")
    cache.add("test", test_data)

    assert(delete_db({"id": 5, "nome": "Joao", "telefone":11},"id","test") == -1)
    assert(delete_db({"id": 3},"id","test") == 1)
