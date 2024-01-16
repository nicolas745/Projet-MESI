class Page {
  constructor(app) {
    let bodyParser = require('body-parser');
    const fs = require('fs');
    app.get('*', (req, res) => {
        let url = 'mesi2024/src'+req.url;
        if (url.endsWith("/")) {
            url = url + "index.html";
        }
        fs.readFile(url, 'utf-8', (erreur, contenuFichier) => {
            if (erreur) {
              console.error('Erreur lors de la lecture du fichier :', erreur.message);
            } else {
              res.end(contenuFichier);
            }
          });
    });
    app.post('*', (req, res) => {
        res.render('index', { title: 'Bonjour', message: 'Bienvenue sur notre site!' });
    });
  }
} 

module.exports = Page;