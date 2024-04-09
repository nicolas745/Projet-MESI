CREATE TABLE IF NOT EXISTS pays(
  pays_id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT
);

CREATE TABLE IF NOT EXISTS type(
  type_id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT
);

CREATE TABLE IF NOT EXISTS Auteur(
  auteur_id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT,
  prenom TEXT
);

CREATE TABLE IF NOT EXISTS users(
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  identifiant TEXT,
  mot_de_passe TEXT,
  email TEXT,
  pays_id INTEGER NOT NULL,
  FOREIGN KEY(pays_id) REFERENCES pays(pays_id)
);

CREATE TABLE IF NOT EXISTS contenu(
  contenu_id INTEGER PRIMARY KEY AUTOINCREMENT,
  description TEXT,
  titre TEXT,
  video TEXT,
  image TEXT,
  auteur_id INTEGER NOT NULL,
  FOREIGN KEY(auteur_id) REFERENCES Auteur(auteur_id)
);

CREATE TABLE IF NOT EXISTS genre(
  genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT
);

CREATE TABLE IF NOT EXISTS herachie_contenu(
  herachie_id INTEGER PRIMARY KEY AUTOINCREMENT,
  type_id INTEGER NOT NULL,
  contenu_id INTEGER,
  contenu_id_1 INTEGER,
  FOREIGN KEY(type_id) REFERENCES type(type_id),
  FOREIGN KEY(contenu_id) REFERENCES contenu(contenu_id),
  FOREIGN KEY(contenu_id_1) REFERENCES contenu(contenu_id)
);

CREATE TABLE IF NOT EXISTS Favorie(
  Favorie_id INTEGER PRIMARY KEY AUTOINCREMENT,
  contenu_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY(contenu_id) REFERENCES contenu(contenu_id),
  FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS pays_contenu(
  pays_id INTEGER,
  contenu_id INTEGER,
  PRIMARY KEY(pays_id, contenu_id),
  FOREIGN KEY(pays_id) REFERENCES pays(pays_id),
  FOREIGN KEY(contenu_id) REFERENCES contenu(contenu_id)
);

CREATE TABLE IF NOT EXISTS contenu_genre(
  contenu_id INTEGER,
  genre_id INTEGER,
  PRIMARY KEY(contenu_id, genre_id),
  FOREIGN KEY(contenu_id) REFERENCES contenu(contenu_id),
  FOREIGN KEY(genre_id) REFERENCES genre(genre_id)
);

CREATE TABLE IF NOT EXISTS action_user(
  user_id INTEGER,
  contenu_id INTEGER,
  duree INTEGER,
  note TEXT,
  PRIMARY KEY(user_id, contenu_id),
  FOREIGN KEY(user_id) REFERENCES users(user_id),
  FOREIGN KEY(contenu_id) REFERENCES contenu(contenu_id)
);