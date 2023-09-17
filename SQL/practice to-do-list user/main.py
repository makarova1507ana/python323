import random 
import sqlite3 as sq
""" 
1. создать бд для "списка задач"

2. реализовать регистрацию пользователей

3. сделаем имитицию авторизации

4. реализовать интерфейс по управлению задач
"""
def add_task(text, id_user):
    #  добавить проверка на пустую задача
    return f"INSERT INTO tasks (task, id_user) VALUES ('{text}', {id_user})"

    
with sq.connect("to-do_list.db") as con:
    cur = con.cursor()
 
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE  NOT NULL,
            password TEXT NOT NULL,
            avatar BLOB);
            
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            id_user INTEGER NOT NULL,
            FOREIGN KEY (id_user) REFERENCES users(id));
        """)
    
    
    #---------------------Регистрация пользователя---------------------------#
    # создали админа -  просто так
    # cur.execute("""
    #             INSERT INTO users (username, password) VALUES ("admin", "admin1234")
    #             """) 
    
    name_user = "username257"#"username" + str(random.randint(1,1000)) # пользователь заносит данные например через input
    result = cur.execute(f"""
                SELECT username FROM users WHERE username = \'{name_user}\'
                """) 
    # print(result.fetchall())
    
    
    while len(result.fetchall()) != 0:
        name_user = "username" + str(random.randint(1,1000)) # пользователь заносит данные например через input
        result = cur.execute(f"""
                SELECT username FROM users WHERE username = \'{name_user}\'
                """)
    password = name_user
    
    # преобразуем к двоичному формату
    with open("diagram2.jpg","rb") as f:
        bin_file = f.read()

    avatar = bin_file
    
    cur.execute("INSERT INTO users (username, password, avatar) VALUES (?,?,?)",(name_user, password, avatar)) 
    
    
    
    #---------------------КОНЕЦ  Регистрация пользователя---------------------------#




    #---------------------имитация Авторизации пользователя---------------------------#
    username = "username257"
  
    while result.rowcount != 0:
        result = cur.execute(f"""
                SELECT id,username FROM users WHERE username = \'{username}\'
                """)
      #  "4. реализовать интерфейс по управлению задач"
        comand = input("""
                        1 - add task
                        2 - update task 
                        3 - delete task
                        4 - exit 
                        """) 
        id_user = result.fetchall()[0][0]
        if comand ==  "1":
            task = add_task("task1",id_user)
            cur.executescript(task)# !!! MUST BE SCRIPT 2
        elif comand ==  "2":
            r = cur.execute("SELECT * FROM tasks where id_user=?",(str(id_user)))# !!! MUST BE SCRIPT 
            print(r.fetchall())
        elif comand ==  "4":
            break
    else:
        print("не удалось авторизоваться",)
        
        
    result = cur.execute("""
                SELECT * FROM tasks;
                """) 
    print(result.fetchall())
    # db -> SQL 
    with open("result.sql","w") as f:
        for sql_txt in con.iterdump():
            f.write(sql_txt)

# #прочитать sql 
#     with open("result.sql","r") as f:
#         sql_script = f.read() 
#         cur.executescript(sql_script)           
    # for row in result.fetchall():
    #     print(row)