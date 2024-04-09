const mustache = require('mustache');
const fs = require('fs');
const { dirname } = require('path');
class Page {
    constructor(app) {
        app.get('/', (req, res) => {
            const template = fs.readFileSync(__dirname + '/../web/index.mustache', 'utf8');
            const partials = {
                header: fs.readFileSync(__dirname + '/../web/header.mustache', 'utf8'),
                footer: fs.readFileSync(__dirname + '/../web/footer.mustache', 'utf8'),
                head: fs.readFileSync(__dirname + '/../web/head.mustache', 'utf8'),
                main: fs.readFileSync(__dirname + '/../web/www/index.html', 'utf8')
            };
            const data = {exemple:"hello word!"}
            const html = mustache.render(template, data, partials);
            res.send(html);
        });
    }
}
module.exports = Page;
