const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const path = require('path');
class Sql {
  constructor() {
    this.dbPath = path.resolve(__dirname, 'database.db');
    this.sqlFilePath = path.resolve(__dirname, 'table.sql');
    this.db = new sqlite3.Database(this.dbPath, (err) => {
      if (err) {
        console.error(err.message);
      } else {
        console.log('Base de données SQLite créée avec succès.');
      }
    });
    fs.readFile(this.sqlFilePath, 'utf8', (err, data) => {
      if (err) {
        console.error('Erreur lors de la lecture du fichier .sql', err);
        return;
      }
      data = data.replace(/\n/g, ' ');
      this.db.exec(data, (err) => { 
        if (err) {
          console.error('Erreur lors de l\'exécution du fichier .sql', err);
        } else {
          console.log('Tables créées avec succès.');
        }
        this.db.close();
      });
    });
  }
}
module.exports = Sql