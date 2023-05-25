import requests
API_KEY = "A055EF56-5D39-4CE3-BDE4-44D71E7BE2D1"

class ModelError(Exception):
    pass

class Get_exchange:
    def __init__(self, base, quote):
        self.base = base
        self.quote = quote
        self.rate = None
        self.status_code = None
        self.time = None

    def get_data(self, apikey):
        r = requests.get( f'https://rest.coinapi.io/v1/exchangerate/{self.base}/{self.quote}?apikey={apikey}' )
        response = r.json()
        self.status_code = r.status_code
        if r.status_code == 200:
            self.rate = response['rate']
            self.time = response['time']
        else:
            print(f"status: {r.status_code}, error: {response['error']}")
            raise ModelError(f"status: {r.status_code}, error: {response['error']}")
        return self.rate
        
get_rate = Get_exchange("EUR", "BTC")

# Cosulta rate de una moneda


print(get_rate.get_data(API_KEY))