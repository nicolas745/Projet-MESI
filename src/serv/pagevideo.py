from serv.serv import serv , url
from sql.video import video
from flask import request
class pagevideo(serv):
    @url("index.html", ['GET'])
    def index(self):
        args = {
            'listvideo':video().list_videos(10,0)
        }
        return self.page("index.html",arg=args)