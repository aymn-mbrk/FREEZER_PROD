create database Music2;
use Music2;

CREATE TABLE playlist (ID INT AUTO_INCREMENT PRIMARY KEY, User TEXT, Title TEXT, Artist TEXT);

INSERT INTO playlist (User, Title, Artist) VALUES ("maissae", "Bad Romance", "Lady Gaga");
INSERT INTO playlist (User, Title, Artist) VALUES ("waleed", "Pink Venom", "Blackpink");
INSERT INTO playlist (User, Title, Artist) VALUES ("khadija", "Umbrella", "Rihanna");
INSERT INTO playlist (User, Title, Artist) VALUES ("aymane", "Voxel", "Raid");


CREATE TABLE connexion (ID INT AUTO_INCREMENT PRIMARY KEY, User TEXT, Password TEXT);

INSERT INTO connexion (User, Password) VALUES ("khadija", "khadija");
INSERT INTO connexion (User, Password) VALUES ("aymane", "aymane");
INSERT INTO connexion (User, Password) VALUES ("maissae", "maissae");
INSERT INTO connexion (User, Password) VALUES ("waleed", "waleed");
