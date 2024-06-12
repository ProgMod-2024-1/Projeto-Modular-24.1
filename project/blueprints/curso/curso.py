from flask import Blueprint, render_template, request, redirect, url_for, flash
from .cursoRepo import salvar_curso, ler_cursos
from .cursoService import register_pre_requisito, register_professor_disponivel
from flask_login import current_user

curso = Blueprint('curso', __name__, url_prefix='/curso')

@curso.route('/criar', methods=['GET'])
def pagina_criar_curso():
    return render_template('cursos/criar_curso.html')

@curso.route('/', methods=['GET'])
def listar_cursos():
    cursos = ler_cursos()
    return render_template('cursos/curso.html', cursos=cursos)

@curso.route('/criar', methods=['POST'])
def criar_curso():
    nome = request.form['nome']
    descricao = request.form['descricao']
    codigo = request.form['codigo']
    pre_requisitos = request.form['pre_requisitos']
    creditos = request.form['creditos']
    criterios_aprovacao = request.form['criterios_aprovacao']

    novo_curso = {
        'nome': nome,
        'descricao': descricao,
        'codigo': codigo,
        'pre_requisitos': pre_requisitos,
        'creditos': creditos,
        'criterios_aprovacao': criterios_aprovacao
    }

    salvar_curso(novo_curso)
    return redirect(url_for('curso.listar_cursos'))

@curso.route("/")
def pagina_curso():
    return render_template("curso/curso.html", current_user=current_user)

@curso.route("/register_pre_requisito", methods=["POST", "GET"])
def register_pre_requisito_route():
    if request.method == 'POST':
        result = register_pre_requisito(codCurs=request.form["codCurs"], codPreReq=request.form["codPreReq"])
        if result["success"] == 1:
            flash(result["message"], "success")
            return redirect(url_for('.pagina_curso'))
        else:
            flash(result["message"], "danger")
            return render_template("curso/register_pre_requisito.html", data=result["curso"])
    else:
        return render_template("curso/register_pre_requisito.html")

@curso.route("/register_professor_disponivel", methods=["POST", "GET"])
def register_professor_disponivel_route():
    if request.method == 'POST':
        result = register_professor_disponivel(codCurs=request.form["codCurs"], matrProf=request.form["matrProf"])
        if result["success"] == 1:
            flash(result["message"], "success")
            return redirect(url_for('.pagina_curso'))
        else:
            flash(result["message"], "danger")
            return render_template("curso/register_professor_disponivel.html", data=result["curso"])
    else:
        return render_template("curso/register_professor_disponivel.html")
