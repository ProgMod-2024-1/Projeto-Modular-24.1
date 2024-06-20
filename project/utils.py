from flask import current_app, flash
from flask_login import current_user
from functools import wraps


def adm_required(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("LOGIN_DISABLED"):
            pass
        elif current_user == None:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif int(current_user.group) != 3:
            print(current_user.group)
            flash('Usuario nao e adm do sistema', "danger")
            return current_app.login_manager.unauthorized()

        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def professor_required(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("LOGIN_DISABLED"):
            pass
        elif current_user == None:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()

        elif current_user.group != 2:
            flash('Usuario nao e professor', "danger")
            return current_app.login_manager.unauthorized()
        
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def aluno_required(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("LOGIN_DISABLED"):
            pass
        elif current_user == None:
            return current_app.login_manager.unauthorized()        
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        
        elif current_user.group != 1:
            return current_app.login_manager.unauthorized()
        
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def aluno_ou_adm_required(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("LOGIN_DISABLED"):
            pass
        elif current_user == None:
            return current_app.login_manager.unauthorized()        
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        
        elif current_user.group != 1 or current_user.group != 3:
            flash('Usuario nao e aluno ou adm do sistema', "danger")
            return current_app.login_manager.unauthorized()
        
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def professor_ou_adm_required(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("LOGIN_DISABLED"):
            pass
        elif current_user == None:
            return current_app.login_manager.unauthorized()        
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        
        elif current_user.group != 2 or current_user.group != 3:
            flash('Usuario nao e professor ou adm do sistema', "danger")
            return current_app.login_manager.unauthorized()
        
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view