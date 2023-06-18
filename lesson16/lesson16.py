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