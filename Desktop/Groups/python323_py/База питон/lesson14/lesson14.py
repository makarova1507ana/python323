# #----------------Задание----------------------#
# """
# Дан текстовый файл.
# создать список, в котором будут выписаны все цифры из этого файла, с повторениями и без.
# это 1 сентября.  2 год в этой школе. на линейке я стоял на 1 месте. 
# [1,2,1]
# """
# def num_list():
#     list_ = []
#     with open(r'C:\Users\Anastasia\Desktop\sometext.txt', 'r') as f:
#         for s in f:# перебираем строки
#             for el in s: # перебирает символ
#                 if el.isdigit():
#                     list_.append(el)
#     return list_

# print(num_list())


# #----------------Задание----------------------#
# """
# Дан текстовый файл.
# создать список, в котором будут выписаны все цифры из этого файла, с повторениями и без.
# это 1 сентября.  2 год в этой школе. на линейке я стоял на 1 месте. 
# [1,2,1]
# """
# def num_list():
#     list_ = []
#     with open(r'C:\Users\Anastasia\Desktop\sometext.txt', 'r') as f:
#         for s in f:# перебираем строки
#             for el in s: # перебирает символ
#                 if el.isdigit():
#                     list_.append(el)
#     return list_

# print(num_list())

# #----------------Кодировка----------------------#
# """
# Кодировка - какой-то набор чисел (в какой-то системе счисления) будет означать символ
# https://wiki.iarduino.ru/page/encoding-arduino/ здесь кесть таблица кодировки

# """
# for i in range(128):
#     print(i,chr(i))
# bukv = ['A','a','Z','E']
# bukv.sort()
# print(bukv)
for encode in 'utf-8', 'CP866	', 'cp1251', 'utf-16':
    with open('encode.txt', 'r', encoding=encode) as f:
        s= f.read()
        print(f.read())



#----------------Задание----------------------#
"""
Дан текстовый файл.
Записать все слова из исходного файла в файл words.txt.
Слово - набор букв, отдельнные пробелом, или кавычками, или точкой только справой стороны, а также запятой.
"""
#1 получить набор строк
correctwords=[]
with open('sometext.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    words = text.split() # список строк без пробелов
    #print(words)
    for word in words:
        isword = 'это слово' #True
        for element in word:
            if not(element.isalpha()) and element!='.' and element!=',':
                isword = 'это не слово'#False
                break
        if isword=='это слово':
            correctwords.append(word)
            
#print(correctwords)   
            
                
    #text = f.readlines()#['это 1 сентября. \n', '2 год в этой школе. на линейке я стоял на 1 месте. ']
    #s=''.join(text)#'это 1 сентября. \n2 год в этой школе. на линейке я стоял на 1 месте. '
    #s='*'.join(text)#'это 1 сентября. \n*2 год в этой школе. на линейке я стоял на 1 месте. '
    #print(s) 
    

            
            
                
    #text = f.readlines()#['это 1 сентября. \n', '2 год в этой школе. на линейке я стоял на 1 месте. ']
    #s=''.join(text)#'это 1 сентября. \n2 год в этой школе. на линейке я стоял на 1 месте. '
    #s='*'.join(text)#'это 1 сентября. \n*2 год в этой школе. на линейке я стоял на 1 месте. '
    #print(s) 
