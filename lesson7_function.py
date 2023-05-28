## ----------------------enumerate-------------------------------#

# arr = [1,2,3,4]
# print(enumerate(arr))
# for i, el in enumerate(arr): # [(index,element),()]
#     print(f'i = {i} el = {el}')

## задача
# def find_average(numbers):
#     return 0  if len(numbers)==0 else sum(numbers) / len(numbers)
# print(find_average([]))


## напечатать кол-во дней в месяце
# month = int(input('месяц ваш'))
# months31 = [1,3,5,7,8,10,12] 
# months30 = [4,6,9,11] 
# months28 = [2]

# if month in months31: # знаечение in [список значений] проверяет все значения
#     print(31)
# elif month in months30: #если есть, то выполняет
#     print(30)
# elif month in months28:
#     print(28)
# else:
#     print(':(')
 
 
##--------------------второй способ------------------#    
# import calendar

# mount = int(input("Введите номер месяца"))
# try:
#     print(calendar.prmonth(2023, mount))# если что поломается
#     # команда 2
# except:
#     print("Ошибка") # то программа перейдет сюда



# ----------------------- функциии ------------------------- #


""" 
Задание дан список.
необходимо показать только значения, которые оканчиваются на четное число
"""
l = [12 ,21 ,5 ,7, 8] # 12, 8 

# перебрать значения в списке

# для двух целей ниже реализуем функцию
# выяснить какая последняя цифра у этого значения
# делится ли эта цифра на 2 без остатка


# #  !!!!! ФУНКЦИЯ кусок алгоритма, который вы сохранили!!!!!!!!1
# def is_even_last_digit(num):
#     s_num = str(num)
#     if int(s_num[-1]) % 2 == 0:
#         print(num)

# for el in l:
#     is_even_last_digit(el)
        

""" 
задание дан список чисел, необходимо написать функцию, 
которая будет находить произведения всех отрицательных элементов
"""

# def is_negative(num):# объявление
#     if num < 0:
#         print('Отрицательное')
#     else:
#         print('неее')
        
# is_negative(-5)# вызов функции is_negative

# def multiply(l):
#     s = 1
#     for i in l:
#         if is_negative(i):
#             s *= i
#     print(s)

# list_ = [1, 16, -8, 25, -74]
# multiply(list_)



""" 
RETURN что это
"""
# def is_negative(num):# объявление
#     if num < 0:
#         n = 0# 1, 'отрицательное ' return -возвращает значение ( определяет программист) /результат
#     else:
#         return False # 0, 'Не отрицательное ' return -возвращает результат 
#     ##!! ВАЖНО если нет return, ее результат всегда будет None!!!###
# result = is_negative(-5)# вызов функции is_negative теперь вызов превращает в значение
# print(result)
# print(type(result))
# r = None
# print(type(r))
# r = 5

""" 
задание дан список чисел, необходимо написать функцию, 
которая будет находить произведения всех отрицательных элементов
"""
# #--------1-----#
# def is_negative(num):# объявление
#     if num < 0:
#         return True # 1, 'отрицательное ' return -возвращает значение ( определяет программист) /результат
#     return False # 0, 'Не отрицательное ' return -возвращает результат 
# result = is_negative(-5)# вызов функции is_negative теперь вызов превращает в значение

# # ------- 2 -------- # 
# def is_negative(num):# объявление
#     return num < 0 # num < 0 - итак преобраует в логический

# result = is_negative(-5)# вызов функции is_negative теперь вызов превращает в значение
# print(result)
# print(type(result))

# def multiply(l):
#     s = 1
#     for i in l:
#         if is_negative(i):
#             s *= i
#     return s

# list_ = [1, 16, -8, 25, -74]
# result = multiply(list_)
# print(result)
# print(type(result))



# """ 
# даны три стороны треугольника.
# написать функцию на проверку существование СТОРОНЫ
# напечатать все ли стороны могут существовать
# """
# def check_side(side):
#     return side > 0

# a = 5
# b = -3
# c = 4

# for side in a, b, c:
#     print(side, check_side(side))

""" 
даны три стороны треугольника.
написать функцию на проверку существование СТОРОНЫ
напечатать все ли стороны могут существовать
# """
# def check_sides(*sides): # *sides(кортеж) -передача аргументов от 0 до бесконю.
#     for side in sides:
#         if side < 0:
#             return False # а еще является точкой выхода из программы
        
# check_sides()# вернет None
# check_sides(1) # None
# check_sides(1,2) # None
# check_sides(1,-2, -3) # False


def existence(a:int, b:int):
    return a > 0 and b > 0
#print(existence())

sum('1','2')
print()
