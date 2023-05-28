"""list_ = [1, 2, 4, 1]

for i in range(len(list_)-2):
    for i2 in range(i+1,len(list_)-1):
        for i3 in range(i2+1,len(list_)):
            res = list_[i] + list_[i2] + list_[i3]
            print(f'{list_[i]} + {list_[i2]} + {list_[i3]} = {res}')"""

#-------------второй способ------------------#
"""
import itertools
list_ = [1, 2, 4, 5]
res = set(itertools.permutations(list_,3))# все возможные комбинации по тройкам
print(res)
"""

#---------------------Задание-----------------------#
"""
Задание
написать функциЮ, которая находит первый наименьший делитель числа отличный от 1
"""
"""
def min_divider(a):# a - число , для которого ищем делитель
    for el in range(2, a+1):
        if a % el == 0:
            return el # точка выхода из функции
"""            
# a = 15
# res = min_divider(a) # print(min_divider(a))
# print(res)

#---------------------Задание-----------------------#
"""
Задание
Используя  функции и предыдущей задаче сравнить два делителя числа,
найти наибольшей делитель
"""
"""
num1 = 5 # наим делитель 5
num2 = 15 # наим делитель 3

# находим делители числа
div1 = min_divider(num1)
div2 = min_divider(num2)

if div1 > div2:
    print(div1)
else:
    print(div2)"""
    


#-------------- сравнение return | break --------------------#
"""
def f():
    for i in range(0, 5):
        for i2 in range(0, 5):
            for i3 in range(0, 5):
                print(i,i2,i3)
                return i
            
f()

for i in range(0, 5):
    for i2 in range(0, 5):
        for i3 in range(0, 5):
            print(i,i2,i3)
            break
        break
    break
"""


#---------------------Задание-----------------------#
"""
Задание
Используя  функции min_divider(), напечатать все минимальные делители для каждого числа
в списке целых чисел
"""
"""
from p.my_functions import min_divider # подключаем p(папка) p.my_functions наш модуль и импортуем функию
l = [1,2,88,99,34]
for el in l:
    print(min_divider(el))"""
    #print(f()) # ошибка




#---------------------Задание-----------------------# 
""" 
даны 2 стороны прямоугольника.
Напечатать площадь и периметр прямоугольника (написать функции для вычисления площади и периметра)
"""
"""
def existence(a, b):
    return a > 0 and b > 0 


def area(a, b):
    if existence(a, b):
        S = a * b
    return S


def per(a, b):
    if existence(a, b):
        P = (a + b) * 2
    return P

a = 4
b = 8
print('Площадь прямугольника', area (a, b))
print('Площадь прямугольника', per(a, b))
"""
#--------------------------Второй способ----------------------------------#
"""
def res(a, b):
    return {'площадь':area(a, b), 'периметр':per(a, b)}

a = 4
b = 8
print(res(a,b))
print('s',res(a,b)['площадь'],'p',res(a,b)['периметр'])
"""


#--------------------параметр с ожидаемыми типами--------------------------#
"""
def existence(a:float, b:float):  #a: float подсказка для программиста
    return float(a) > 0 and float(b) > 0
print(existence('10','2.5'))
"""

"""
напечатать символ (определяет пользовтель) определяет кол-во символов
реализовать функцию
вывод через print

ввод
*
5

вывод
*****
"""
#--------------------параметр по умолчанию--------------------------#
"""def print_symbol(s='*', count=1): #count=1 если пользователь не определил count, то count=1
    print(s*count)
    
print('ab '*4)
print_symbol( count= 7)"""


















def f(n):# суммируем значения от n до нуля
    if n == 0:
        return 2
    return f(n-1)+n 

print(f(2))







