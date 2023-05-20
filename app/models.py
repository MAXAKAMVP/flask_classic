import sqlite3


def select_all():
    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()
    res = cur.execute("select * from movements;")

    rows = res.fetchall()
    columns = res.description

    list_dict = []
    
    for f in rows:
        dict = {}
        position = 0
        for c in columns:
            dict[c[0]] = f[position]
            position += 1
        list_dict.append(dict)

    return list_dict