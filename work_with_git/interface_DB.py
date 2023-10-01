# Создать БД с таблицей для класса Товар,
# добавить функционал по добалению,редактированию и удаления записей в талице, 
# Создать класс товар (имя, цена, тип)

import sqlite3 as sq
from product import Product 
#
list_products = [('стул', 500 ,'мебель для зала '), ('стол', 1500 ,'мебель для зала '), ('диван', 20000 ,'мебель для зала ')]

#  прохождения через файл product.py -> объект типа product


# ('стул', 500 ,'мебель для зала ') -> объект типа product


# объект типа product-> добавить в таблицу
def add_product(product):# добалениe Товарa
    pname, price, types = product.name, product.price, product.types 
    return f"INSERT INTO products (pname, price, types) VALUES ('{pname}', {price}, '{types}')"
  
   
with sq.connect("Shop.db") as con:
    cur = con.cursor()
 
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pname TEXT NOT NULL,
            price INTEGER DEFAULT 0,
            types TEXT NOT NULL); """)
    
# ----------------------Интерфейс по добалению,редактированию и удаления записей в талице------------------------------#
    for product in list_products: # product = ('стул', 500 ,'мебель для зала ')
        product = Product(product[0], product[1], product[2]) # product = Product('стул', 500 ,'мебель для зала ')
        
        # Функция добаления
        cur.executescript(add_product(product))
    
    result = cur.execute("SELECT * FROM products;")
    print(result.fetchall())

    # Функция редактирование товара
    
    # Функция удаления товара


