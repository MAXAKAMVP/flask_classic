import sqlite3
import requests
#from .utils import API_KEY, TODAY, TIME_NOW, DB_SOURCE

#funciones base de datos
"""
def select_all():
    con = sqlite3.connect(DB_SOURCE)
    cur = con.cursor()
    res = cur.execute("select * from movements")

    rows = res.fetchall()
    columns = res.description

    list_dict = []
    
    for f in rows:
        dict = {}
        position = 0
        for c in columns:
            dict[c[0]] = f[position]
            position += 1
        list_dict.append(dict)

    con.close()

    return list_dict

def insert_movement(date, time, coin_from, amount_from, coin_to, amount_to, p_u):
    con = sqlite3.connect(DB_SOURCE)
    cur = con.cursor()
    instruction = f"INSERT INTO movementsV2 VALUES ('{TODAY}', '{TIME_NOW}', '{coin_from}', '{amount_from}', '{coin_to}', '{amount_to}')"
    res = cur.execute(instruction)
    con.commit()
    con.close()

if __name__ == "__main__":
    insert_movement('2023-05-23', '4:44', 'BTC', '15', 'ETH', '25', '25')
"""
#Funciones requests api

API_KEY = "A055EF56-5D39-4CE3-BDE4-44D71E7BE2D1"
coin_to = "Lo que devuelve el formulario de la web"

r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/EUR/{coin_to}?apikey={API_KEY}")

reply = r.json()
if r.status_code == 200:
    print(reply["rate"])
else:
    print(reply["error"])

"""
def exchange_rate(crypto):
    url = f"https://rest.coinapi.io/v1/exchangerate/{coin_from}/EUR?apikey={API_KEY}"
    res = requests.get(url)
    r = res.jason()
    rate = r["rate"]
    return rate

def buy_coin(currency, crypto):
    rate = exchange_rate(crypto)
    total_amount = currency / rate
    return total_amount

def crypto_trading()
"""