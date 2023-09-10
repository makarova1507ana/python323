import sqlite3 
#https://docs.python.org/3/library/sqlite3.html



# Есть файл с именами, прочитали и записали в список кортежей
# players = [] 
# with open("players.txt","r") as f:
#     for l in f:
#         l = l.split()
#         l = tuple(l)
#         print(l)
#         players.append(l)

# print(players)

games = [(1,0,1,1,1),(1,0,2,2,1),(1,0,3,3,1),(2,0,1,1,1),(2,1,1,2,1),(2,1,2,3,1),(2,1,3,4,1)]# id player_score computer_score step id_player 
"""
games = [{
  "id": 1,
  "player_score": 0,
  "computer_score": 1
  "step": 1 
  "id_player ": 1
}]
"""
for row in range(len(games)):
    games[row] = {"id": games[row][0], "player_score": games[row][1],"computer_score": games[row][2], "step": games[row][3], "id_player ": games[row][4]}
print(games)
with sqlite3.connect("knb.db") as con:
    cur = con.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS players(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  pname VARCHAR(50) NOT NULL  );
                  
                CREATE TABLE IF NOT EXISTS games(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  player_score INTEGER,
                  computer_score INTEGER,
                  step INTEGER,
                  id_player INTEGER,
                  FOREIGN KEY (id_player) REFERENCES players);
                  
                CREATE TABLE IF NOT EXISTS result_games(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  count_steps INTEGER,
                  winner TEXT,
                  id_player INTEGER,
                  FOREIGN KEY (id_player) REFERENCES players);
                """) 
    #----------------------------Способы добавки данных------------------------------------#
    # 1 СПОСОБ
    # cur.execute("""
    #             INSERT INTO players (pname) VALUES ("Fred"), ("Vanya")
    #             """) 
    
    # 2 СПОСОБ
    # for player in players:
    #   cur.execute("INSERT INTO players VALUES (NULL, ?)", player)
     
    # 3 СПОСОБ
    #cur.executemany("INSERT INTO players VALUES (NULL, ?)", players)

    # 4 СПОСОБ
    # cur.execute("INSERT INTO players VALUES (NULL, :player_name)", {'player_name': "Egor"})


    result = cur.execute("""
                SELECT * FROM players;
                """) 
    for row in result.fetchall():
        print(row)
    #print(result.fetchall()) # надо посмотреть