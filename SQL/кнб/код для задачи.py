animals = [ {"id":1,"orderA":"Корм","animal":"для хомиков"},{"id":2,"orderA":"Корм","animal":"для собак"}, {"id":3,"orderA":"Лакомство","animal":"для котов"}, {"id":4,"orderA":"Корм","animal":"для кошек"}]

import sqlite3

with sqlite3.connect("lesson.db") as con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS animal_eat")

    cur.execute('''

                 create table if not exists animal_eat

                 (

                    id integer primary key autoincrement,

                    orderA text,

                    animal text

                 );

                 ''')

    for animal in animals:

        cur.execute('insert into animal_eat values(:id, :orderA, :animal)',animal)

    result = cur.execute("""

                SELECT * FROM animal_eat;

                """)

    for row in result.fetchall():

        print(row)