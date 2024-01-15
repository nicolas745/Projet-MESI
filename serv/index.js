class Page {
  constructor(app) {
    let bodyParser = require('body-parser');
    app.use(bodyParser.urlencoded({extended : true}));
    let mustacheExpress = require('mustache-express');
    app.engine('mustache', mustacheExpress()); 
    app.engine('mustache', mustacheExpress(__dirname + '/../views/partials', '.mustache'));
    app.set('view engine', 'mustache');
    app.set('views', __dirname + '/../views'); 
    app.get('*', (req, res) => {
        res.render('index', { title: 'Bonjour', message: 'Bienvenue sur notre site!' });
    });
    app.post('*', (req, res) => {
        res.render('index', { title: 'Bonjour', message: 'Bienvenue sur notre site!' });
    });
  }
} 

module.exports = Page;