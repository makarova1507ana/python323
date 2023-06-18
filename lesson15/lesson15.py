#----------------------------OS------------------------------------#
import os

# # получение текущий директория (путь файла)
# print('текущая директория', os.getcwd())
# #print(os.path)

# # создание каталог (папки)
# if not os.path.isdir('folder'): # есть папка == True
#     os.mkdir("folder")
    
# #перемещение  текущей директории

# os.chdir('..\\JS')#..\\выход из текущей папки
# print('текущая директория', os.getcwd())
# with open('text.txt', 'w') as f:
#     f.write('hi')

# os.chdir('..\\PYTHON 223 ПИТОН\\folder')#..\\выход из текущей папки
# #переименования файла
# if  os.path.isdir('text.txt'): # есть файл == True
#     os.rename('text.txt','newtext.txt')

# #os.chdir('..\\')
# #переименования файла
# #os.rename('folder','  newfolder')

# #os.rename('PYTHON 223 ПИТОН','  python323_py') # не раотает так как открыта папка
# #переименования файла
# os.mkdir('lesson1')
# os.replace('lesson1.py','lesson1/lesson1.py')


#список папок
#print(os.listdir())

#удаление
#os.remove('text1.txt')
#удаление папки
#os.rmdir('folder')


#-------------------------------Задание--------------------------------------------#

"""
Дан файл companies.txt
Создать папки с соответствующими именами компаний

"""

import os
print(os.getcwd())
#os.mkdir('files_txt')
f = open('files_txt/companies.txt','w')
f.write('compan1')
f.close()
with open('files_txt/companies.txt','r') as f:
  company_names = f.readlines()
  #print(company_names)
  for name in company_names:
    if not os.path.isdir(name):
      os.mkdir(name)# создаем папку 