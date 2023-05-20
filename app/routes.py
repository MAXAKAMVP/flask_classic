from app import app
from flask import render_template
from app.models import select_all

@app.route("/")
def index():
    
    movements = select_all()

    return render_template("index.html", data = movements)

@app.route("/purchase")
def purchase():

    coins = [
        "Seleccione una moneda…", "EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"
    ]
    return render_template("purchase.html", monedas = coins,)

@app.route("/status")
def status():
    return render_template("status.html")