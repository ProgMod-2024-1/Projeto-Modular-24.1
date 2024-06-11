from flask import Blueprint, render_template, redirect, request, flash, url_for
from project.blueprints.curso.cursoService import register_pre_requisito, register_professor_disponivel
from flask_login import current_user

curso = Blueprint("curso", __name__, url_prefix='/curso')

@curso.route("/")
def pagina_curso():
    print(current_user)
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
