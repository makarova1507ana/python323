# # ----------------- Задание -----------------  #
# """
# Напишите программу, которая будет считать полную
# стоимость всех товаров или со скидкой.
# Пользователь определяет кол-во товаров и цену за одну штуку
# """
#
# # 1 получить от пользователя кол-во товаров и цену за одну штуку
# count, cost, sale = int(input("count of items: ")), int(input("your cost: ")), int(input("your sale: "))
#
# # 2 предоставить пользователю выбор :
# #   * сумма товаров без учета скидки
# #   * сумма товаров с учетом скидки
# is_sale = input("Хотите ли посчитать сумма товаров со скидкой?")
# if is_sale == "да":
#     print(f" ваша сумма товаров со скидкой: {count*cost*(1-sale/100)}")
# if is_sale == "нет":
#     print(f" ваша сумма товаров  без скидки: {count*cost}")


#
# # ----------------- Задание -----------------  #
# """
# Напишите программу.
# Пользователь выбирает фигуру (квадрат или треугольник),
# черепеха рисует выбранную фигуру
# """
#
# from turtle import*
# from time import *
# figure = input('Выберете фигуру, квадрат или треугольник ').lower()# lower() -если написали с большой, переведет  в нижний регситр
# if figure == 'квадрат':
#     forward(120)
#     right(90)
#     forward(120)
#     right(90)
#     forward(120)
#     right(90)
#     forward(120)
#     right(90)
#     sleep(5)
#
# if figure == 'треугольник':
#     forward(120)
#     right(120)
#     forward(120)
#     right(120)
#     forward(120)
#     right(120)
#     sleep(5)
#
# # else:
# #     print('Надо выбрать только квадрат или треугольник')





# ЛОГИЧЕСКИЙ ТИП ДАННЫХ bool -> boolean
# True - правда (1)  False - ложь (0)
# числа преобразуется к логическому типу
# 0 - всегда ложь, все остальное правда
# '' - пустая строка это тоже ложь,все остальное правда

# проверить кратно ли число 3
# num = 33
# if num % 3: #  преобразование к логическому типу данных (0-> False)
#     print(f"{num} делится на 3")
# print(bool(0))
# print(bool(2.3))


# # РАБОЧИЙ ВАРИАНТ
# num = 33
# if num % 3 == 0: #  преобразование к логическому типу данных (0-> False)
#     print(f"{num} делится на 3")





#---------------------Вопросы знатокам----------------------------------#

# print(bool(True == 1))# True ->  1 ,   1 -> True
# # print(int(True))
# # print(bool(1))
# print(bool(True == 21))# False -> потому что разные типы данных
# print(bool(True == bool(21)))# True

# print(bool('1' == 1)) # False
# print(type(int('1')))
# print(type(str(1)))


# жизненные примеры
# кофемашины - сварить кофе, перемолоть зерна, вкл/выкл кофемашину
# if условие:
#       commands

# if Нажал ли пользователь кнопку "сварить кофе"?: #True False
#       commands


#------------------------------Задача--------------------------------------#
"""
Напишите программу. Пользователь определяет:
вес конфет (граммы и кг допустимы)
и цену за кг конфет.

Показать итоговую цену.
Показать бонусные баллы? 100 рублей = 1 бонусный балл
"""

# weight = float(input('Вес конфет равен:'))
# price = int(input('Цена за кг конфет равна: '))
# card = input('У вас есть бонусная карта: ')
#
# if price <= 0:
#     print("price must be > 0")
# elif weight <= 0: # elif - иначе если
#     print("weight must be > 0")
# else:
#     summ = weight * price
#     print(f'Итоговая сумма равна {summ}')
#     if card == 'да':
#         print(f'Вам начислено {summ // 100} баллов')
#     if card == 'нет':
#         print('У вас нет баллов')



# # вопрос с ответом да или нет
# is_card = True # да - True    |   нет - False
# if is_card:
#         print(f'Вам начислено {1000 // 100} баллов')
# else: # если is_card = False
#         print('У вас нет баллов')


# -------------------логические операторы----------------------#
# and - логическое И
# or -  логическое ИЛИ
# not - логическое НЕ (отрицание)
# in - множества (посмотрим когда списки)


#--------------------------Задание----------------------------------------#
"""
У отца два ребенка. 
Он решил сводить детей в кино, но сначала планирует узнать их мнение
Если оба ребенка согласны, то все трое пойдут в кино (мама видимо работает)
напишите программу для этой задачи
"""
child1_answer = True # да - True    |   нет - False
child2_answer = True # да - True    |   нет - False

if child1_answer and child2_answer:
    print("идем в кино!!!")
else:
    print("НЕ идем в кино :(")