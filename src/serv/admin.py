from .serv import serv, url
from flask import session, redirect
class admin(serv):
    def __init__(self, app):
        super().__init__(app)
    @url("/membre/home.html")
    def home(self,**arg):
        if(not session.get("id")):
            return redirect('/admin/')
        return self.page("/membre/home.html",arg=arg)