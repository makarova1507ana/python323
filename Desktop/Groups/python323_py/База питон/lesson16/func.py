import os
import random as r
def create_file(name:str, name_file:str, password=''):
    file = open(name_file+'.txt', 'w')
    if password=='':
        file.write(f'login: {name[:3]+str(r.randint(1,1000))}' )
    else:
        file.write(password)
    file.close()
    os.replace(name_file+'.txt', f'{name[:len(name) - 1]}/'+name_file+'.txt')
    
def create_pass(n):
    symbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = n
    password=''
    for i in range(length):
        password += r.choice(symbols)
    return password