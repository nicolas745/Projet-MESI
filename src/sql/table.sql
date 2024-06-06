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
  pays_id INTEGER NULL,
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


INSERT OR REPLACE INTO Auteur (auteur_id, prenom, nom) VALUES (1, 'Jean', 'Dupont');
INSERT OR REPLACE INTO Auteur (auteur_id, prenom, nom) VALUES (2, 'Marie', 'Curie');
INSERT OR REPLACE INTO Auteur (auteur_id, prenom, nom) VALUES (3, 'Albert', 'Camus');
INSERT OR REPLACE INTO Auteur (auteur_id, prenom, nom) VALUES (4, 'Simone', 'de Beauvoir');
INSERT OR REPLACE INTO Auteur (auteur_id, prenom, nom) VALUES (5, 'Victor', 'Hugo');
INSERT OR REPLACE INTO Auteur (auteur_id, prenom, nom) VALUES (6, 'Emile', 'Zola');
INSERT OR REPLACE INTO Auteur (auteur_id, prenom, nom) VALUES (7, 'Marcel', 'Proust');


INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (1,'Description 1', 'Title 1', 'video1.mp4', 'image1.png', 1);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (2,'Description 2', 'Title 2', 'video2.mp4', 'image2.png', 2);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (3,'Description 3', 'Title 3', 'video3.mp4', 'image3.png', 3);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (4,'Description 4', 'Title 4', 'video4.mp4', 'image4.png', 4);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (5,'Description 5', 'Title 5', 'video5.mp4', 'image5.png', 5);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (6,'Description 6', 'Title 6', 'video6.mp4', 'image6.png', 6);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (7,'Description 7', 'Title 7', 'video7.mp4', 'image7.png', 7);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (8,'Description 8', 'Title 8', 'video7.mp4', 'image8.png', 3);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (9,'Description 9', 'Title 9', 'video7.mp4', 'image9.png', 1);