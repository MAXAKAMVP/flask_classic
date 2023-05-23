from flask import Flask

app = Flask(__name__)

from app_crypto_trader.routes import *

API_KEY = "A055EF56-5D39-4CE3-BDE4-44D71E7BE2D1"
DB_SOURCE = "data/movimientos.sqlite"

