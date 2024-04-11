from project.project.blueprints.principal.principal import principal
from flask import Flask

app = Flask(__name__)
app.register_blueprint(principal)

if __name__ == '__main__':
    app.run(debug=True)