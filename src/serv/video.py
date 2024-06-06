from serv.serv import serv , url
from sql.video import sqlvideo
from flask import request
class video(serv):
    @url("/api/video/list",['GET'])
    def listvideo(self):
        if('page' in request.args):
            return sqlvideo().list_videos(10,request.args.get('page'))
        return sqlvideo().list_videos(10,0)
    @url("/video/", ['GET'])
    def video(self):
        return sqlvideo().getinfo(request.args.get('id'))
