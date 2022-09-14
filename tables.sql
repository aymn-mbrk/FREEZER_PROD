CREATE TABLE Music2;

CREATE TABLE Music2.playlist (ID INT AUTO_INCREMENT PRIMARY KEY, User TEXT, Title TEXT, Artist TEXT);

INSERT INTO Music2.playlist (User, Title, Artist) VALUES ("maissae", "Bad Romance", "Lady Gaga");
INSERT INTO Music2.playlist (User, Title, Artist) VALUES ("waleed", "Pink Venom", "Blackpink");
INSERT INTO Music2.playlist (User, Title, Artist) VALUES ("khadija", "Umbrella", "Rihanna");
INSERT INTO Music2.playlist (User, Title, Artist) VALUES ("aymane", "Voxel", "Raid");


CREATE TABLE Music2.connexion (ID INT AUTO_INCREMENT PRIMARY KEY, User TEXT, Password TEXT);

INSERT INTO Music2.connexion (User, Password) VALUES ("khadija", "khadija");
INSERT INTO Music2.connexion (User, Password) VALUES ("aymane", "aymane");
INSERT INTO Music2.connexion (User, Password) VALUES ("maissae", "maissae");
INSERT INTO Music2.connexion (User, Password) VALUES ("waleed", "waleed");
