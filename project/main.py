from project.blueprints.principal.principal import principal
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from project.blueprints.principal.principalRepo import get_user
from project.blueprints.principal.principalService import User
from project.blueprints.aluno.aluno import aluno

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.register_blueprint(principal)
app.secret_key = "senhaSecreta"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'principal.user_login'

@app.route("/")
def access():
    return redirect(url_for('principal.pagina_principal'))

app.register_blueprint(aluno)

@login_manager.user_loader
def load_user(user_id):
    user_data = get_user(user_id)
    return User(user_data["username"], user_data["permission"])
    
if __name__ == '__main__':
    app.run(debug=True)

