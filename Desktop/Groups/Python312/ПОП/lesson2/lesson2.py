#-------------------------------------Практика------------------------------------------------#
#
# # Перевод Из мм в м
# mm = input()
# mm = int(mm)
#
# print(f"m = {(mm/10)/100}")





# # Дано:
# # * кол-во товаров в коризине и их суммарная стоимость
# # (один и тот же товар, цена соответсвена фикисрована на каждый товар)
# # * кол-во товаров, которые нужно удалить из корзины
# #
# # Необходимо:
# # показать сколько осталось товаров в коризне и итоговую стоимость
#
#
# # Алгоритм - последовательный и четкий набор действий
#
# # кол-во товаров =1000 #шт шоколадки
# # их суммарная стоимость = 1000
# # кол-во товаров, которые нужно удалить  = 500 #шт шоколадок
#
# # осталось товаров = кол-во товаров - кол-во товаров, которые нужно удалить = 500
# # итоговую стоимость = осталось товаров * стоимость 1шт = 500
# #   стоимость 1шт =  суммарная стоимость /  кол-во товаров = 1
#
#
#
#
# count_products = 1000
# cost_of_product = 1000
# to_del = 7
#
# price_per_one = cost_of_product / count_products
# print(f'Цена за 1 штуку = {price_per_one}')
#
# count_products -= to_del
# new_price = count_products * price_per_one
# print(f'Осталось {count_products} товаров за {new_price} рублей')



# # ---------------------------------логические тип данных - bool(boolean) -------------------------------------- #
# # True - правда
# # False - ложь
#
# print(f"{0} = ", bool(0))
# print(f"{0.00} = ", bool(0.00))
# print(f"{'пустая строка'} = ", bool(''))
# print(f"{None} = ", bool(None))
# print(f"{'{}'} = ", bool({}))
# print(f"{'()'} = ", bool(()))
# print(f"{'[]'} = ", bool([]))
#
#
# print(f"{1} = ", bool(1))
# print(f"{55} = ", bool(55))
# print(f"{-1} = ", bool(-1))
# print(f"{0.01} = ", bool(0.01))
# print(f"{'_'} = ", bool(' '))

# --------------------------------- операторы сравнения-------------------------------------- #
# >
# >=
# <
# <=
# ==
# !=

# print(f"{'5 == 5'} -> ", bool(5 == 5))
# print(""" '5' == 5  -> """, bool(5 == '5'))
# print(f"{'1 == True'} -> ", bool(1 == True))
# print(f"{'5 == True'} -> ", bool(5 == True))
# print(f"{'bool(5) == True'} -> ", bool(bool(5) == True))
# print(f"{'0 == False'} -> ", bool(0 == False))


# ---------------------------------условные операторы (ветвления)-------------------------------------- #
# if
# elif - (else if)
# else


# n = int(input())
# if n > 0:
#     print(f"n > 0 ->  {n>0}")
#     print("2 action")
#     print("smth action")
#
# print(" the end ")  #Не относится к конкструкции if


# # дано n (целое число)
# # проверить является ли число четным
# n = int(input())
# if n % 2 == 0:
#     print(f"{n} - четное")
# else:
#     print(f"{n} - нечетное")


# -----------------------------Задача-------------------------------------#
# # Пользователь вводит с клавиатуры два числа.
# # Необходимо найти максимум из двух чисел и показать его на
# # экран.
# num1 = 6
# num2 = 6
# if num1 > num2:
#     print(f"{num1} > {num2}")
# else:
#     print(f"{num1} =< {num2}")



# # Пользователь вводит с клавиатуры два числа.
# # Необходимо найти максимум из двух чисел и показать его на
# # экран.
#
# num1 = 6
# num2 = 5
# if num1 > num2:
#     print(f"{num1} > {num2}")
# elif num1 < num2:
#     print(f"{num1} < {num2}")
# else:
#     print(f"{num1} = {num2}")


