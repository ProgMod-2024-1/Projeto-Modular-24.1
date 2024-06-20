from project.db.database import write_db, delete_db, update_db, read_db
import json,os

TEST_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"db","test_db.json")
TEST_URI_INEXITENTE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"db","falso.json")

def test_delete_filial():
    pass

def test_update_filial():
    pass

def test_add_filial():
    pass