from .serv import serv,url
from flask import request, session, redirect
from sql.user import sqluser
import os
import bcrypt
class page(serv):
    def __init__(self, app):

        super().__init__(app)
    @url('/<path:chemin>',methods=['GET','POST'])
    def all(self,chemin,**arg):
        return self.page(chemin,**arg)
    @url('/index.html',methods=['GET','POST'])
    def index(self):
        if(session.get("id")):
            return redirect('/admin/')
        form_datas = request.form
        if form_datas.get("submit"):
            if form_datas.get("username") and form_datas.get("password"):
                res=sqluser().SELECTuserGetPassword(form_datas.get("username"))
                if(res.__len__()):
                    if(bcrypt.checkpw(form_datas.get("password").encode("utf-8"),res[0][1])):
                        session["id"] = res[0][0]
                        return redirect('/membre/')
        return self.page("index.html")
    @url('/inscription.html',methods=['GET','POST'])
    def inscription(self,**arg):
        if(session.get("id")):
            return redirect('/admin/')
        return self.page('inscription.html',arg=arg)