"""
Выведите на экран надпись " Anyone who stops learning
is old, whether at twenty or eighty" Henry Ford на разных
строках. 

Пример вывода:
“Anyone who
    stops
        learning is old,
            whether at twenty or eighty”.
                                Henry Ford
"""
# print(""""Anyone who
#             stops
#                 learning is old,
#                     whether at twenty or eighty".
#                                         Henry Ford""")

################################################################

#print('"Anyone who \n\tstops \n\t\tlearning is old, \n\t\t\twhether at twenty or eighty".\n\t\t\t\t\t\t\tHenry Ford')

################################################################

"""
дана  переменная n = 5, необходимо напечтать ее
"""
# # !!! НЕЛЬЗЯ ОБЪЯВИТЬ ПЕРЕМЕННУЮ БЕЗ ИНИЦИАЛИЗАЦИИ !!! #
# n = 5
# print(n)

################################################################

"""
дана  переменная n = 5, необходимо напечтать результат деления на 2, целую часть и остаток
"""
# n = 5
# print(n/2) # 2.5 - float
# print(n//2) # 2 - int - целая часть 
# print(n%2) #  1 - int - Остаток от деления

################################################################


"""
Дано две цифры. Необходимо создать число, содержащее эти цифры. 
Например 9, 7, тогда нужно сформировать число 97.
"""
# x1 = 7 # первый разряд -единицы
# x2 = 9 # второй разряд - десятки

# x = x2*10 + x1 # 97 - int
# print(x, type(x))

################################################################
x1 = 7 # первый разряд -единицы
x2 = 9 # второй разряд - десятки

# str() - преобразует в строку
x = str(x2) + str(x1) # 97 - str
x = int(x) # int() - преобразует в целое
print(x, type(x))

################################################################

"""
Дан прямоугольник размером 647 x 170. Сколько квадратов 
со стороной 30 можно вырезать из него?
Для решения задачи использовать переменные для задания 
размеров прямоугольника
а также переменную для записи результата
"""
a = 647
b = 170
#result = a*b // 30**2
result = a*b / 30**2
print(result, 'кол-во квадратов со стороной 30 =',int(result)) # int - отбрасывает . и все после нее