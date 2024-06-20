from flask import Blueprint, render_template, request, flash
from project.blueprints.turma.turmaService import *
from project.blueprints.turma.matriculaService import *
from project.blueprints.turma.turmaRepo import TURMA_DB_URI

app_turmas = Blueprint("turma", __name__, url_prefix='/turma')
pathToFile = TURMA_DB_URI


@app_turmas.route('/', methods=['GET', 'POST'])
def turmaConsulta():
    turma = None
    if request.method == 'POST':
        if 'atualizar' in request.form:
            dados = {key: value for key, value in {
                'cod_curso': request.form['cod_curso'],
                'matrProf': request.form['matrProf'],
                'horario': request.form['horario'],
                'filial': request.form['filial']
            }.items() if value}

            result = atualizaDadosTurma(
                codTurma=request.form["cod_turma"], dadosTurma=dados, pathToFile=pathToFile)
            if result["success"] == 6:
                flash(result["message"], "success")
            else:
                flash(result["message"], "danger")
        if 'apagar' in request.form:
            result = excluiTurma(codTurma=request.form["codTurma"], pathToFile=pathToFile)
            if result["success"] == 9:
                flash(result["message"], "success")
            else:
                flash(result["message"], "danger")
        elif 'consulta' in request.form:
            result = consultaTurma(codTurma=request.form["codTurma"], pathToFile=pathToFile)
            if result["success"] == 3:
                flash(result["message"], "success")
                turma = result["turma"]
            else:
                flash(result["message"], "danger")
        elif 'adicionar' in request.form:
            result = addAlunoTurma(matrAluno=request.form["matricula"], codTurma=request.form["turma"], pathToFile=pathToFile)
            if result["success"] == 6:
                flash(result["message"], "success")
            else:
                flash(result["message"], "danger")
        elif 'deletar' in request.form:
            result = removeAlunoTurma(matrAluno=request.form["matricula"], codTurma=request.form["turma"], pathToFile=pathToFile)
            if result["success"] == 9:
                flash(result["message"], "success")
            else:
                flash(result["message"], "danger")
    return render_template('turma/consultaturma.html', turma=turma)


# @app_turmas.route('/', methods=['GET', 'POST'])
# def turmaAluno():
#     if request.method == 'POST':
#         elif 'adicionar' in request.form:
#             result = addAlunoTurma(matrAluno=request.form["matricula"], codTurma=request.form["turma"], pathToFile=pathToFile)
#             if result["success"] == 6:
#                 flash(result["message"], "success")
#             else:
#                 flash(result["message"], "danger")
#         elif 'deletar' in request.form:
#             result = removeAlunoTurma(matrAluno=request.form["matricula"], codTurma=request.form["turma"], pathToFile=pathToFile)
#             if result["success"] == 9:
#                 flash(result["message"], "success")
#             else:
#                 flash(result["message"], "danger")
#     return render_template('turma/consultaturma.html')
