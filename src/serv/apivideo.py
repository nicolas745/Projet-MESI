from serv.serv import serv , url
from sql.video import video
from flask import request
class apivideo(serv):
    @url("/api/video/list",['GET'])
    def listvideo(self):
        if('page' in request.args):
            return video().list_videos(10,request.args.get('page'))
        return video().list_videos(10,0)
    @url("api/video", ['GET'])
    def video(self):
        return video().getinfo(request.args.get('id'))