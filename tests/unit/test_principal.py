from project.blueprints.principal.principalService import *

def test_register_user():
    ##Registrando usuario
    result = register_user("test123", "abc")
    assert(result["success"], 1)

    ##Registrando usuario repetido
    result = register_user("test123", "abc")
    assert(result["success"], 0)

def test_login_user():
    ##Login User existente
    result = login_user("test123", "abc")
    assert(result["success"], 1)

    ##Login User Inexistente
    result = register_user("NaoExiste", "abc")
    assert(result["success"], 0)

    ##Login Senha Incorreta
    result = register_user("test123", "Errada")
    assert(result["success"], 0)

def test_logout_user():
    login_user("test123", "abc")
    result = logout()
    assert(result["success"]==0)