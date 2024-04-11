from flask import Flask
import os
import secrets
import importlib
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
repertoire = "serv"
for fichier in os.listdir(repertoire):
    if fichier.endswith(".py"):
        module = importlib.import_module("serv."+fichier[:-3])
        for name, objs in vars(module).items():
            if isinstance(objs, type):
                if(objs.__name__ in module.__name__):
                    objs(app)

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("port"))