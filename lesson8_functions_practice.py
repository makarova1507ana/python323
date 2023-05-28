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

l = [1,2,88,99,34]
for el in l:
    print(min_divider(el))







