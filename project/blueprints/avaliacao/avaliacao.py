from flask import Blueprint,render_template,redirect, request, flash, url_for, jsonify
from project.blueprints.avaliacao.avaliacaoService import get_avaliacoes, registra_avaliacoes, seek_avaliacoes, muda_avaliacoes, deleta_avaliacoes
from flask_login import current_user



avaliacao = Blueprint("avaliacao",__name__,url_prefix= '/avaliacao')

#Página que mostra todas as avaliações do professor
@avaliacao.route("/")
def mostrar_avaliacoes_route():
    avaliacoes = get_avaliacoes()
    return render_template("avaliacao/mostra-avaliacoes.html", current_user=current_user, avaliacoes = avaliacoes)


#Página onde um professor pode registrar uma nova avaliação
@avaliacao.route("/registrar_avaliacoes", methods=['POST', 'GET'])
def registrar_avaliacoes_route():

    if request.method == 'POST':
        data = request.form
        for key in data.keys():
            print(key)

        perguntas = []
        for i in range(10):
            question_text = request.form.get(f'question_text_{i}')
            if question_text:
                perguntas.append(question_text)

        novaAval = {"perguntas":perguntas, "correcoes":[], "info": {"turma": data["turmaAvaliacao"], "codAval": data["codigoAvaliacao"], "curso": data["nomeCurso"], "corretor":""}}

        result = registra_avaliacoes(novaAval)

        if(result["success"] == 1):
            flash(result["message"], "success")
        else:
            flash(result["message"], "danger")


        return redirect(url_for('.mostrar_avaliacoes_route'))
    else:
        return render_template("avaliacao/registra-avaliacao.html", current_user=current_user, num_perguntas=10)
    

#Rota para deletar uma avaliação
@avaliacao.route("/deletar_avaliacoes")
def deletar_avaliacoes_route():

    turma = request.args.get('turma')
    codAval = request.args.get('codAval')
    curso = request.args.get('curso')

    aval = seek_avaliacoes(turma, codAval, curso)

    result = deleta_avaliacoes(aval)

    if(result["success"] == 1):
        flash(result["message"], "success")
    else:
        flash(result["message"], "danger")


    return redirect(url_for('.mostrar_avaliacoes_route'))


#Página onde um professor pode ver todas as informações sobre uma avaliação específica
@avaliacao.route("/ver_avaliacoes")
def ver_info_avaliacoes_route():

    turma = request.args.get('turma')
    codAval = request.args.get('codAval')
    curso = request.args.get('curso')

    data = seek_avaliacoes(turma, codAval, curso)

    return render_template("avaliacao/ver-avaliacao.html", avaliacao=data)


#Página onde um professor pode alterar as questões de uma avaliação
@avaliacao.route("/mudar_questoes", methods=['POST', 'GET'])
def mudar_questoes_route():

    turma = request.args.get('turma')
    codAval = request.args.get('codAval')
    curso = request.args.get('curso')
    
    aval = seek_avaliacoes(turma, codAval, curso)

    if request.method == 'POST':

        perguntas = []
        for i in range(len(aval["perguntas"])):
            question_text = request.form.get(f'question_text_{i}')
            if question_text:
                perguntas.append(question_text)
            else:
                flash("Questões não podem estar em branco!", "danger")
                return redirect(url_for('.mudar_questoes_route', turma=turma, codAval=codAval, curso=curso))
            
        aval["perguntas"] = perguntas

        result = muda_avaliacoes(aval)

        if(result["success"] == 1):
            flash(result["message"], "success")
        else:
            flash(result["message"], "danger")

        return redirect(url_for('.ver_info_avaliacoes_route', turma=turma, codAval=codAval, curso=curso))
        

    else:
        return render_template("avaliacao/mudar-questoes.html", avaliacao=aval, num_perguntas = len(aval["perguntas"]))

#Página onde um professor pode adicionar uma correção
@avaliacao.route("/registrar_correcao", methods=['POST', 'GET'])
def registrar_correcoes_route():

    turma = request.args.get('turma')
    codAval = request.args.get('codAval')
    curso = request.args.get('curso')

    aval = seek_avaliacoes(turma, codAval, curso)

    if request.method == 'POST':
        data = request.form
        for key in data.keys():
            print(key)

        respostas = []
        for i in range(len(aval["perguntas"])):
            question_text = request.form.get(f'answer_text_{i}')
            if question_text:
                respostas.append(question_text)
            else:
                respostas.append("")

        correcao_nova = {"nomeAluno":data["nomeAluno"], "nota":data["notaAvaliacao"], "respostas": respostas, "comentario":data["comentarioAvaliacao"]}
        aval["correcoes"].append(correcao_nova)

        result = muda_avaliacoes(aval)

        if(result["success"] == 1):
            flash(result["message"], "success")
        else:
            flash(result["message"], "danger")


        return redirect(url_for('.ver_info_avaliacoes_route', turma=turma, codAval=codAval, curso=curso))
    else:
        return render_template("avaliacao/registra-correcao.html", current_user=current_user, num_perguntas = len(aval["perguntas"]), avaliacao=aval, criando=1)
    

#Página onde um professor pode mudar uma correção
@avaliacao.route("/mudar_correcao", methods=['POST', 'GET'])
def mudar_correcoes_route():

    turma = request.args.get('turma')
    codAval = request.args.get('codAval')
    curso = request.args.get('curso')
    nomeAluno = request.args.get('nomeAluno')

    aval = seek_avaliacoes(turma, codAval, curso)

    index_correcao = next((i for i, item in enumerate(aval["correcoes"]) if item["nomeAluno"] == nomeAluno), None)

    if request.method == 'POST':
        data = request.form
        for key in data.keys():
            print(key)

        respostas = []
        for i in range(len(aval["perguntas"])):
            question_text = request.form.get(f'answer_text_{i}')
            if question_text:
                respostas.append(question_text)
            else:
                respostas.append("")

        correcao_atualizada = {"nomeAluno":data["nomeAluno"], "nota":data["notaAvaliacao"], "respostas": respostas, "comentario":data["comentarioAvaliacao"]}
 
        aval["correcoes"][index_correcao] = correcao_atualizada

        result = muda_avaliacoes(aval)

        if(result["success"] == 1):
            flash(result["message"], "success")
        else:
            flash(result["message"], "danger")


        return redirect(url_for('.ver_info_avaliacoes_route', turma=turma, codAval=codAval, curso=curso))
    else:
        return render_template("avaliacao/registra-correcao.html", current_user=current_user, num_perguntas = len(aval["perguntas"]), avaliacao=aval, correcao=aval["correcoes"][index_correcao])
    

#Rota para deletar uma correção
@avaliacao.route("/deletar_correcao")
def deletar_correcoes_route():

    turma = request.args.get('turma')
    codAval = request.args.get('codAval')
    curso = request.args.get('curso')
    nomeAluno = request.args.get('nomeAluno')

    aval = seek_avaliacoes(turma, codAval, curso)

    index_correcao = next((i for i, item in enumerate(aval["correcoes"]) if item["nomeAluno"] == nomeAluno), None)

    del aval["correcoes"][index_correcao]

    result = muda_avaliacoes(aval)

    if(result["success"] == 1):
        flash(result["message"], "success")
    else:
        flash(result["message"], "danger")


    return redirect(url_for('.ver_info_avaliacoes_route', turma=turma, codAval=codAval, curso=curso))
