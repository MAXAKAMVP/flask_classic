import requests
from __init__ import API_KEY
from connection import Connection
"""
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
# Funciones base de datos.

def select_all():
    connect = Connection("SELECT * from movements order by date DESC")
    rows = connect.res.fetchall()
    columns = connect.res.description
                                                          
    #objetivo crear una lista de diccionario con filas y columnas
    dict_list = []
    
    for f in rows:
        dict = {}
        position = 0
        for c in columns:
            dict[c[0]] = f[position] 
            posicion +=1
        dict_list.append(dict)

    connect.con.close()
    
    return dict_list