from app_crypto_trader.connection import Connection

class Db_data:
    def get_data(query):
        connect = Connection(query)
        rows = connect.res.fetchall()
        columns = connect.res.description

        dict_list = []
        
        for r in rows:
            dict = {}
            position = 0
            for c in columns:
                dict[c[0]] = r[position] 
                position += 1
            dict_list.append(dict)

        connect.con.close()
        
        return dict_list

    def insert(resgitro_form):
        connect_insert = Connection("INSERT INTO movements (date, time, base, amount_base, quote, amount_quote) VALUES (?, ?, ?, ?, ?, ?)", resgitro_form)
        connect_insert.con.commit()
        connect_insert.con.close()
