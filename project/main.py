from project.blueprints.principal.principal import principal
from flask import Flask, redirect, url_for

app = Flask(__name__)
app.register_blueprint(principal)

@app.route("/")
def access():
    return redirect(url_for('principal.pagina_principal'))
    
if __name__ == '__main__':
    app.run(debug=True)
