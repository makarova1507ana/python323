#----------------------Улучшаем код------------------------------#
""" 
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. 
Границы диапазона передаются в качестве параметров. Если границы диапазона перепутаны, их нужно поменять 
местами. Если конец диапазона не передан, сделать значение по умолчанию,
равное стартовой границе диапазона
"""
#--------------------------было -----------------------------------#
""" 
def multiplication(frm, to=None):
    if to == None:
        to = frm
    result = 1
    if frm < to:
        for i in range(frm, to + 1):
            result *= i
            print(i, end=' ')
    else:
        for i in range(to, frm + 1):
            result *= i
            print(i, end=' ')
            
    return result
"""
##--------------------------стало--------------------------------#
# def multiplication(frm, to=None):
#     if to == None:
#             to = frm
#     result = 1
#     if frm > to:
#         to, frm = frm, to
#     for i in range(frm, to + 1):
#         result *= i
#         print(i, end=' ')
#     return result
#print('\nпроизведение =', multiplication(3, 5))



#-------------------Задание---------------------#
""" 
реализовать функцию, которая вычисляить факториал передаваемого значения
ввод
2
вывод
2 (2*1)

ввод 
4
вывод
24 (1*2*3*4)
"""
# def f(n):   
#     if n == 1:
#         return n 
#     return f(n-1)*n

# print(f(5))


#-------------------Задание---------------------#
""" 
точная степень двойки
реализовать рекурсию, которая возвращает True , если число является результатом степени двойки,
и false - не является

2 -> true
7 -> false
1024 -> true

"""

# def is_power_of_two(n):
#     if n == 1:  # Если число равно 1, то это степень двойки, возвращаем True.
#         return True
#     elif n % 2 != 0:  # Если остаток от деления числа на 2 не равен нулю,
#                       # то это не степень двойки, возвращаем False.
#         return False
#     else:
#         return is_power_of_two(n // 2)  # Рекурсивно вызываем функцию с аргументом,
#                                         # равным целочисленному частному от деления числа на 2.


# print(is_power_of_two(8))
# print(is_power_of_two(10))
# print(is_power_of_two(1))








#----------------------лямбда-функия--------------------------#

""" 
- анонимная функция
lambda аргументы: выражения
"""
f = lambda x: x*2
print(f(8))

#--------------тоже самое что и----------------#
def g(y):
    return y*2
print(g(8))


print(f(6))

#-----------задание----------------#
""" 
найти полупериметр треугольника
"""
p = lambda a,b,c : (a+b+c)/2 
print(p(1,1,1))

#-----------задание----------------#
""" 
даны стороны треугольника, сделать заключение, может такой треугольник существовать или нет
"""

check_side = lambda side: side>0
#check_side_ = lambda side: True if side>0 else False # но можно короче см выше строка
print(check_side(4))

check_sides = lambda a,b,c: a>0 and b>0 and c>0
print(check_sides(4,3,2))

is_triangle = lambda a,b,c: a+b>c and b+c>a and c+a>b

triangle= [4,3,2]
if check_sides(triangle[0], triangle[1], triangle[2]) and is_triangle(triangle[0], triangle[1], triangle[2]):
    print('есть такой треугольник')
else:
    print('нет ')
# #------не очень подходит для данной задачи---------------#
# check_sides = lambda *sides: [side>0 for side in sides] # вернет [True, True, True] - список
# print(check_sides(4,3,2))



# ---------- filter()------------ #
""" 
создать новый список четных чисел из исходного списка
"""
l = [2,5,34,78889,9,44]
new_l = list(filter(lambda n: n%2==0, [2,5,34,78889,9,44]))


print(new_l)









