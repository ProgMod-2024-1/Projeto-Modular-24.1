from project.blueprints.principal.principalService import *

def test_register_user():
    ##Registrando usuario
    result = register_user("test123", "abc")
    assert(result["success"], 1)

    ##Registrando usuario repetido
    result = register_user("test123", "abc")
    assert(result["success"], 0)

def test_login_user():
    pass

def test_logout_user():
    pass