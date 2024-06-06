from .db import DB
class sqluser():
    def __init__(self) -> None:
        self.db=DB()
    def SelectDataPublicUser(self):
        self.db.open()
        membres=self.db.execute("SELECT `user_id`, `email` FROM users;")
        self.db.close()
        return membres
    def delete(self,listid:list):
        self.db.open()
        for id in listid:
            self.db.execute("DELETE FROM users WHERE user_id = ?;",(id,))
        self.db.commit()
        self.db.close()
    def SELECTuserGetPassword(self,email):
        self.db.open()
        res=self.db.execute("SELECT `user_id`,`mot_de_passe` FROM users WHERE email=?",(email,))
        self.db.close()
        return res
    def INSERTuser(self, email, password):
        self.db.open()
        self.db.execute("INSERT INTO users (email, mot_de_passe) VALUES (?, ?)", (email, password))
        self.db.commit()
        self.db.close()
    def SELECTuser(self,id):
        self.db.open()
        user=self.db.execute("SELECT * FROM users WHERE user_id=?", ( id,))
        self.db.commit()
        self.db.close()
        if( user.__len__()):
            return user[0]
        return None