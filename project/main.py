#general imports
from flask import Flask, redirect, url_for, flash
from flask_login import LoginManager
from flask_login import AnonymousUserMixin
#lista de espera imports
from project.blueprints.lista_de_espera.lista_de_espera import lista_espera
#principal imports
from project.blueprints.principal.principal import principal
from project.blueprints.principal.principalRepo import get_user
from project.blueprints.principal.principalService import User
#turma imports
from project.blueprints.turma.turma import app_turmas


#from project.blueprints.filial.filial import filial
from project.db.database import read_db_json, save_cache
from project.cache import cache
from flask_login import logout_user
import os


ALUNO_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","aluno","database","aluno.json")
AVALIACAO_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","avaliacao","database","avaliacao.json")
CERTIFICACAO_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","certificacao","database","certificacao.json")
CRITERIO_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","criterios","database","criterios.json")
CURSO_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","curso","database","curso.json")
FILIAL_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","filial","database","filial.json")
FORMACAO_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","formacao","database","formacao.json")
LISTA_DE_ESPERA_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","lista_de_espera","database","lista_de_espera.json")
USERS_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","principal","database","users.json")
PROFESSOR_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","professor","database","professor.json")
TURMA_DB_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)),"blueprints","turma","database","turma.json")






app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 3000000000000000000000000000000000000000000

cache.init_app(app)
cache.set("aluno",read_db_json(ALUNO_DB_URI))
cache.set("avaliacao",read_db_json(AVALIACAO_DB_URI))
cache.set("certificacao",read_db_json(CERTIFICACAO_DB_URI))
cache.set("criterios",read_db_json(CRITERIO_DB_URI))
cache.set("curso",read_db_json(CURSO_DB_URI))
cache.set("filial",read_db_json(FILIAL_DB_URI))
cache.set("formacao",read_db_json(FORMACAO_DB_URI))
cache.set("lista_de_espera",read_db_json(LISTA_DE_ESPERA_DB_URI))
cache.set("users",read_db_json(USERS_DB_URI))
cache.set("professor",read_db_json(PROFESSOR_DB_URI))
cache.set("turma",read_db_json(TURMA_DB_URI))


app.register_blueprint(principal, url_prefix='/principal')
app.register_blueprint(lista_espera, url_prefix='/lista_espera')
app.register_blueprint(app_turmas)
#app.register_blueprint(filial)

app.secret_key = "senhaSecreta"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'principal.user_login'

@app.route("/")
def access():
    return redirect(url_for('principal.pagina_principal'))

@app.route("/save")
def save():
    result = save_cache("aluno",ALUNO_DB_URI)
    if result != 1: flash('Nao foi possivel salvar os alunos', "danger")
    result = save_cache("avaliacao",AVALIACAO_DB_URI)
    if result != 1: flash('Nao foi possivel salvar as avaliacoes', "danger")
    result = save_cache("certificacao",CERTIFICACAO_DB_URI)
    if result != 1: flash('Nao foi possivel salvar as certificacoes', "danger")
    result = save_cache("criterios",CRITERIO_DB_URI)
    if result != 1: flash('Nao foi possivel salvar os criterios', "danger")
    result = save_cache("curso",CURSO_DB_URI)
    if result != 1: flash('Nao foi possivel salvar os cursos', "danger")
    result = save_cache("filial",FILIAL_DB_URI)
    if result != 1: flash('Nao foi possivel salvar as filiais', "danger")
    result = save_cache("formacao",FORMACAO_DB_URI)
    if result != 1: flash('Nao foi possivel salvar as formacoes', "danger")
    result = save_cache("lista_de_espera",LISTA_DE_ESPERA_DB_URI)
    if result != 1: flash('Nao foi possivel salvar as listas de espera', "danger")
    result = save_cache("users",USERS_DB_URI)
    if result != 1: flash('Nao foi possivel salvar os usuarios', "danger")
    result = save_cache("professor",PROFESSOR_DB_URI)
    if result != 1: flash('Nao foi possivel salvar os professores', "danger")
    result = save_cache("turma",TURMA_DB_URI)
    if result != 1: flash('Nao foi possivel salvar as turmas', "danger")
    return redirect(url_for('principal.pagina_principal'))


@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None
    print(user_id)
    user_data = get_user(user_id)
    if user_data == None:
        return None
    return User(user_data["username"], int(user_data["permission"]))
    
if __name__ == '__main__':
    app.run(debug=True)
