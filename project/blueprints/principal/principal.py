from flask import Blueprint,render_template,redirect

principal = Blueprint("principal",__name__,template_folder="templates")

@principal.route("/")
def index():
    return render_template("principal.html")