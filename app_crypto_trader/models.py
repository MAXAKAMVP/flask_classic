import requests
from connection import DatabaseConnector
from utils import API_KEY
from form import Form_inputs

# Funciones requests api

class Crypto_exchange:
    
    def __init__(self, base, quote, amount_base, db_connector):
        self.base = base
        self.amount_base = amount_base
        self.quote = quote
        self.rate = None
        self.status_code = None
        self.time = None
        self.date = None
        self.db_connector = db_connector

    def get_data(self, API_KEY = API_KEY):
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.base}/{self.quote}?apikey={API_KEY}')
        json = r.json()
        #self.status_code = r.status_code
        self.rate = json["rate"]
        self.date = json["time"]
        return self.rate


