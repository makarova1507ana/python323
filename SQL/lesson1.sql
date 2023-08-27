/* CREATE DATABASE testDB  ; /* - создание БД*/
use testDB;/* - подключаемся к  БД*/

/* - создание таблицы*/
/*
CREATE TABLE players ( 
 name_p NVARCHAR(20) NOT NULL,
 score INT(3) default null
);*/

/*Изменить структур таблицы */

/*ALTER TABLE players ADD column id int(10);*/
/*ALTER TABLE players ADD primary key (id); */
/*ALTER TABLE players modify  id int(11)  not null auto_increment; 
*/

/*Добавление записи:*/
/*
INSERT INTO players VALUES(
"Вася", 200, 0
)*//*
INSERT INTO players (score, name_p) 
VALUE
(150, "Вася2"),
(300, "IVan"),
(420, "Vanya");*/

/*ПРОСМОТР записей в таблице*/
-- SELECT * FROM players;
-- SELECT score FROM players;
-- SELECT * FROM players WHERE score=200;
-- SELECT * FROM players WHERE score<200;
-- select * from players;

/*маски*/
select * from players where name_p LIKE "вася%" ;








/*создать таблицу товар (имя_товара, цена)
добавить 3 любые товара
показать товары стоимость, которого больше 500
 */
 /*напишите сами*/
 
 /*удалить*/
--  DROP TABLE players;


/*удалить строку*/
-- DELETE FROM  AUTHORS 
-- WHERE firstname = "Петр" OR firstname = "Иван"; 


/* DROP DATABASE IF EXISTS testDB;/* - удалить БД, если существует*/
