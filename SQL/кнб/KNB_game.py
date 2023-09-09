import sqlite3 
#https://docs.python.org/3/library/sqlite3.html
with sqlite3.connect("knb.db") as con:
    cur = con.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS players(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  pname VARCHAR(50) NOT NULL  );
                """) 
    # cur.execute("""
    #             INSERT INTO players (pname) VALUES ("Fred"), ("Vanya")
    #             """) 
    result = cur.execute("""
                SELECT * FROM players;
                """) 
    for row in result.fetchall():
        print(row)
    #print(result.fetchall()) # надо посмотреть