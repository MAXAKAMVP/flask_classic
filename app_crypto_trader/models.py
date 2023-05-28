import requests
from app_crypto_trader.utils import API_KEY
from app_crypto_trader.form import Form_input
#from app_crypto_trader.form import Form_input

# Funciones requests api


form = Form_input()
"""
def get_rate(base, quote):
    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{quote}/{base}?apikey={API_KEY}')
    json = r.json()
    #self.status_code = r.status_code
    rate = json["rate"]
    return rate

exchange_rate = get_rate(form.base, form.quote)
amount_acquired_result = (form.amount_base / exchange_rate)
        """