import sqlite3
from app_crypto_trader.utils import DB_SOURCE

class Connection:
    def __init__(self, querySql, params = []):
        self.con = sqlite3.connect(DB_SOURCE)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql, params)
        