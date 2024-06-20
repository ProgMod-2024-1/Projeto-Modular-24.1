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

    with open(TEST_DB_URI, mode="w") as jsonFile:
        json.dump(test_data, jsonFile)

    data_from_db = {"data":read_db(TEST_DB_URI)}

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

    test_data_assertion = {"data":[
        { 
            "id": 1,
            "nome": "Joao"
        },
        {
            "id": 2,
            "nome": "Antonio"
        },
        {
            "id": 3,
            "nome": "Maria"
        }
    ]}

    with open(TEST_DB_URI, mode="w") as jsonFile:
        json.dump(test_data, jsonFile)

    assert(write_db([{"id": 2, "nome": "Joao"}],"id",TEST_DB_URI) == -1)
    assert(write_db([{"id": 4, "nome": "Joao", "telefone":234343343}],"id", TEST_DB_URI) == -3)
    assert(write_db([{"id": 3, "nome": "Maria"}], "id", TEST_DB_URI) == 1)
    assert(write_db([{"id": 3, "nome": "Maria"}], "id", TEST_URI_INEXITENTE) == -4)
    
    with open(TEST_DB_URI, mode="r") as jsonFile:
        data_from_db = json.load(jsonFile)
        assert(data_from_db == test_data_assertion)

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

    test_data_assertion = {"data":[
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

    with open(TEST_DB_URI, mode="w") as jsonFile:
        json.dump(test_data, jsonFile)

    assert(update_db({"id": 5, "nome": "Joao", "telefone":11},"id",TEST_DB_URI) == -1)
    assert(update_db({"id": 5, "nome": "Joao", "telefone":11, "endereco": "Gavea"},"id",TEST_DB_URI) == -3)
    assert(update_db([{"id": 3, "nome": "Maria"}], "id", TEST_URI_INEXITENTE) == -4)
    assert(update_db({"id": 1, "nome": "Joao", "telefone":11},"id",TEST_DB_URI) == 1)
    
    with open(TEST_DB_URI, mode="r") as jsonFile:
        data_from_db = json.load(jsonFile)
        assert(data_from_db == test_data_assertion)

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

    test_data_assertion = {"data":[
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
    ]}

    with open(TEST_DB_URI, mode="w") as jsonFile:
        json.dump(test_data, jsonFile)

    assert(delete_db({"id": 5, "nome": "Joao", "telefone":11},"id",TEST_DB_URI) == -1)
    
    assert(delete_db({"id": 3},"id",TEST_DB_URI) == 1)
    
    with open(TEST_DB_URI, mode="r") as jsonFile:
        data_from_db = json.load(jsonFile)
        assert(data_from_db == test_data_assertion)