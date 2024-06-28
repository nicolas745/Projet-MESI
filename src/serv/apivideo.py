from serv.serv import serv , url
from sql.video import video
from flask import Flask, request
class apivideo(serv):
    def __init__(self, app: Flask):
        super().__init__(app)
    @url("/api/video/list",['GET'])
    def listvideo(self):
        if('page' in request.args):
            return video().list_videos(10,request.args.get('page'))
        return video().list_videos(10,0)
    @url("/api/video", ['GET'])
    def video(self):
        return video().getinfo(request.args.get('id'))
    @url('/search', methods=['POST'])
    def search(self):
        print(request.method)
        search_term = request.get_json()['search']
        print(search_term)
        results = video().searchvideo(search_term)
        return results