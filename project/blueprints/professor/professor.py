from flask import Blueprint, render_template, request, redirect, url_for, flash
from .professorRepo import salvar_professor, ler_professores
from .professorService import registrar_professor

professor = Blueprint('professor', __name__, url_prefix='/professor')

@professor.route('/criar', methods=['GET'])
def pagina_criar_professor():
    return render_template('professor/criar_professor.html')




@professor.route('/', methods=['GET'])
def listar_professores():
    professores = ler_professores()
    return render_template('professor/professor.html', professores=professores)

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
