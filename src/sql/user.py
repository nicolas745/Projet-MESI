from .db import DB
class sqluser():
    def __init__(self) -> None:
        self.db=DB()
        pass
    def getperm(self,id):
        self.db.open()
        res = self.db.execute("SELECT `perm` FROM users WHERE id=?;",[id])
        self.db.close()
        return res[0][0]
    def SelectDataPublicUser(self):
        self.db.open()
        membres=self.db.execute("SELECT `id`, `username`, `email` FROM users;")
        self.db.close()
        res = []
        for membre in membres:
            res.append({
                'ID':membre[0],
                'USER':membre[1],
                'EMAIL':membre[2]
            })
        return res
    def delete(self,listid:list):
        self.db.open()
        for id in listid:
            self.db.execute("DELETE FROM users WHERE id = ?;",[id])
        self.db.commit()
        self.db.close()
    def add(self,username,email,password,perm):
        self.db.open()
        self.db.execute('INSERT INTO users (username, email, password, perm) VALUES (?, ?, ?, ?);',(username,email,password,perm))
        self.db.commit()
        self.db.close()
    def SELECTuserGetPassword(self,user):
        self.db.open()
        res=self.db.execute("SELECT `id`,`password` FROM users WHERE username=?",[user])
        self.db.close()
        return res
