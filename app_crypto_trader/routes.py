from flask import render_template, request, flash
from app_crypto_trader import app
from app_crypto_trader.models import Api_data
from app_crypto_trader.models_db import Db_data
from app_crypto_trader.form import form_validator
from datetime import datetime

@app.route("/")
def index():
    data = Db_data.get_data("SELECT * from movements order by date, time ASC")
    return render_template("index.html", data=data)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    currencies = ['EUR', 'BTC', 'ETH', 'USDT', 'BNB', 'XRP', 'ADA', 'SOL', 'DOT', 'MATIC']
    if request.method == "GET":
        return render_template("purchase.html", currencies=currencies)

    else:
        if request.form['button'] == 'calcular' or request.form["button"] == 'confirmar':
            errors = form_validator(request.form)
            
            if errors == []:
                base = request.form['base']
                quote = request.form['quote']
                base_amount = float(request.form['base_amount'])
                error, pu = Api_data.get_rate(base, quote)
                if error == None:
                    acquired_amount = Api_data.get_amount_acquired(pu, base_amount)

                    if request.form["button"] == 'confirmar':
                        date = datetime.now().date()
                        time = datetime.now().strftime("%H:%M:%S")
                        get_amount_owned = Db_data.get_amount_owned(base)
                        if base != 'EUR' and base_amount > get_amount_owned:
                            errors.append("No tienes suficientes fondos de la mondeda seleccionada")
                            return render_template("purchase.html", errors=errors, base=base, quote=quote, base_amount=base_amount, pu=pu, acquired_amount=acquired_amount, currencies=currencies)
                        else:
                            Db_data.insert([date, time, base, base_amount, quote, acquired_amount])
                            data = Db_data.get_data("SELECT * from movements order by date, time ASC")
                            msg = "movimiento confirmado"
                            return render_template("index.html", msg=msg, data=data)
                    elif request.form['button'] == 'calcular':
                        return render_template("purchase.html", errors=errors, base=base, quote=quote, base_amount=base_amount, pu=pu, acquired_amount=acquired_amount, currencies=currencies)
                else:
                    errors.append(error)
                    return render_template("purchase.html", errors=errors, base=request.form['base'], quote=request.form['quote'], base_amount=request.form['base_amount'], currencies=currencies)
            else:
                return render_template("purchase.html", errors=errors, base=request.form['base'], quote=request.form['quote'], base_amount=request.form['base_amount'], currencies=currencies) 
        
@app.route("/status")
def status():
    eur_invested = Db_data.get_eur_invested()
    eur_recovered = Db_data.get_eur_recovered()
    purchase_value = eur_invested - eur_recovered

    currencies = ['EUR', 'BTC', 'ETH', 'USDT', 'BNB', 'XRP', 'ADA', 'SOL', 'DOT', 'MATIC']
    total = 0
    for currency in currencies:
        if currency != 'EUR':
            amount_owned = Db_data.get_amount_owned(currency)
            pu = Api_data.get_rate('BTC' ,'EUR')
            amount_owned_eur = Api_data.get_amount_acquired(pu[1], amount_owned)
            total = round(float(total + amount_owned_eur), 2)
  
    return render_template("status.html", total=total, currencies=currencies, eur_invested=eur_invested, eur_recovered=eur_recovered, purchase_value=purchase_value) 

"""
                    {% for crypto in currencies %}
                    {% if crypto != 'EUR' %}
                        <li>{{crypto}}:</li>
                    {% endif %}
                    {% endfor %}
                    {% for value in values %}
                    <li>{{value}}:</li>
                    {% endfor %}
"""