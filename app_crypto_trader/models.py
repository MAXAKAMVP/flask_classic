import requests
from app_crypto_trader.utils import API_KEY

# Requests api methods
class Api_data:
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

    def get_amount_owned():
        pass

