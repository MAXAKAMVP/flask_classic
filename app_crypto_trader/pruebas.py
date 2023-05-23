import requests

"""
def get_rate():
    url = 'https://rest.coinapi.io/v1/exchangerate/EUR/{crypto_currency}'
    headers = {'X-CoinAPI-Key' : "A055EF56-5D39-4CE3-BDE4-44D71E7BE2D1"}
    response = requests.get(url, headers=headers)
    json = response.json()
    rate = json["rate"]

    return json

#print(get_rate())
v = get_rate()
print(v)
"""

def get_rate(base, quote):
    #r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{quote}?apikey={API_KEY}')
    #json = r.json()
    #return json
    
    json_to_falso = {
        "time": "2023-05-23T09:28:49.0000000Z",
        "asset_id_base": "BTC",
        "asset_id_quote": "USD",
        "rate": 27291.970866279902385442486655
    }
    return json_to_falso
    
	
rate = get_rate('EUR', 'USD')
print(rate["rate"])

API_KEY = "A055EF56-5D39-4CE3-BDE4-44D71E7BE2D1"

class Buy_crypto(API_KEY):
    
    def __init__(self, crypto):
        self.crypto = crypto
        self.rate = None
        self.status_code = None
        self.time = None
        self.date = None

    def get_data(self, crypto, base = "EUR", API_KEY = API_KEY):
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{crypto}?apikey={API_KEY}')
        json = r.json()
        self.rate = json["rate"]
        self.time = json["time"]
        self.date = json["time"]
        self.status_code = json["status_code"]

    def get_exchange(self, amount, rate):
        crypto_amount = amount / rate
        return crypto_amount
    
class Trade_crypto(API_KEY):
    
    def __init__(self, crypto):
        self.crypto = crypto
        self.rate = None
        self.status_code = None
        self.time = None
        self.date = None

    def get_data(self, base, quote, API_KEY = API_KEY):
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{base}/{quote}?apikey={API_KEY}')
        json = r.json()
        self.rate = json["rate"]
        self.time = json["time"]
        self.date = json["time"]
        self.status_code = json["status_code"]

    def crypto_trade(amount, rate):
        new_crypto_amount = amount * rate
        return new_crypto_amount