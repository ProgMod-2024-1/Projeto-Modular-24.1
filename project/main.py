from flask import Flask, redirect, url_for
from flask_login import LoginManager
from blueprints.lista_de_espera.lista_de_espera import lista_espera_bp
from blueprints.principal.principal import principal
from blueprints.principal.principalRepo import get_user
from blueprints.principal.principalService import User

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.register_blueprint(principal, url_prefix='/principal')
app.register_blueprint(lista_espera_bp, url_prefix='/lista_espera')

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


