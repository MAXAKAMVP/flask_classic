import sqlite3
from .__init__ import DB_SOURCE

def select_all():
    con = sqlite3.connect(DB_SOURCE)
    cur = con.cursor()
    res = cur.execute("select * from movements")

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

    con.close()

    return list_dict


class Connection:
    def __init__(self,querySql,params = []):
        self.con = sqlite3.connect(DB_SOURCE)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)