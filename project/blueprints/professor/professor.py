from flask import Blueprint, render_template, request, redirect, url_for, flash
from .professorRepo import salvar_professor, ler_professores, get_professor, update_professor, atualizar_professor, salvar_professores, validar_codigo, validar_dados, gerar_propostas_turmas, consultar_professor, excluir_professor
from .professorService import registrar_professor
from flask_login import current_user
import re

professor = Blueprint('professor', __name__, url_prefix='/professor')

@professor.route('/criar', methods=['GET'])
def pagina_criar_professor():
    return render_template('professor/criar_professor.html')

@professor.route('/', methods=['GET'])
def listar_professores():
    professores = ler_professores()
    return render_template('professor/professor.html', professores=professores)

@professor.route("/")
def pagina_professor():
    return render_template("professor/professor.html", current_user=current_user)

@professor.route('/atualizar', methods=['GET'])
def pagina_atualizar_professor():
    return render_template('professor/atualizar_professor.html')

@professor.route('/consultar', methods=['GET'])
def pagina_buscar_professor():
    return render_template('professor/consultar_professor.html')

@professor.route('/excluir', methods=['GET'])
def pagina_excluir_professor():
    return render_template('professor/excluir_professor.html')

@professor.route('/criar', methods=['POST'])
def criar_professor():
    nome = request.form['nome']
    horario = request.form['horario']
    matricula = request.form['matricula']
    disponibilidade = request.form['disponibilidade']

    result = registrar_professor(nome, horario, matricula, disponibilidade)

    if result["success"] == 1:
        flash(result["message"], "success")
    else:
        flash(result["message"], "danger")

    return redirect(url_for('professor.listar_professores'))

@professor.route('/atualizar', methods=['POST'])
def atualizar_professor_route():
    matricula = request.form['matricula']
    dados_atualizados = {
        "nome": request.form['nome'],
        "horario": request.form['horario'],
        "disponibilidade": request.form['disponibilidade'],
        "cursos": request.form['cursos']
    }

    result = atualizar_professor(matricula, dados_atualizados)

    if result == "sucesso":
        flash("Professor atualizado com sucesso", "success")
    else:
        flash("Erro ao atualizar professor", "danger")

    return redirect(url_for('professor.listar_professores'))

@professor.route('/exclui_professor', methods=['POST'])
def excluir_professor_route():
    codigoProfessor = request.form['codigoProfessor']
    result = excluir_professor(codigoProfessor)
    if result == "sucesso":
        flash("Professor excluído com sucesso!", "success")
    else:
        flash("Falha ao excluir o professor!", "error")
    return redirect(url_for('professor.listar_professores'))
