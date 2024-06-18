from flask import Blueprint,render_template,redirect, request, flash, url_for, jsonify
from project.blueprints.filial.filialService import get_filiais,update_filias, add_filiais, delete_filiais, update_filias
from flask_login import current_user, login_required
from project.utils import adm_required



filial = Blueprint("filial",__name__,url_prefix= '/filial')

@filial.route("/")

@adm_required
def pagina_filiais_route():
    filiais = get_filiais()
    return render_template("filial/filial.html", current_user=current_user, filiais = filiais)

@adm_required
@filial.route("/add_filial", methods=['POST'])
def add_filiais_route():
    data = request.form  # Get the JSON data sent from the client
    
    result = add_filiais(nome=data["nomeFilialNova"], endereco=data["enderecoFilialNova"], cep=data["cepFilialNova"], nAlunos=data["numeroDeAlunosFilialNova"])

    if(result["success"] == 1):
        flash(result["message"], "success")

    else:
        flash(result["message"], "danger")
    
    return redirect(url_for('.pagina_filiais_route'))

@adm_required
@filial.route("/delete_filiais",  methods=['POST'])
def delete_filiais_route():
    data = request.form  # Get the JSON data sent from the client
    
    result = delete_filiais(codigo=data["codigo"])

    if(result["success"] == 1):
        flash(result["message"], "success")

    else:
        flash(result["message"], "danger")
    
    return redirect(url_for('.pagina_filiais_route'))

@adm_required
@filial.route("/update_filiais",  methods=['POST'])
def update_filiais_route():
    data = request.form  # Get the JSON data sent from the client
    result = update_filias(data)

    if(result["success"] == 1):
        flash(result["message"], "success")

    else:
        flash(result["message"], "danger")
    
    return redirect(url_for('.pagina_filiais_route'))