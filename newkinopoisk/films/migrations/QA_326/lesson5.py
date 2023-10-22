# ---------------------------Разбор задачи---------------------------------#

"""#  Задача 3
# Дано два числа .
# Найдите наибольшее четное число среди них.
# Если оно не существует, выведите фразу "not found"

a = int(input("Число 1"))
b = int(input("Число 2"))
if a > b:
    if a%2==0:
        print(a)
    elif b%2==0:
        print(b)
elif b > a:
    if a%2==0:
        print(a)
    elif b%2==0:
        print(b)
else:# a==b
  if a%2==0:
        print(a)
    else:
        print("not found")"""


#-------------------------2 способ  решения-----------------------------#
# #  Задача 3
# # Дано два числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"
#
# a = 6
# b = 7
# if a % 2 == 0 and b % 2 == 0:
#     if a > b:
#         print(a)
#     elif b > a:
#         print(b)
#     else:  # a==b
#         print(a)
# elif a % 2 == 0:
#     print(a)
# elif b % 2 == 0:
#     print(b)
# else:
#     print("not found")




# if elif - практике
# https://highload.today/python-if-else/


#-------------------------ЗАДАЧА-----------------------------#
#  Перевод Из мм в м и наоборот
#
# choice_user = input("""
# Выберите систему перевода
#     1 - Из мм в м
#     2 - Из м в мм """)
# l = 100 #добавьте проверку на >=0
#
# if choice_user == '1':
#     print(f"{l} mm = {l/1000} m")
# elif choice_user == '2':
#     print(f"{l} m = {l * 1000} mm")
# else:
#     print("нет такой команды")






#-------------------------ЗАДАЧА-----------------------------#


# Дано:
# * кол-во товаров в коризине и их суммарная стоимость
# (один и тот же товар, цена соответсвена фикисрована на каждый товар)
# * кол-во товаров, которые нужно удалить из корзины
#
# Необходимо:
# показать сколько осталось товаров в коризне и итоговую стоимость

# Пример
# ВХОДНЫЕ ДАННЫЕ
# кол-во товаров в коризине  = 10
# суммарная стоимость = 1000
# кол-во товаров, которые нужно удалить из корзины =  3

# ВЫХОДНЫЕ ДАННЫЕ
# осталось товаров = 7
# итоговую стоимость = 700
#
#
# count_products = 10
# sum_products = 1000
# count_deleted_products = 3
#
# #  блок с указанием ошибок пользователя
# if count_products <= 0:
#     raise("должен быть > 0") # прерывает работы программы и показывает сообщение
# elif sum_products <= 0:
#     raise("должен быть > 0")
# elif count_deleted_products < 0:
#     raise("должен быть >=0")
#
# if count_products > 0 and sum_products > 0 and count_deleted_products >= 0:
#
#     if count_deleted_products <= count_products:
#         product_price = sum_products / count_products
#         result_count_product = count_products - count_deleted_products
#         result_sum_products = sum_products - (count_deleted_products * product_price)
#         print(f"В корзине осталось {result_count_product} товаров на сумму {result_sum_products} рублей")
#     else:
#         print(f"Нельзя удалить больше {count_products} продуктов")
# else:
#     print("Все значения должны быть больше 0")
#






#-------------------------ЗАДАЧА ПОИСК ОШИБОК-----------------------------#
# дано
#  * кол-во символов в пароле
#  * кол-во цифр в пароле
# пароль может сущетсвовать если есть  хотя бы 6 символов и хотя бы 1 цифра

#---------------------решение которое было--------------------------#
# count_symbols = 10
# count_digit = 3
#
# if count_symbols > 6 or count_digit > 1:
#     print("можно использвоать пароль")
# else:
#     print("нельзя использвоать пароль")

#
# #---------------------решение, которое стало--------------------------#
# count_symbols = 10 # только число
# count_digit = 11 # только число - включено count_symbols
#
# # пароль может существовать если есть  хотя бы 6 символов и
# # хотя бы 1 цифра
# if count_symbols >= 6 and count_digit >= 1 and count_digit <= count_symbols:
#     print("можно использовать пароль")
# else:
#     print("нельзя использовать пароль")


