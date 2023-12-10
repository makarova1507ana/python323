-- CREATE DATABASE testDB IF NOT EXISTS ;
-- use testDB;

 
CREATE TABLE IF NOT EXISTS STUDENT(
names VARCHAR(50) NOT NULL,
groupName VARCHAR(10));




 /*client and phone*/
CREATE TABLE IF NOT EXISTS clients(
id INTEGER PRIMARY  KEY AUTOINCREMENT,
cname VARCHAR(50) NOT NULL);
 
CREATE TABLE IF NOT EXISTS phones(
number_phone int(12) PRIMARY  KEY  UNIQUE,
id_client INTEGER,
FOREIGN KEY (id_client) REFERENCES clients(id)
);
 
 
--  INSERT INTO clients  VALUES (1,"Иванов Иван"),
-- в Иван"),
-- Иванов Иван");
--  INSERT INTO phones VALUES (89991110002233, 1),
--  (89994444444444, 1),
--  (83331110002255, 2),
--  (84441110002233, 3);
/*INSERT INTO clients (cname)VALUES ("Петров Антон");*/
-- INSERT INTO phones VALUES(80001110001100,4);
/* все номера и всех клиентов */
-- SELECT * FROM phones, clients WHERE id_client = id;

/* всех Петровых  и их номера*/
/*SELECT * FROM phones, clients WHERE id_client = id AND cname  LIKE "Петров%";
*/
/* конкретный номер и его клиента*/
SELECT number_phone, cname FROM phones, clients WHERE number_phone = 83331110002255 AND id_client = id ;

-- INSERT INTO doctors VALUES
-- 
-- ("Олег", "Хирург" , 10500)
-- ог" , 10600)
-- "Уролог" , 10500)
--  FROM doctors WHERE post="Хирург";