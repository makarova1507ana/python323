# from random import randint as r

# b =list(filter(lambda x: x % 2==0, [r(1, 100) for i in range(100)]))
# #print(b)
# def make_list(n):
#     l=[]
#     for i in range(n):
#         l.append(r(1,100))
#     return l

# for n in make_list(10):  
#         print(n)





import os
import random as r
import func
print(os.getcwd())
os.chdir('lesson16')


    
with open('users.txt', 'r+') as f:
    users = f.readlines()

for name in users:
    if not os.path.isdir(name[:len(name) - 1]):
        os.mkdir(name[:len(name) - 1])
    #lambda x: os.mkdir(name[:len(name) - 1]) if (not os.path.isdir(name[:len(name) - 1])) else False
    func.create_file(name,name_file='login')# password не передаю 

    for n in range(len(users)):
        password = func.create_pass(8)
        func.create_file(name,name_file='password',password=password)
        
#-----------------------Удаление папок с user------------------------------#
name = users[1][:len(users[0]) - 1]
if os.path.isdir(name):
    os.chdir(name)
    files=os.listdir()
    for file in files:   
        os.remove(file)
    os.chdir('../')
    os.rmdir(name)
    
#-----------------------регулярные выражения------------------------------#
""" шаблон для поиска чего-либо в сторке
"""
# регулярные выражения
import re #импортируем модуль
# пример шаблон длчя поиска чисел -?[0-9]+[\n, .]

s = "ёжик. Эти события произошли в 2021 году. 2021 год был особенный! в нем было 20212021 шт необычных вещей. Правда?" #тестовая строка
#reg = '2021' #наше регулярное выражени
#list_s = re.findall(reg, s) #находим все совпадения по шамблону рег. выражений
#print(list_s)
"""
print(re.search(reg, s))# находит первое совпадения по шамблону  с развернутым анализом
print(re.search(reg, s).span())# возвращает номера занимаемого первогосовпадения
print(re.search(reg, s).start())# находит начальный номер первого совпадения по шамблону
print(re.search(reg, s).end())# находит конечный номер первого совпадения по шамблону
print(re.search(reg, s).group())# находит первое совпадения по шамблону
"""
#reg = '(\.|\!|\?)'# либо '.'  либо '!' либо '?'
#print(re.split(reg, s))#разделение строки по предложениям
#reg = r'\.'# r - позволяет игнорировать дополнительного экранирование спец сиволов в строке
#print(re.sub(reg, "!", s, 1))# поиск и замена по шаблону (последняя цифра необязательна, указывает сколько должно быть замен)
reg = r'[А-яё]'#необходимо указывать явно букву "ё"
print(re.findall(reg, s))