#-------------------------ЗАДАЧА ПОИСК ОШИБОК-----------------------------#
#  перевод в новую систему
# курс  - 1 a = 0.5 b
# проверить верно ли сделать перевод

# Пример
# 5 a -> 5 * 0.5 = 2.5 b
#----------решение, которое было------------#
# a = 10 #только число
# b = 3 #только число
# if b * 5 == a:
#     print("перевод верный")
# else:
#     print("перевод неверный")




# #----------решение, которое стало------------#
# # курс  - 1 a = 0.5 b
# # проверить верно ли сделать перевод
#
#
# a = 10 #только число
# b = 5 #только число
# if a > 0 and b > 0: # не хватало проверки на положительность чисел
#     if b * 2 == a: # был неверный перевод из одной системы в другую
#         print("перевод верный")
#     else:
#         print("перевод неверный")
# else:
#     print("невозможно сравнить")







#------------------------ использование конструкции match-case --------------------- #
#  3.9 +
# дни недели {пн, вт, ср, чт и т.д.}
# какой это номер дня недели (1-7)

# day = 'пн'
# if day == 'пн':
#     print(1)
# elif day == 'вт':
#     print(2)
# # ...
# else:
#     print("нет такого дня недели или введено неверное значение")

# # #-------------------вместо решения выше ---------------------#
# day = 'чт'
# match day:
#     case 'пн':
#         print(1)
#     case 'вт':
#         print(2)
#     case 'ср':
#         print(3)
#     case 'чт':
#         if True:
#             print(4)
#     case _:
#         print('нет такого дня')
#
#
#
# #-------------------------ЗАДАЧА-----------------------------#
# # Перевод Из мм в м, из м в км (и наоборот)
#
#
# choice_user = input("""
# Выберите систему перевода
#     1 - Из мм в м
#     2 - Из м в мм
#     3 - из м в км
#     4 - из км в м
#     5 - из км в мм
#     6 - из мм в км""")
# l = 100 #добавьте проверку на >=0
#
# match choice_user:
#     case '1': # тоже что и  if choice_user == '1'
#         print(f"{l} mm = {l / 1000} m")
#     case '2':
#         print(f"{l} m = {l * 1000} mm")
#     case '3':
#         print(f"{l} m = {l * 1000} km")
#     # ... можете дорешать
#     case _:
#         print("нет такой команды")
#
# start = 'm' #  из которого делается перевод
# end = 'km' #  в который делается перевод
# match start:
#     case 'm':
#         match end:
#             case 'mm':
#                 pass
#             case 'km':
#                 print(l*1000)
#             case _:
#                 pass
#     case 'mm':
#         pass
#     case 'km':
#         pass
#     case _:
#         pass

# ДЗ

#-------------------------ЗАДАЧА ПОИСК ОШИБОК-----------------------------#
# калькулятор
# доступны операции умножить и поделить

num1 = float(input(""))# 5, 0, gfdgfd, *
operation = input("")
num2 = int(input(""))

print(f"num2 = {num2}")

if operation == '*':
    print(num1*num2) # 5, 2
elif operation == '/':
    print(num1*num2) # 5, 2 | 5, 0
else:
    print("нет такой операции")



ппав

#
#

# import sqlite3 as sq
#
# with sq.connect("test.db") as con:
#     cur = con.cursor()
#
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE  NOT NULL,
#             password TEXT NOT NULL,
#             avatar BLOB);""")
#
#     # cur.execute("""
#     #             INSERT INTO users (username, password) VALUES ("'admin);", "admin1234")
#     #             """)
#     # result = cur.execute(f"""
#     #                 SELECT username FROM users WHERE username = \'{name_user}\'
#     #                 """)
#
#     username = "username257"
#     # print('this is username: ' +username )
#     # cur.executescript("""
#     #             INSERT INTO users (username, password) VALUES ('"""+username+"""', "admin1234")
#     #             """)
#
#     username = "'testpass' OR '1'='1';"
#     print("5")
#     print(5)










