import sqlite3
class DB():
    def __init__(self,sqltype="sqlite") -> None:
        self.type = sqltype
        self.sqlname = "base.db"
        self.create()
    def execute(self,query,*data):
        if(self.type=="sqlite"):
            cursor = self.con.cursor()
            cursor.execute(query,*data)
            rows = cursor.fetchall()
            if rows:
                columns = [col[0] for col in cursor.description]
                orders_list = [dict(zip(columns, row)) for row in rows]
                return orders_list
            return []
    def open(self):
        if(self.type=="sqlite"):
            self.con = sqlite3.connect(self.sqlname)
    def close(self):
        if(self.type=="sqlite"):
            self.con.close()
    def create(self):
        with open('table.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        self.open()
        cursor = self.con.cursor()
        cursor.executescript(sql_script)
        self.commit()
        self.close()
    def commit(self):
        if(self.type=="sqlite"):
            self.con.commit()