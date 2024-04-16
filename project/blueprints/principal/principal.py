from flask import Blueprint,render_template,redirect, request, flash
from project.blueprints.principal.principalService import register_user

principal = Blueprint("principal",__name__,url_prefix= '/principal', template_folder="templates",static_folder="static")

@principal.route("/")
def pagina_principal():
    return render_template("principal.html")

@principal.route("/register", methods = ["POST", "GET"])
def register():

    if request.method =='POST':
        result = register_user(username=request.form["username"], password=request.form["password"], permission=request.form["permission"])

        if(result["success"] == 1):
            pass

        else:
            flash(result["message"], "error")
            return render_template("register.html", data = result["user"])
    
    else:
        return render_template("register.html")