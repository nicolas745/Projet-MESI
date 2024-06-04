from .db import DB
class sqluser():
    def __init__(self) -> None:
        self.db=DB()
        pass
    def SelectDataPublicUser(self):
        self.db.open()
        membres=self.db.execute("SELECT `id`, `username`, `email` FROM users;")
        self.db.close()
        return membres
    def delete(self,listid:list):
        self.db.open()
        for id in listid:
            self.db.execute("DELETE FROM users WHERE id = ?;",[id])
        self.db.commit()
        self.db.close()
    def SELECTuserGetPassword(self,user):
        self.db.open()
        res=self.db.execute("SELECT `id`,`password` FROM users WHERE username=?",[user])
        self.db.close()
        return res
    def INSERTuser(self, username, password):
        self.db.open()
        self.db.execute("INSERT INTO users (username, password) VALUES (?, ?)", [username, password])
        self.db.commit()
        self.db.close()