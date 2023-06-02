from flask import render_template, request, flash
from app_crypto_trader import app
from app_crypto_trader.models import Api_data
from app_crypto_trader.models_db import Db_data
from datetime import datetime

@app.route("/")
def index():
    data = Db_data.get_data("SELECT * from movements order by date DESC")
    return render_template("index.html", data=data)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    currencies = ['EUR', 'BTC', 'ETH', 'USDT', 'BNB', 'XRP', 'ADA', 'SOL', 'DOT', 'MATIC']
    if request.method == "GET":
        return render_template("purchase.html", currencies=currencies)

    else:
        if request.form['button'] == 'calcular':
            base = request.form['base']
            quote = request.form['quote']
            base_amount = int(request.form['base_amount'])
            pu = Api_data.get_rate(base, quote)
            acquired_amount = Api_data.get_amount_acquired(pu, base_amount)
            return render_template("purchase.html", base=base, quote=quote, base_amount=base_amount, pu=pu, acquired_amount=acquired_amount, currencies=currencies)
        
        elif request.form['button'] == 'confirmar':
            date=datetime.now().date()
            time=datetime.now().strftime("%H:%M:%S")
            base = request.form['base']
            quote = request.form['quote']
            base_amount = int(request.form['base_amount'])
            pu = Api_data.get_rate(base, quote)
            acquired_amount = Api_data.get_amount_acquired(pu, base_amount)
            Db_data.insert([date, time, base, base_amount, quote, acquired_amount])
            return index()
        
@app.route("/status")
def status():
    return render_template("status.html") 

