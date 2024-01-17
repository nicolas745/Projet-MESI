
class Page {
  constructor(app) {
    const path = require('path')
    app.get('*', (req, res) => {
      res.sendFile(path.join(__dirname,"./mesi2024/build/index.html"))
    });
    app.post('*', (req, res) => {
        res.render('index', { title: 'Bonjour', message: 'Bienvenue sur notre site!' });
    });
  }
} 

module.exports = Page;