# # #  ------------------------- Задание ----------------------------------- #
# # Выяснить делится число на 5 и на 3, печатаем "делится на 3 и на 5"
# # если только на 3, печатаем "делится на 3"
# # если только на 5, печатаем "делится на 5"
# # если не делится на 5 и на 3, печатаем "не делится на 3 и на 5"
# num = 15
# if num % 3 == 0 and num % 5 == 0:
#     print("делится на 3 и на 5")
# elif num % 3 == 0:
#     print("делится на 3")
# elif num % 5 == 0:
#     print("делится на 5")
# else:
#     print("не делится на 3 и на 5")


# 3.10 +
# Используется когда в одной конструкции везде используется ==
# match
# case
# _


#  ------------------------- Задание ----------------------------------- #
# дано - номер дня недели
# напечатать название дня недели
num_of_weekday = 1
# if num_of_weekday == 1:
#     print("пн")
# elif num_of_weekday == 2:
#     print("вт")
# # ... и т.д.
# elif num_of_weekday == 7:
#     print("вс")
# else:
#     print("incorrect value")

# match num_of_weekday:
#     case 1: # num_of_weekday == 1:
#         print("пн")
#     case 2:  # num_of_weekday == 2:
#         print("вт")
# # ... и т.д.
#     case 7:  # num_of_weekday == 7:
#         print("вс")
#     case _:# else:
#         print("incorrect value")

# ---------------------------------логические операторы-------------------------------------- #
# and - Логическое И
# or - Логическое ИЛИ
# not - Логическое НЕ

# #  ------------------------- Задание ----------------------------------- #
# # программа Тамогочи (питомец)
# # показатель настроения (0 до 100)
# # 0-20 - очень грустный
# # 21-40 - грустный
# # 41-60 - нейтральный
# # 61-80 - веселый
# # 81-99 -очень веселый
# # 100 - эйфория
# mood = int(input('Введите настроение от 0 до 100: '))
#
# if mood >= 0 and mood <= 20:
#     print('Очень грустный')
# elif mood > 20 and mood <= 40:
#     print('Грустный')
# elif mood > 40 and mood <= 60:
#     print('Нейтральный')
# elif mood > 60 and mood <= 80:
#     print('Веселый')
# elif mood > 80 and mood < 100:
#     print('Очень веселый')
# elif mood == 100:
#     print('Эйфория')
# else:
#     print('Некорректное значение')





# # ----------------------------------- Задание ------------------------------ #
# # посчитать перемитр и площадь прямоугольника (на выбор пользователя)
# a = 6
# b = 4
# choice = "периметр "
# if a > 0 and b > 0:
#     if choice == "периметр ":
#         print(f"периметр  = {(a+b)*2}")
#     elif choice == "площадь":
#         print(f"площадь = {a*b}")
# else:
#     print("неверные данные")


# # -----------------------Способы оформления--------------------------------#
# num = -4
# num2 = -4
# #print("num > 0") if num > 0 else print("num < 0") # тернарный оператор
#
# if num > 0: print("num > 0")
# elif num < 0: print("num < 0")
# else: print("num = 0")






# #  ------------------------- Задание ----------------------------------- #
# # # программа кошелек (статус ("активный", "заблокирован"), баланс >= 0),
# # снятие, пополнение, просмотр баланса
# #
# status = "активный"
# balance = 0
# operation = "снятие"
# match status:
#     case "активный":
#
#         match operation:
#             case "снятие":
#                 print(f"баланс: {balance}")
#                 money = 100  # можно input
#                 if balance - money >= 0:
#                     balance -= money  # balance = balance + money
#                     print(f"баланс: {balance}")
#                 else:
#                     print(f"запрашивая сумма > balance")
#
#             case "пополнение":
#                 print(f"баланс: {balance}")
#                 money = 100 # можно input
#                 balance += money # balance = balance + money
#                 print(f"баланс: {balance}")
#
#             case "просмотр баланса":
#                 print(f"баланс: {balance}")
#
#     case "заблокирован":
#         print("Ваш кошелек заблокирован. Нет доступных операций")
#
#     case _:
#         print("нет такого статуса ")








