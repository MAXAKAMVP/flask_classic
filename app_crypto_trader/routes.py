from flask import render_template, request
from app_crypto_trader import app
#from app_crypto_trader.form import Form_input
from app_crypto_trader.models import get_amount_acquired, get_rate
from app_crypto_trader.models_db import Db_data
#from app_crypto_trader.connection import Connection
from datetime import datetime

@app.route("/")
def index():
    #db_connector = Connection("data/movimientos.sqlite")
    data = Db_data.fetch_all()
    return render_template("index.html", data=data)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    currencies = ['EUR', 'BTC', 'ETH', 'USDT', 'BNB', 'XRP', 'ADA', 'SOL', 'DOT', 'MATIC']
    if request.method == "GET":
        return render_template("purchase.html", currencies=currencies)

    else:
        if request.form['Button1'] == 'Calcular':
            date = datetime.date
            time = datetime.now
            base = request.form['base']
            quote = request.form['quote']
            base_amount = int(request.form['base_amount'])
            rate = get_rate(base, quote)
            acquired_amount = get_amount_acquired(rate, base_amount)
            data = [date, time, base, base_amount, quote, acquired_amount]
            return render_template("purchase.html", data=data, date=date, time=time, base=base, quote=quote, base_amount=base_amount, rate=rate, acquired_amount=acquired_amount, currencies=currencies)
        
        elif request.form['Button2'] == 'Confirmar':
            db_data = Db_data()
            if db_data.insert(data):
                return 'Datos insertados en la base de datos correctamente.'
            else:
                return 'Error al insertar en la base de datos.'

@app.route("/status")
def status():
    return render_template("status.html")