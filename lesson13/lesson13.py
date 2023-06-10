#-------------------исключения------------------------#

# try:
#     file = open('text4.txt','r')
#     lines = file.readlines() # список строк
#     print(lines)
# except FileNotFoundError:
#     print("file is not found")
# except:
#     print("Something else went wrong")
# finally:
#     file.close()
    
 
#-------------------raise------------------------#
# x = ''    
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")



#---------------------ЧТЕНИЕ и ЗАПИСь---------------------#
# f = open('text.txt','r+')#а также w+
# f.write('abcd')

# f.seek(1)#seek перенос на необходимый индекс 
# s = f.readline()
# print(s)
# f.close() #!обязательно!



# #---------------------with---------------------#
# with open('text.txt','r') as f:
#     s = f.readline()
#     print(s)
    
#----------------------------------------------#
""" 
Текстовый файл состоит не более чем из 10^6 символов L, D и R. Определите максимальную длину цепочки вида LDRLDRLDRL... 
(составленной из фрагментов LDR, последний фрагмент может быть неполным).
"""


# with open('zadanie24_2.txt','r') as f:
#     s = f.read()#получили строку из файла
#     #s="LDRLDRLDRLDDLDLDRL"
#     # LDRLDR - 1
#     # LDRLD - 1
#     # LDRL - 1
#     # LDRLDLDR - 2 разные LDRLD  LDR 
#     # ****LD******DDD***L
#     s = s.replace('LDR','*') # *LDD , учитывать LD   *LRD ,
#    # s = s.replace('*LD','#') # *- 3+ 2 = 5
#     #s = s.replace('*L','!')# 3+1 = 4
#     #print(s)
#     counter = 0
#     max_count = 0
#     for i in range(len(s)):
#         if s[i]=='*':
#             counter+=3
#         #elif s[i-1]=="*" and s[i]=='#':
#        #     counter+=5
#        # elif s[i-1]=='*' and s[i]=='!':
#        #     counter+=4
#         else:
#             if s[i]=='L':
#                 counter+=1
#                 if s[i+1]=='D':
#                     counter+=1
                    
#             if max_count<counter:
#                 max_count = counter
#             counter=0
                
#     if max_count<counter:
#         max_count = counter  
#     print(max_count)
            

#-----------------Задание-----------------------------#
""" 
Текстовый файл, на каждой строке которого записаны пароли.
Пароль должен состоят как минимум из одной заглавной буквы(буквы любые) и как минимум одной цифры.
В пароле не должно быть пробелов, табуляции(\t), все остальные остальные символы допустимы

Подходят

Pfe3
Zfdf32
14mkM
Я5

Не подходят
&lkYh-GTF4;\t456Fd!
ffffF
1234

"""
with open('passwords.txt','r') as f:
    # passwords = f.readlines() #['Pfe3\n', 'Zfdf32\n', '14mkM\n', 'Я5\n', '&lkYh-GTF4;\\t456Fd!\n', 'ffffF\n', '1234']
    # print(passwords)
    passwords = f.read().split('\n') # read -> passwords - строка ['Pfe3', 'Zfdf32', '14mkM', 'Я5', '&lkYh-GTF4;\\t456Fd!', 'ffffF', '1234']
    print(passwords)
    right_passwords = []
    
    for password in passwords:       
        isUpper = False
        isDigit = False
        
        for el in password:
            if (' ' in password) or  (r'\t' in password): #В пароле не должно быть пробелов, табуляции(\t), все остальные остальные символы допустимы
                break
            #.isdigit() - проверяет строку на числовые значения
            #.isupper() - проверяет строку на заглавную букву
            # #Пароль должен состоят как минимум из одной заглавной буквы(буквы любые) и как минимум одной цифры.
            if el.isupper(): # el - один символ 
                #print(el, password)#pass #код не выдаст ошибки, но здесь нет никаких команд
                isUpper = True
            if el.isdigit():
                #print(el, password)# pass    
                isDigit = True
            if isDigit and isUpper: #оба условия True
                print(password)
                
            
            

                
    