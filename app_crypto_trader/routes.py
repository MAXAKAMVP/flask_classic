
from flask import render_template, request
#from . import app
from app_crypto_trader import app
from app_crypto_trader.form import Form_input
from app_crypto_trader.models import *
from app_crypto_trader.models_db import Db_data
#from app_crypto_trader.connection import Connection

@app.route("/")
def index():
    #db_connector = Connection("data/movimientos.sqlite")
    data = Db_data.fetch_all()
    return render_template("index.html", data=data)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    #form_input = Form_input()
    currencies = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]
    if request.method == "GET":
        return render_template("purchase.html", currencies=currencies)#, form_input=form_input)
    """
    else:
        if request.form['button'] == 'calc':
            form_input.base = request.form['base']
            form_input.quote = request.form['quote']
            form_input.amount_base = request.form['amount_base']
            form_input.amount_acquired = amount_acquired_result(form_input.amount_base)
            return render_template("purchase.html", currencies=currencies, form_input=form_input)
        elif request.form['button'] == 'confirm':
            # Insertar datos en la base de datos
            db_data = Db_data(form_input)
            db_data.insert()
            return render_template("purchase.html", currencies=currencies, form_input=form_input)

@app.route("/status")
def status():
    return render_template("status.html")
"""

###############################################
"""
#import os
from flask import render_template, request
from app_crypto_trader import app
from app_crypto_trader.form import Form_input
from app_crypto_trader.models import amount_acquired_result
from app_crypto_trader.models_db import Db_data
from app_crypto_trader.connection import Connection

#SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY
#app = Flask(__name__)
@app.route("/")
def index():
    db_connector = Connection("data/movimientos.sqlite")
    data = Db_data.fetch_all()
    return render_template("index.html", data=data)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    form_input = Form_input()
    currencies = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]
    if request.method == "GET":
        return render_template("/purchase", currencies = currencies)

    else:
        if request.form['button'] == 'calc':
            form = [{"base" : form_input.base},
            {"quote" : form_input.quote},
            {"amount_base" : form_input.amount_base},
            {"amount_acquired" : amount_acquired_result}]
            #data = [form_input.date_select.data, form_input.time_select.data, base, amount_base, quote, amount_acquired]
            return render_template("purchase.html", currencies = currencies, form_input = form_input)
        elif request.form_input['button'] == 'confirm':
            Db_data.insert(form_input)


    return render_template("purchase.html", currencies = currencies, form_input = form_input)

@app.route("/status")
def status():
    return render_template("status.html")

def validateForm(datosFormulario):
    errores = []  # Crear lista para guardar errores
    if type(datosFormulario['amount_in']) != float:
        errores.append("El monto debe ser un número")
    elif datosFormulario['amount_in'] == "" or datosFormulario['amount_in'] == 0:
        errores.append("El monto debe ser distinto de 0 y no estar vacío")
    return errores
"""