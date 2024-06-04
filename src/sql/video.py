from .db  import DB
class video:
    def __init__(self) -> None:
        self.db = DB()
    def getinfo(self,id):
        self.db.open()
        info=self.db.execute("SELECT `contenu_id`, `description`, `titre`, `video`, `image`, `Auteur.nom`, `Auteur.prenom` INNER JOIN Auteur ON contenu.auteur_id = Auteur.auteur_id  FROM contenu WHERE contenu_id=?;",[id])
        self.db.close()
        return info
    