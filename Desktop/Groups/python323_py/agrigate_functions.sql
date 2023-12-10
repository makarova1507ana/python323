
CREATE TABLE IF NOT EXISTS Staff (
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    has_child INTEGER NOT NULL, -- 1 - есть ребенок  0 - нет детей
    phone INTEGER UNIQUE NOT NULL,
	salary INTEGER DEFAULT 0 
);

--Агрегатные функции  и группировка данных
/*
INSERT INTO staff (name, has_child, phone, salary) VALUES 
("Антон Иванов", 1,79990001122, 500),
("Иван Иванов", 0,79990301122, 1000),
("Мария Иванова", 1,79980001122, 700),
("Полина Иванова", 0,79970701727, 800),
("Владислад Картонов", 1,79880099122, 750),
("Мария Уварова", 1,79770001122, 230),
("Мария Усупова", 0,79660701452, 500),
("Никита Усупов", 1,79220301452, 550),
("Владимир Иванов", 0,79334567891, 0),
("Ирина Карпова", 1,79787771122, 600),
("Иван Карпов", 1,79787671122, 700),
("Ильдар Володин", 1,79787871122, 540);*/

-- count()
-- sum() 500 + 550 = 1050
-- avg() среднее значение
-- min() 
-- max()


--SELECT  count(id) FROM staff 
--SELECT  sum(salary) FROM staff 
--SELECT  avg(salary) FROM staff 

--SELECT  sum(salary) FROM staff WHERE has_child = 1
--SELECT  count(id),* FROM staff Group By id
SELECT  count(has_child), has_child FROM staff Group By has_child
