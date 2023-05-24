from datetime import date
from app_crypto_trader import app
from flask import render_template, request
from app_crypto_trader.models import *

@app.route("/")
def index():
    
    movements = select_all()

    return render_template("index.html", data = movements)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():

    coins = [
        "EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"
    ]

    if request.method == "GET":
        return render_template("purchase.html", monedas = coins,)

    else:
        errors = validateForm(request.form)

        if errors:
            return render_template("purchase.html", msg_error = errors)
        else:

            return request.form
        

@app.route("/status")
def status():
    return render_template("status.html")

def validateForm(datosFormulario):
    errores=[]#crear lista para guardar errores
    if  datosFormulario['amount_in'] == type(str):
        errores.append("El monto debe ser un número")
    elif  datosFormulario['amount_in'] == "" or datosFormulario['amount_in'] == 0:
        errores.append("El monto debe ser distinto de 0 y de vacio")
    
    return errores
