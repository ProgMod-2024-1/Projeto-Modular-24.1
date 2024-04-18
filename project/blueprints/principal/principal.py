from flask import Blueprint,render_template,redirect, request, flash, url_for
from project.blueprints.principal.principalService import register_user, user_login, logout_user
from flask_login import current_user



principal = Blueprint("principal",__name__,url_prefix= '/principal')

@principal.route("/")
def pagina_principal():
    print(current_user)
    return render_template("principal/principal.html", current_user=current_user)

@principal.route("/register", methods = ["POST", "GET"])
def register():

    if request.method =='POST':
        result = register_user(username=request.form["username"], password=request.form["password"], permission=request.form["permission"])
        print(request.form["username"], request.form["password"], request.form["permission"])
        print(result)
        if(result["success"] == 1):
            flash(result["message"], "success")
            return redirect(url_for('.login'))

        else:
            flash(result["message"], "danger")
            return render_template("principal/register.html", data = result["user"])
    
    else:
        return render_template("principal/register.html")
    
@principal.route("/login", methods = ["POST", "GET"])
def login():
    if request.method =='POST':
        result = user_login(username=request.form["username"], password=request.form["password"])
        if(result["success"] == 1):
            print(current_user.id)
            print(current_user.is_authenticated)
            flash(result["message"], "success")
            return redirect(url_for('.pagina_principal'))

        else:
            flash(result["message"], "danger")
            return render_template("principal/login.html", data = result["user"], name=current_user)
    
    else:
        return render_template("principal/login.html")
    
@principal.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.pagina_principal'))
    
