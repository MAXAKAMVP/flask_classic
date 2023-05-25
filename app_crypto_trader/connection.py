import sqlite3
from app_crypto_trader.utils import DB_SOURCE

class Connection:
    def __init__(self,querySql,params = []):
        self.con = sqlite3.connect(DB_SOURCE)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)

"""
class DatabaseConnector:
    
    def __init__(self, db_source):
        self.db_source = db_source
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_source)
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS exchange_rates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    time TEXT,
                    base TEXT,
                    amount_base REAL,
                    quote TEXT,
                    amount_quote REAL
                )'''
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, date, time, base, amount_base, quote, amount_qoute):
        query = "INSERT INTO exchange_rates (date, time, base, amount_base, quote, amount_quote) VALUES (?, ?, ?, ?, ?, ?)"
        data = (date, time, base, amount_base, quote, amount_qoute)
        self.cursor.execute(query, data)
        self.conn.commit()

    def fetch_data(self):
        conectar = DatabaseConnector("SELECT * from movements order by date DESC")
        filas = con.res.fetchall() #(1,2023-05-05,sueldo,1600)
        columnas= conectar.res.description #columnas(id,0,0,0,0,0,0)
                                                            
        #objetivo crear una lista de diccionario con filas y columnas
        lista_diccionario=[]
    
        for f in filas:
            diccionario={}
            posicion=0
            for c in columnas:
                diccionario[c[0]] = f[posicion] 
                posicion +=1
            lista_diccionario.append(diccionario)

    def close_connection(self):
        self.conn.close()

db_connector = DatabaseConnector(DB_SOURCE)
db_connector.connect()
db_connector.create_table()
db_connector.insert_data('2023-05-25', '18:19', 'EUR', 100, 'BTC', 10)
"""