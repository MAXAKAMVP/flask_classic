import sqlite3
from utils import DB_SOURCE


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
        query = "INSERT INTO exchange_rates (date, time, base, amount_base, quote, amount_quote) VALUES (?, ?, ?, ?)"
        data = (date, time, base, amount_base, quote, amount_qoute)
        self.cursor.execute(query, data)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

db_connector = DatabaseConnector(DB_SOURCE)
db_connector.connect()
db_connector.create_table()
db_connector.insert_data('2023-05-25', '18:19', 'EUR', 100, 'BTC', )
