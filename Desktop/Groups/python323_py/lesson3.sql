/*Насколько удобно?   см рисунок 1*/
CREATE TABLE IF NOT EXISTS LESSONS(
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
NAME_L VARCHAR(10) NOT NULL,
DATE_TIME INT NOT NULL,
CLASS_ROOM VARCHAR NOT NULL);
 
CREATE TABLE IF NOT EXISTS GROUPS(
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(10) NOT NULL,
ID_LESSON INT,
FOREIGN KEY (ID_LESSON) REFERENCES LESSONS (ID));


CREATE TABLE IF NOT EXISTS STUDENTS(
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(10) NOT NULL,
id_group INT,
FOREIGN KEY (id_group) REFERENCES GROUPS (ID));
 
-- INSERT INTO LESSONS (NAME_L, DATE_TIME, CLASS_ROOM) VALUES
-- ('MATEMATIKA','22.10.2023/10:30','250_K'),
-- ('INFORMATIKA','22.10.2023/13:10','240_K'),
-- ('FIZRA','24.10.2023/10:30','100_K');
--  
-- INSERT INTO GROUPS (NAME,ID_LESSON) VALUES
-- ('356_G', 1),
-- ('414_G', 3),
-- ('289_G', 2);
-- 
-- INSERT INTO STUDENTS (NAME, id_group) VALUES
-- ('IVAN',1),
-- ('DMITRYI',1),
-- ('ANDREY',2),
-- ('MAX',2),
-- ('ARTUR',3);

/*хочу найти конкретную группу и всех студентов*/
-- SELECT * from groups, students WHERE id_group = groups.ID  and groups.name = "356_G" 

/*хочу найти конкретный урок и его группу*/
-- SELECT * from groups, LESSONS WHERE ID_LESSON = LESSONS.ID  and LESSONS.NAME_L = "MATEMATIKA"; 

/*хочу найти конкретный урок и его группу  и всех студентов*/
-- SELECT * from groups, LESSONS, STUDENTS WHERE ID_LESSON = LESSONS.ID  and LESSONS.NAME_L = "MATEMATIKA" and STUDENTS.id_group = GROUPS.ID; 












CREATE TABLE IF NOT EXISTS books(
id integer PRIMARY KEY AUTOINCREMENT UNIQUE,
nameb nvarchar(20) 
);



CREATE TABLE IF NOT EXISTS authors(
id integer PRIMARY KEY AUTOINCREMENT UNIQUE,
namea nvarchar(20) 
);


CREATE TABLE IF NOT EXISTS authors_and_books(
id_author INTEGER,
id_book INTEGER,
FOREIGN KEY (id_author) REFERENCES authors(id),
FOREIGN KEY (id_book) REFERENCES books(id));

-- 
-- INSERT INTO authors (namea) VALUES ("Пукарац"), ("Андреловац"), 
-- ушкарац");
-- INTO books (nameb) VALUES ("май прекрасный"), ("небо"), ("Ночь");
-- and_books VALUES (1,3), (1,2), (2,1), (3,3), (4,2);-- 


/*книга и ее автров*/
-- SELECT * FROM books, authors, authors_and_books 
-- WHERE books.nameb = "небо" AND authors_and_books.id_author = authors.id
-- authors_and_books.id_book = books.id

/*авторы и их книги*/
SELECT nameb, namea FROM books, authors, authors_and_books 
WHERE authors.namea = "Андреловац" AND authors_and_books.id_author = authors.id
AND authors_and_books.id_book = books.id