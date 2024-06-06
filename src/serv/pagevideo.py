#from serv.serv import serv , url
#from sql.video import video
#from flask import Flask, request
#class pagevideo(serv):
#    def __init__(self, app: Flask):
#        super().__init__(app)
#    @url("index.html", ['GET'])
#    def index(self):
#        args = {
#            'listvideo':video().list_videos(10,0)
#        }
#        return self.page("index.html",arg=args)