from .serv import serv,url
from flask import request, session, redirect
from sql.user import sqluser
import os
import bcrypt
class page(serv):
    def __init__(self, app):
        super().__init__(app)
    def generer_cle(self):
        return bcrypt.gensalt()
    @url('/<path:chemin>',methods=['GET','POST'])
    def all(self,chemin,**arg):
        if(not session.get("id")):
            return redirect('/login.html')
        return self.page(chemin,**arg)
    @url('/')
    def red(self):
        return redirect('/index.html')
    @url('/login.html',methods=['GET','POST'])
    def index(self):
        if(session.get("id")):
            return redirect('/index.html')
        form_datas = request.form
        if "submit" in form_datas:
            if form_datas.get("email") and form_datas.get("password"):
                res=sqluser().SELECTuserGetPassword(form_datas.get("email"))
                print(res)
                if(res.__len__()):
                    if(bcrypt.checkpw(form_datas.get("password").encode("utf-8"),res[0]['mot_de_passe'])):
                        print(res[0])
                        session["id"] = res[0]['user_id']
                        return redirect('/membre/')
        return self.page("login.html")
    @url('/inscription.html',methods=['GET','POST'])
    def inscription(self,**arg):
        if(session.get("id")):
            return redirect('/admin/')
        form_datas = request.form
        if "submit" in form_datas:
            if(form_datas.get("password")) and form_datas.get("rep_password") and form_datas.get('email'):
                if(form_datas.get("password")) == form_datas.get("rep_password"):
                    password = bcrypt.hashpw(form_datas.get("password").encode("utf-8"),self.generer_cle())
                    sqluser().INSERTuser(form_datas.get('email'),password)
                    return redirect("login")
        return self.page('inscription.html',arg=arg)