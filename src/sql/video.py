from .db  import DB
class video:
    def __init__(self) -> None:
        self.db = DB()
    def getinfo(self,id):
        self.db.open()
        info=self.db.execute("SELECT * FROM contenu INNER JOIN Auteur ON contenu.auteur_id = Auteur.auteur_id  WHERE contenu_id=?;",(id,))
        self.db.close()
        return info

    def list_videos(self, num_elements, page_number):
        self.db.open()
        offset = (page_number - 1) * num_elements
        query = "SELECT * FROM contenu INNER JOIN Auteur ON contenu.auteur_id = Auteur.auteur_id LIMIT ? OFFSET ?;"
        videos = self.db.execute(query, (num_elements, offset))
        self.db.close()
        return videos

    def add_video(self,description, titre ,urlvideo,image,auteur_id ):
        self.db.open()
        query = "INSERT INTO contenu (`description`, `titre`, `video`, `image`, `auteur_id`) VALUES (? , ? , ? , ? , ?);"
        self.db.execute(query, (description, titre ,urlvideo,image,auteur_id  ))
        self.db.close()

    def delete_video(self, id):
        self.db.open()
        query = "DELETE FROM contenu WHERE contenu_id = ?;"
        self.db.execute(query, (id,))
        self.db.close()
    def searchvideo(self,search):
        self.db.open()
        query = "DELETE FROM contenu WHERE titre LIKE ? OR Auteur.nom LIKE ? OR Auteur.prenom LIKE ?;"
        res=self.db.execute(query, (search,))
        self.db.close()
        return res