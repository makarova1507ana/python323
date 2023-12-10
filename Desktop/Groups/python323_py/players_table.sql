CREATE TABLE IF NOT EXISTS clients  (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nameC VARCHAR(50) NOT NULL,
  	city VARCHAR(50) NOT NULL);

INSERT INTO clients (nameC, city) VALUES (
("Ivanov Inav",  "Moscow"),
("Petrov petr",  "Volgograd"),
("Olegov Oleg",  "Samara"),
("Smirnov Anton",  "Samara"));

CREATE TABLE IF NOT EXISTS  phones(
	number_ph INT PRIMARY KEY,
  	id_client INT,
  	FOREIGN KEY(id_client) references clients(id)
);


INSERT INTO clients (nameC, city) VALUES (
("Ivanov Inav",  "Moscow"),
("Petrov petr",  "Volgograd"),
("Olegov Oleg",  "Samara"),
("Smirnov Anton",  "Samara"));

INSERT INTO phones VALUES(
(9991110000,	1),
(1001110000,	1),
(9992220000,	2),
(8881110000,	3),
(7771110000,	3),
(6661110000,	3),
(5551110000,	NULL),
(4441110000,	4));


SELECT * FROM phones






























