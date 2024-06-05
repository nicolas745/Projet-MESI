import os
from flask import render_template,redirect, request, Flask, session
from langselect import langselect
from chameleon import PageTemplate
from sql.user import sqluser
from lang.lang_global import lang_global
def url(path, methods=['GET']):
    def decorator(func):
        setattr(func, 'path', path)
        setattr(func, 'methods', methods)
        return func
    return decorator

class serv:
    def __init__(self, app:Flask):
        self.lang = langselect()
        self.app = app
        res = [namefunc for namefunc in dir(self) if callable(getattr(self, namefunc)) and not namefunc.startswith("__") and namefunc != "app"]
        for func in res:
            fonction_decorator = getattr(self, func)
            if hasattr(fonction_decorator,'path'):
                path_associe = getattr(fonction_decorator, 'path')
                methods_associes = getattr(fonction_decorator, 'methods' )
                if path_associe:
                    self.app.add_url_rule(path_associe, view_func=fonction_decorator, methods=methods_associes)
    def page(self, chemin, **arg):
        if not 'lang' in session:
            session['lang'] = "FR_fr"
        if request.method == "POST":
            if "lang" in request.form.keys():
                session['lang'] = request.form["lang"]
        if session.get("id"):
            arg['user'] = sqluser().SELECTuser(session.get("id"))
        arg['lang'] ={varible.name: varible.value for varible in lang_global}
        arg['lang'].update({variable.name: variable.value for variable in self.lang.getlang(session.get("lang"))})
        arg['listlang'] = [" "]
        arg['listlang'].extend(self.lang.getlist())
        if chemin.endswith("/"):
            chemin = chemin.rstrip("/")
            chemin += "/index.html"
            return(redirect("/"+chemin))
        chemin_complet = os.path.join("templates/www", chemin)
        if os.path.exists(chemin_complet):
            template= PageTemplate(render_template("index.html", page="www/"+chemin, **arg))
            return template.render(**arg)
        elif os.path.exists("templates/www/404.html"):
            return PageTemplate(render_template("index.html", page="www/404.html",**arg)).render(**arg), 404
        else:
            return "404.html not found", 404