import requests
#from app_crypto_trader.utils import API_KEY
#from app_crypto_trader.form import Form_input

API_KEY = "A055EF56-5D39-4CE3-BDE4-44D71E7BE2D1"

# Funciones requests api

def get_rate(base, quote):
    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{quote}/{base}?apikey={API_KEY}')
    json = r.json()
    #self.status_code = r.status_code
    rate = json["rate"]
    rate_float = float(rate)
    return rate_float

def get_amount_acquired(rate, base_amount):
    acquired_amount = base_amount/rate
    return acquired_amount

rate = get_rate('EUR', 'BTC')
get_acquired = get_amount_acquired(rate, 1000)
print(get_acquired)
