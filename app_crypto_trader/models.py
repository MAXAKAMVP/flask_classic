from app_crypto_trader.utils import API_KEY, API_KEY2
import requests

# Requests api methods
class Api_data:
    def get_rate(base, quote):
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{quote}/{base}?apikey={API_KEY2}')
            
        if r.status_code == 429:
            return "Ha consumido sus 100 peticiones diarias", None
        elif r.status_code != 200:
            return "Las tasas de cambio no están disponibles", None
        else:      
            json = r.json()
            rate = json["rate"]
            rate_float = float(rate)

            return None, rate_float

    def get_amount_acquired(rate, base_amount):
        acquired_amount = base_amount/rate
        acquired_amount = acquired_amount
        return acquired_amount
