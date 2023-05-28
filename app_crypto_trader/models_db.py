from app_crypto_trader.connection import Connection
from app_crypto_trader.form import Form_input

form_input = Form_input

class Db_data:
    def fetch_all():
        conectar = Connection("SELECT * from exchange_rates order by date DESC")
        filas = conectar.res.fetchall()
        columnas = conectar.res.description

        lista_diccionario=[]
        
        for f in filas:
            diccionario={}
            posicion=0
            for c in columnas:
                diccionario[c[0]] = f[posicion] 
                posicion +=1
            lista_diccionario.append(diccionario)

        conectar.con.close()
        
        return lista_diccionario

    def insert(form_input):
        conectarInsert = Connection("INSERT INTO exchange_rates (date, time, base, amount_base, quote, amount_quote) VALUES (?, ?, ?, ?, ?, ?)", form_input)
        conectarInsert.con.commit()
        conectarInsert.con.close()
