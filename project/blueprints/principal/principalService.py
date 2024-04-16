from project.blueprints.principal.principalRepo import add_user

def register_user(username: str, password:str, permission: int)->object:
    result = add_user(username=username, password=password, permission=permission)
    print(result)
    if result == 1:
        return {
                "success": 1,
                "message": "Registro concluido com sucesso",
                "user":{"username":username,"password":password, "permission": permission}
                }
    elif result == -1:
        return {
                "success": 0,
                "message": "Este usuario ja existe. Tente novamente com outro usuario",
                "user":{"username":username,"password":password, "permission": permission}
                }
    elif result == -2 or result == -3:
        return {
                "success": 0,
                "message": "Ocorreu um erro ao criar o usuario. Tente novamente mais tarde",
                "user":{"username":username,"password":password}
                }

    