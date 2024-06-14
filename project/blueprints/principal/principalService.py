from project.blueprints.principal.principalRepo import add_user, get_user
from flask_login import UserMixin, login_user, logout_user


class User(UserMixin):
    def __init__(self, id, permission):
        self.id = id
        self.group = permission


def register_user(username: str, password: str, permission: int) -> object:
    result = add_user(username=username, password=password, permission=permission)
    print(result)
    if result == 1:
        return {
            "success": 1,
            "message": "Registro concluido com sucesso",
            "user": {"username": username, "password": password, "permission": permission}
        }
    elif result == -1:
        return {
            "success": 0,
            "message": "Este usuario ja existe. Tente novamente com outro usuario",
            "user": {"username": username, "password": password, "permission": permission}
        }
    elif result == -2 or result == -3:
        return {
            "success": 0,
            "message": "Ocorreu um erro ao criar o usuario. Tente novamente mais tarde",
            "user": {"username": username, "password": password}
        }


def user_login(username: str, password: str) -> object:
    user = get_user(username=username)

    if user is None:
        return {
            "success": 0,
            "message": "Este usuario nao existe",
            "user": {"username": username, "password": password}
        }

    elif password == user["password"]:

        user = User(user["username"], user["permission"])
        login_user(user)
        return {
            "success": 1,
            "message": "Login feito com sucesso",
            "user": {"username": username, "password": password}
        }

    else:
        return {
            "success": 0,
            "message": "Senha incorreta, tente novamente",
            "user": {"username": username, "password": password}
        }


def logout():
    if logout_user():
        return {
            "success": 1,
            "message": "Logout feito com sucesso",
        }

    else:
        return {
            "success": 0,
            "message": "Nao foi possivel fazer logout, tente novamente",
        }
