

# def number_encryption(s):
    
#     for j, line in enumerate(s):

       

       
#                 if world[i] == '1':

#                     worlds[el] = world.replace('1', '!')
                    

#                 elif world[i] == '2':

#                     worlds[el] = world.replace('2', '@')

#                 elif world[i] == '3':

#                     worlds[el] = world.replace('3', '#')

#                 elif world[i] == '0':

#                     worlds[el] = world.replace('0', '(')

#                 elif world[i] == '4':

#                     worlds[el] = world.replace('4', '$')
#             #worlds[el] = world
#             res=''
#             for world in worlds:
#                 res = res.join(world)
#                 res = res+' '
#             s[j] = res
#        # print(s)
    

       

#     return s

# # with open('text2.txt','r+', encoding='utf-8') as f:

#     # s = f.readlines()

#     # print(type(s),s)
# s=['f ff 12 1f','fdsdd ddd','1111']
# #number_encryption(s)
# print(number_encryption(s))


# # s = '1234'
# # print(s[0])
# # s[0]=s.replace('1','!')

num = '123'#input("Введите ваш номер автомобиля: ")

# with open("fff.txt",'r' ) as f:

    #file = f.readlines()#['123','sss','11']
file = 'fffff 123 11'#['123','sss','11']''

if num  in file:

    print(num,"Ваш номер есть в списке")

else:

    print("нет такого номера")