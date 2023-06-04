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
    
    def get_amount_owned(crypto_buyer):
        connect = Connection(f"SELECT amount_base FROM movements WHERE base = '{crypto_buyer}'")
        base_rows = connect.res.fetchall()
        crypto_sold = 0
        for s in base_rows:
            crypto_sold += s[0]
        connect2 = Connection(f"SELECT amount_quote FROM movements WHERE quote = '{crypto_buyer}'")
        quote_rows = connect2.res.fetchall()
        crypto_bought = 0
        for b in quote_rows:
            crypto_bought += b[0]
        crypto_owned = crypto_bought - crypto_sold
        crypto_owned = float(crypto_owned)
        return crypto_owned

    def get_eur_invested():
        connect = Connection(f"SELECT amount_base FROM movements WHERE base = 'EUR'")
        eur_rows = connect.res.fetchall()
        eur_invested = 0
        for r in eur_rows:
            eur_invested += r[0]
        eur_invested = round(eur_invested, 2)
        return eur_invested
    def get_eur_recovered():
        connect = Connection(f"SELECT amount_quote FROM movements WHERE quote = 'EUR'")
        eur_rows = connect.res.fetchall()
        eur_recovered = 0
        for r in eur_rows:
            eur_recovered += r[0]
        eur_recovered = round(eur_recovered, 2)
        return eur_recovered

    def insert(resgitro_form):
        connect_insert = Connection("INSERT INTO movements (date, time, base, amount_base, quote, amount_quote) VALUES (?, ?, ?, ?, ?, ?)", resgitro_form)
        connect_insert.con.commit()
        connect_insert.con.close()
