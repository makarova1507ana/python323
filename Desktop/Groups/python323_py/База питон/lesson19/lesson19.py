# ------------------------------Локальные и глобальные---------------------------------#

# # n=1
# # print(n)

# # #--------------тоже самое (мы этого не видим)-----------------#
# # def main():
# #     n=1
# #     print(n)

# a = 4#сюда ссылаемся

# def f():
#     n = 2 # локальная переменная распротраняется только на функцию
#     global a # глобальная переменная

#     l = 3# локальная
#     a = 3 # глобальная переменная
#     print('f()=',n)

# n = 1 # локальная - радиус обзора больше переменная
# print(a)
# print(n)
# f()
# print(n)
# print(a)
# #print(l)# локальная поэтому ошибка
# ------------------------------Локальные и глобальные---------------------------------#


#-----------------------Регулярное-------------------------#
# 
# [A-z0-9,А-я ]{0,}\.[A-z]{0,} - шаблон
#"С:\\folder1\\folder\\file.txt"    

# "С:\folder1\folder\file.txt"

# \f.txt//подходит
# \File.png//подходит
# \fi3le.exe//подходит
# \fil,  f.gg //подходит
# \file,txt // исключить, потому что опечатка
# \fil*e.json/// исключить, потому что опечатка
# \fileфtxt // исключить, потому что не файл
# file@txt // исключить, потому что опечатка

# . - любой символ
# \ - экранирование 
# \. - ищем точку
# [] -  допустимый символ
# [A-z] - вся латиница  - [a-zA-Z]
# [A-z0-9,А-я] - поиск одного символа
# {} - указывают кол-во повторения (сколько раз допустимый может встретиться )
# {start, end} - 
# [A-z0-9,А-я]{0,}\. - допустимый символ до точки любое кол-во раз и даже 0

# [A-z0-9,А-я ]{0,}\.[A-z]{0,}




# регулярные выражения
import re #импортируем модуль regular expresion -re

# s = """ёжик. Эти события произошли в 2021 году. 2021 год был особенный! 
# в нем было 20212021 шт необычных вещей. Правда?"""#тестовая строка
# reg = '[0-9]' #наше регулярное выражени / наш шаблон
# list_s = re.findall(reg, s) #находим все совпадения по шамблону рег. выражений
# print(list_s)
"""
# print(re.search(reg, s))# находит первое совпадения по шамблону  с развернутым анализом (специальный тип данных)
# print(re.search(reg, s).span())# возвращает номера занимаемого первогосовпадения
# print(re.search(reg, s).start())# находит начальный номер первого совпадения по шамблону
# print(re.search(reg, s).end())# находит конечный номер первого совпадения по шамблону
# print(re.search(reg, s).group())# находит первое совпадения по шамблону
"""

#reg = '(\.|\!|\?)'# либо '.'  либо '!' либо '?'
#print(re.split(reg, s))#разделение строки по предложениям
#reg = r'\.'# r - позволяет игнорировать дополнительного экранирование спец сиволов в строке
# snew=re.sub(reg, "*", s)# поиск и замена по шаблону (последняя цифра необязательна, указывает сколько должно быть замен)
# print(snew)
# reg = r'[А-яё]'#необходимо указывать явно букву "ё"
# print(re.findall(reg, s))










#---------------------------ООП---------------------------------#
