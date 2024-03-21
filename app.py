from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "App Cicero Edson Machado v2.0"
