from .db import DB
from datetime import datetime
class sqlinfoapi():
    def __init__(self) -> None:
        self.db=DB()
    def insert(self,userid,enddate,perm):
        self.db.open()
        self.db.execute("INSERT INTO api (userid,enddate,perm) VALUES (?,?,?) ",[userid,enddate,perm])
        self.db.commit()
        res=self.db.execute("SELECT `id` FROM api WHERE userid=? AND enddate=? AND perm=?;",[userid,enddate,perm])
        self.db.close()
        return res[0][0]
    def select(self, userid):
        self.db.open()
        datas = self.db.execute("SELECT `id`, `enddate`, `datecreate`, `perm`, `ban` FROM api WHERE userid=?", [userid])
        res = []
        for data in datas:
            if not self.comparer_date(data[1]):
                res.append({
                    "id": data[0],
                    "enddate": data[1],
                    "datecreate": data[2],
                    "ban": data[4],
                    "perm": data[3]
                })
            else:
                self.db.execute("DELETE FROM api WHERE id=?",[data[0]])
        self.db.commit()
        self.db.close()
        return res

    def convertir_date(self, date_str):
        try:
            if not date_str:
                # Si la chaîne est vide ou nulle, retourner None ou une valeur par défaut selon vos besoins
                return None

            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            try:
                date_obj = datetime.strptime(date_str, '%y-%m-%d')
            except ValueError:
                annee_reference = 2000
                annee = int(date_str[-4:])
                date_obj = datetime(annee + annee_reference, int(date_str[5:7]), int(date_str[8:10]))
        return date_obj

    def comparer_date(self, date_str):
        date_obj = self.convertir_date(date_str)
        date_actuelle = datetime.now()

        # Vérifier si la date convertie est None
        if date_obj is None:
            # Choisissez un comportement par défaut, par exemple, considérer la date comme postérieure
            return False

        return date_obj < date_actuelle
