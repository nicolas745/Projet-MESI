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

INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (1, 'Un homme noir rend visite à la famille de sa petite amie blanche.', 'Get Out', 'getout.mp4', 'get_out.jpg', 1);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (2, 'Clark Kent apprend qu''il est un super-héros.', 'Man of Steel', 'manofsteel.mp4', 'man_of_steel.jpg', 2);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (3, 'Devilman Crybaby est une série d''animation ONA japonaise.', 'Devilman Crybaby', 'devilmancrybaby.mp4', 'dmcb.jpg', 3);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (4, 'Les habitants d''une petite ville sont témoins d''un phénomène mystérieux.', 'Nope', 'Nope.mp4', 'nope.jpg', 4);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (5, 'La chronique des familles de l''aristocratie britannique.', 'La Chronique des Bridgerton', 'LaChroniquedesBridgerton.mp4', 'bridgerton.jpg', 5);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (6, 'Un lycéen brillant réveille l''humanité de la pétrification.', 'Dr. Stone', 'drstone.mp4', 'drstone.jpg', 6);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (7, 'Un adolescent sous surveillance électronique suspecte son voisin d''être un tueur en série.', 'Paranoiak', 'paranoiak.mp4', 'paranoiak.jpg', 7);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (8, 'Un acteur et son cascadeur cherchent à se faire un nom dans le Hollywood de 1969.', 'Once Upon A Time In Hollywood', 'OnceUponATimeInHollywood.mp4', 'once_upon_a_time.jpg', 3);
INSERT OR REPLACE INTO contenu (contenu_id, description, titre, video, image, auteur_id) VALUES (9, 'Batman affronte le Joker dans Gotham City.', 'Batman : The Dark Knight', 'Batman.mp4', 'batman.jpg', 1);
