# #*****************************methods_lists*************************************#
# # [1,2,'3']
# # Функция == метод ? Нет
# # Одна и та же задачу предоставить готовый алгоритм по решение какой-то проблемы
# # max() - функция -> не имеет привязки  print()
# #  метод -> имеет привязку к какому-ту типу (классу) List = [1,2]
# # List.append(el) - метод, записывает новый элемент в конец списка

# print()
# List = [1, 2]
# print(List)
# List.append('3')
# print(List)

# #print('abc'.count('a')) # count() - метод

########################   Задание     ######################################
"""
Создать список длиной в 10 элеметов в котором на четных будут стоять 1, а на  нечетных 0     
 """
# num1 = 1
# num2 = 0
# size = 10
# List = []
# for counter in range(size):
#     if counter % 2 == 0:
#         print('index', counter,'num', num1)
#         List.append(num1)
#     else:
#         print('index', counter,'num', num2)
#         List.append(num2)
# print(List)

########################   remove и pop     ######################################

# l = [1,2,3,4, 2]
# print(l.remove(2))#удаляет элемент только первый элемент который встретил
# print(l)
# print(l.pop(1))#удаляет элемент по иднексу
# print(l)

############ пример ############
# list_ = []

# n = 0

# while len(list_)<=9:
#     n +=1
#     list_.append(n)
#     print(list_)

#     if n%2!=0:
#         list_.pop()
#         print(list_)

#         list_.append(0)
#         print(list_)


# print(list_)
######  замена элементов и очистка списка
# list_ = [1,2,3]
# list_[0] = '1'
# print(list_)
# list_.pop(0)
# list_.insert(0,'1')
# print(list_)
# list_.insert(0,'1')
# print(list_)

# #------------------очистка--------------------#
# #list_ = []
# list_.clear()
# print(list_)

#-------------------------Задание---------------------------#
# """ 
# Поменять местами наибольший и наименьший элементы списка( только содержит целые)

# """
# listNum = [2, 1, 4, 5, 3]

# maxNum = max(listNum)# находим само число макс
# maxInd = listNum.index(maxNum) # находим индекс макс числа
# print(maxNum, maxInd)

# minNum = min(listNum)
# minInd = listNum.index(minNum)
# print(minNum, minInd)

# #----------------------#
# # listNum.pop(minInd)
# # listNum.insert(minInd, maxNum)

# # listNum.pop(maxInd)
# # listNum.insert(maxInd, minNum)
# #----------------------#
# listNum[minInd], listNum[maxInd] = maxNum, minNum

# #----------------------#
# # a = 5
# # b = 1
# # a, b = b, a
# # print(a,b)
# #----------------------#

# print(listNum)


#-------------------------Задание---------------------------#
#-------------------Угадай число-------------------------#
# Показать кол-во сделанных попыток и их значения
# Показать  сделанные попытки в случае, если пользователь уже ввел такое число
# показать кол-во сделанных Уникальных попыток и их значения

#сделаем рандомное число
import random #подключаем модуль - файл, в котором написаны функции
# каждый модуль увеличивает вес вашей программы

attempts = [] #попытки пользователя
computer_number = 55#random.randint(1, 100) # randint(start, end) -включительно
while True:# старт Игры точка входа
    n = int(input('введите число от 1 до 100 '))
    attempts.append(n)
    if attempts.count(n) >= 2:
        print('ваши попытки', attempts)

    if n == computer_number:
        print('Победа')
        print('ваши попытки', attempts, 'кол-во', len(attempts))
        print('ваши уникальные попытки', set(attempts), 'кол-во', len(set(attempts)))

        break # Точка выхода
#конец игры



    
#--------------Задание---------------------#
""" 
Дан список, только целых чисел. 
Сформировать новый список или преобразовать текущий,
в котором идут сначала отрицательные элементы, затем нули, 
затем положительные. 
БЕЗ СОРТИРОВКИ итогового списка
"""
# [-3, -1, 2, 2, 0, 5, 1, -5] ->
# -> [-3, -1, -5, 0, 2, 2, 5, 1]
list_1 = [-3, -1, 2, 2, 0, 5, 1, -5]
list_2 = []

for i in list_1:
  if i < 0:
    list_2.append(i)
for i in list_1:
  if i == 0:
    list_2.append(i)
for i in list_1:
  if i > 0:
    list_2.append(i)

print(list_2)

#-------- 2 способ ----------#
ist_ = [2, -1, 0, 1, -2]
list1 = []
list2 = []
list_zero = []
list_end = []
for i in ist_:
    if i > 0:
        list1.append(i)
    elif i == 0:
        list_zero.append(i)
    elif i < 0:
        list2.append(i)
list_end.extend(list2)
list_end.extend(list_zero)
list_end.extend(list1)

print(list_end)