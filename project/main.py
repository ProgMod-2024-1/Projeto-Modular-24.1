#general imports
from project.blueprints.principal.principal import principal
from project.blueprints.filial.filial import filial
from flask import Flask, redirect, url_for
from flask_login import LoginManager
#lista de espera imports
from project.blueprints.lista_de_espera.lista_de_espera import lista_espera
#principal imports
from project.blueprints.principal.principal import principal
from project.blueprints.principal.principalRepo import get_user
from project.blueprints.principal.principalService import User
#turma imports
from project.blueprints.turma.turma import app_turmas

app = Flask(__name__, static_folder="static", static_url_path="/static")

app.register_blueprint(principal, url_prefix='/principal')
app.register_blueprint(lista_espera, url_prefix='/lista_espera')
app.register_blueprint(app_turmas)

app.register_blueprint(principal)
app.register_blueprint(filial)
app.secret_key = "senhaSecreta"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'principal.login'

@app.route("/")
def access():
    return redirect(url_for('principal.pagina_principal'))

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    user_data = get_user(user_id)
    return User(user_data["username"], int(user_data["permission"]))
    
if __name__ == '__main__':
    app.run(debug=True)


