from flask import Flask, render_template, request, jsonify
from Modulos.Fuction_x import Trapecio

app = Flask(__name__)

@app.route("/")
def hola():
    return render_template("index.html")

@app.route("/proceso", methods = ["POST"])
def proceso():
    datos = request.get_json()
    a_valor = datos.get('valor_a')
    b_valor = datos.get('valor_b')
    n_valor = datos.get('valor_n')
    fx_valor = datos.get('valor_fx')
    resultado = str(Trapecio(a_valor, b_valor, n_valor, fx_valor))
    return jsonify({'result': resultado})
