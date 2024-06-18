from flask import Blueprint, render_template, request, redirect, url_for, flash
from .cursoRepo import salvar_curso, ler_cursos, consultar_curso, excluir_curso, atualizar_curso
from .cursoService import register_pre_requisito, register_professor_disponivel
from flask_login import current_user
import re

curso = Blueprint('curso', __name__, url_prefix='/curso')

def validar_codigo(codigo):
    # Regex para validar se o código tem 3 letras seguidas por 4 números
    return re.match(r'^[A-Za-z]{3}\d{4}$', codigo) is not None

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
    nota = request.form['nota']

    if not validar_codigo(codigo):
        flash('Não foi possível criar o curso: o código deve ter exatamente 3 letras seguidas por 4 números.', 'danger')
        return redirect(url_for('curso.pagina_criar_curso'))

    novo_curso = {
        'nome': nome,
        'descricao': descricao,
        'codigo': codigo,
        'pre_requisitos': pre_requisitos,
        'creditos': creditos,
        'criterios_aprovacao': criterios_aprovacao,
        'nota': nota
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

@curso.route('/exclui_curso', methods=['POST'])
def excluir_curso_route():
    cursos = ler_cursos()
    codigoCurso = request.form['codigoCurso']
    result = excluir_curso(codigoCurso)
    if result == "sucesso":
        flash("Curso excluído com sucesso!", "success")
    else:
        flash("Falha ao excluir o curso!", "error")
    return redirect("/principal")

@curso.route('/consulta_curso', methods=['POST'])
def consultar_curso_route():
    codigoCurso = request.form['codigoCurso']
    result = consultar_curso(codigoCurso)
    if result:
        flash(f'Dados do curso: {result}')
    else:
        flash("Não existe esse curso!", "error")
    return redirect("/principal")

@curso.route('/atualiza_curso', methods=['GET'])
def pagina_atualizar_curso():
    return render_template('cursos/atualizar_curso.html')

@curso.route('/atualizar', methods=['POST'])
def atualizar_curso_route():
    codigoCurso = request.form['codigo']
    result = excluir_curso(codigoCurso)
    if result == "sucesso":
        nome = request.form['nome']
        descricao = request.form['descricao']
        codigo = request.form['codigo']
        pre_requisitos = request.form['pre_requisitos']
        creditos = request.form['creditos']
        criterios_aprovacao = request.form['criterios_aprovacao']
        nota = request.form['nota']

        novo_curso = {
            'nome': nome,
            'descricao': descricao,
            'codigo': codigo,
            'pre_requisitos': pre_requisitos,
            'creditos': creditos,
            'criterios_aprovacao': criterios_aprovacao,
            'nota': nota
        }

        salvar_curso(novo_curso)
        flash("Curso atualizado com sucesso!", "success")
    else:
        flash("Falha ao atualizar o curso!", "error")
    return redirect("/principal")
