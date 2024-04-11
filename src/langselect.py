import os
import importlib
class langselect:
    def __init__(self) -> None:
        self.listlang = {}
        repertoire = "lang"
        for fichier in os.listdir(repertoire):
            if fichier.endswith(".py"):
                if(fichier[:-3]!="lang_global"):
                    module = importlib.import_module("lang."+fichier[:-3])
                    for name, objs in vars(module).items():
                        if isinstance(objs, type) and name!="Enum" and name!="lang_global":
                           self.listlang[name] = objs
                    pass
    def gettext(self,lang,varible):
        return self.listlang[lang][varible].value
    def getlang(self,lang="FR_fr"):
        if(not lang in self.listlang.keys()):
            return self.listlang['FR_fr']
        return self.listlang[lang]
    def getlist(self):
        return self.listlang