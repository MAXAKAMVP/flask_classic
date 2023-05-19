from app import app
from flask import render_template

@app.route("/")
def index():

    datos_movimiento = [
        {'date':'2023-05-18', 'time':'16:35:55', 'coin_from':'BTC', 'amount_from':'10.0', 'coin_to':'ETH', 'amount_to':'20.0'},
        {'date':'2023-05-18', 'time':'16:35:55', 'coin_from':'BTC', 'amount_from':'10.0', 'coin_to':'ETH', 'amount_to':'20.0'},
        {'date':'2023-05-18', 'time':'16:35:55', 'coin_from':'BTC', 'amount_from':'10.0', 'coin_to':'ETH', 'amount_to':'20.0'},
        {'date':'2023-05-18', 'time':'16:35:55', 'coin_from':'BTC', 'amount_from':'10.0', 'coin_to':'ETH', 'amount_to':'20.0'},
    ]

    return render_template("index.html", data = datos_movimiento)

@app.route("/purchase")
def purchase():

    coins = [
        "Seleccione una moneda…", "EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"
    ]
    return render_template("purchase.html", monedas = coins,)

@app.route("/status")
def status():
    return render_template("status.html")