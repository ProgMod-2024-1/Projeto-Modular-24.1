from flask import Flask, redirect, url_for
from flask_login import LoginManager
from project.blueprints.principal.principal import principal
from project.blueprints.professor.professor import professor  # Importando o blueprint professor
from project.blueprints.principal.principalRepo import get_user
from project.blueprints.principal.principalService import User

app = Flask(__name__, static_folder="static", static_url_path="/static")

# Registrando os blueprints na aplicação Flask
app.register_blueprint(principal)
app.register_blueprint(professor)  # Registrando o blueprint professor
app.secret_key = "senhaSecreta"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'principal.user_login'

@app.route("/")
def access():
    return redirect(url_for('principal.pagina_principal'))

@login_manager.user_loader
def load_user(user_id):
    user_data = get_user(user_id)
    return User(user_data["username"], user_data["permission"])
    
if __name__ == '__main__':
    app.run(debug=True)
