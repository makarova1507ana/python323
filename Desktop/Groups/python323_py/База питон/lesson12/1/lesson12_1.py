# file = open('text4.txt','r')
# print(type(file))
# # # file_text = file.read() 
# # # print(file_text)
# # line = file.readline() 
# # print(line)
# # for line in file: # если нужно прочитать по строкам
# #     print(line)

# lines = file.readlines() # список строк
# print(lines)
# file.close()

#-------------------исключения------------------------#

try:
    file = open('text4.txt','r')
    lines = file.readlines() # список строк
    print(lines)
except FileNotFoundError:
    print("file is not found")
except:
    print("Something else went wrong")
finally:
    file.close()



#------------------21 слайд-------------#