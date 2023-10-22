#--------------------------------Задача-------------------------------------#
# Запрещено: использовать map,sort,min,max, count
# Определить, содержит ли списке данное число x

#-------------1 способ---------------#
# l = [1, 3, 6] #
# num = 3
# for el in l:
#     if el == num:
#         print(f"{num} есть in {l}")
#         break

# #-------------2 способ---------------#
# l = [1, 3, 6] #
# num = 3
# print(num in l)

# # #-------------3 способ---------------#
# l = [1, 3, 6] #
# num = 3
# if l.count(num):
#     print(f"{num} есть in {l}")
# else:
#     print(f"{num} нет in {l}")



#--------------------------------Задача-------------------------------------#
# Запрещено: использовать map,sort,min,max, count
# Найти количество чисел в массиве, которые делятся на 3, но не делятся на 7.

# [1, 3, 9]  count = 2
# l = [1, 3, 6] # [1, 3, 6]  count = 1     |     [1, 3, 21] count = 1    |[1, 63, 21] count = 0\\
# count = 0
# counter = 0
#
# for x in l:
#     if x % 3 == 0 and x % 7 != 0:
#         counter += 1
#
# if counter != 0:
#     print(f"counter = {counter}")
# else:
#     print("NO")




#--------------------------------Задача-------------------------------------#
# Найти второй максимум в списке чисел, исходный список менять нельзя
# #-------------1 способ---------------#
# l = [1]
# if len(l) >= 2:
#     print(max(l))
#     new_l = l.copy()
#     new_l.remove(max(new_l))
#     print(f"исходный список = {l}")
#     print(f"второй максимум = {max(new_l)}")
# elif len(l) == 1:
#     print(f"единственный максимум = {max(l)}")
# else:
#     print("нечего вычислять")


# # #-------------2 способ---------------#
# l = [1, 5, 4]
# if len(l) >= 2:
#     new_l = l.copy()
#     new_l.sort()
#     print(f"исходный список = {l}")
#     print(f"второй максимум = {new_l[-2]}")
# elif len(l) == 1:
#     print(f"единственный максимум = {max(l)}")
# else:
#     print("нечего вычислять")


# #--------------------------------Задача-------------------------------------#
# # отсортировать список в порядке уменьшения значений
#
# l = [1, 28, 8, 3, -4]
# l.sort(reverse=True)
# print(l)

# l = [1, 28, 8, 3, -4]
# l.sort()
# l.reverse()
# print(l)


# l = [1, 26, 13, 4324, 5, 4]
# new_l = l[::-1]
# print(f"исходный список = {new_l}")

# #--------------------------Срезы-------------------------------------- #
# l = [1, 26, 13, 4324, 5, 4]
# print(l[0:2]) # l[start:end (Не включается)]
# print(l[2:4]) # l[start:end (Не включается)]
# print(l[2: ]) # l[start:end (если нет, то до конца)]
# print(l[:4]) # l[start (если нет, то сначала) :end (Не включается)]
# print(l[:])# от начала и до конца
# print(l[::2])# l[start: end: step]
# print( l[::-1])# l[start: end: step]







#--------------------------------Многомерные коллекции-------------------------------------#
# [[],[],[]] - матрица
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print(matrix) #matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0]) # matrix[i] - показать строку
# print(matrix[0][0]) # matrix[i][j] - показать строку элемент строки


# users = [["user1", " password1"],
#           ["user2", " password2"],
#           ["user3", " password3"]]
# print(users)
#
#
# list_products = ["product1",
#                  "product2",
#                  "product3"]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# # обход строк
# # for row in matrix:
# #     print(row)
# # print("\n********************************************\n")
# # for row_i in range(len(matrix)):
# #     print(matrix[row_i])
#
# # # обход элементов внутри строк
# # for row in matrix:
# #     print()# разделитель новой строки
# #     for element in row:
# #         print(element, end=' ')
# #
# # print("\n********************************************\n")
# # for row_i in range(len(matrix)):
# #     print()  # разделитель новой строки
# #     for column_i in range(len(matrix[row_i])):
# #         print(matrix[row_i][column_i], end=' ')
#
# # обход столбцов
# # for j in range(len(matrix)):
# #     print("************ new column *********\n")
# #     for row in matrix:
# #         print(row[j])
#
# # print("\n********************************************\n")
#
# # count_rows = len(matrix)
# # count_columns = len(matrix[0])
# #
# # for column_i in range(count_columns):
# #     print("************ new column *********\n")
# #     for row_i in range(count_rows):
# #         print(matrix[row_i][column_i])
#
# # обход диагоналей
# # Решите дома самостоятельно
#
#
#
# # list_passwords = ["password1",
# #                   "password2",
# #                  "password3"]
#
# # for row in list_passwords:
# #     print("new password symbols \n")
# #     for symbol in row:
# #         print(symbol)
#
#
# # ----------------------- еще про коллекции ------------------------------------------- #
# # # тип данных в пайтоне
# # #     * list - список
# # #     * tuple - кортеж
# # #     * set -  множества
# # #     * dictionary - словарь
#
# # -------------------- кортеж ------------------------------ #
# # *tuple - кортеж
# # нельзя изменить, операции удаление, добавлению и редактированию - недоступны
# # tuple_ = (1, 5, 3)
# # tuple_[0] = 3 # TypeError: 'tuple' object does not support item assignment
# # print(tuple_[0])
# # tuple_ = (2, 3, 4)
# # print(tuple_[0])
#
# # На подумать
# tuple_ = ([1, 2], 3, 4)
# print(tuple_[0])
# tuple_[0][0] = '*'
# tuple_[0].append( '*')
# print(tuple_[0])


# # # -------------------- множества ------------------------------ #
# # #      * set -  множества
# #
# # # хранит только уникальные значение
# # # #  операции удаление, добавлению и редактированию - доступны
# # недопустна операция по обращение к индексу
# #
# set_ = {1, 2, 3, 3}
# set_.add(('1', 1)) # можно добавить приминитивные типы или кортеж
# print(set_)
# #[print(element) for element in set_] #доступ к элемент
# for element in set_:
#     print(element)
#

# # Удалить дупликаты (одинаковые значения)
# list_ = [1, 1, 1, 2, 2, 1, 3, 4]
# print(set(list_))



#  -------------------- словарь ------------------------------ #
#      * dictionary - словарь - ассоциативный массив
# ключ(ДОЛЖЕН быть уникальным): значение
dictionary = {"one": 1, "two": 2} # ключ: значение

