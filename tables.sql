create database Music2;
use Music2;

CREATE TABLE playlist (ID INT AUTO_INCREMENT PRIMARY KEY, User TEXT, Title TEXT, Artist TEXT);

INSERT INTO playlist (User, Title, Artist) VALUES ("user2", "Bad Romance", "Lady Gaga");
INSERT INTO playlist (User, Title, Artist) VALUES ("user1", "Pink Venom", "Blackpink");
INSERT INTO playlist (User, Title, Artist) VALUES ("user3", "Umbrella", "Rihanna");

