""" 
Задание 

треугольник 
3 стороны 
написать функцию, которая  возвращает площадь этого треугольника 
triangle_s(a,b,c, type_t='прямоугольный')
"""

# """
# Функция triangle_properties вычисляет площадь треугольника
# по формуле Герона и определяет его тип в зависимости от длин
# его сторон.

# :param a: длина первой стороны треугольника
# :param b: длина второй стороны треугольника
# :param c: длина третьей стороны треугольника
# :return: кортеж, содержащий площадь треугольника и его тип
# """
# def triangle_properties(a, b, c):
  
#     # вычисляем полупериметр треугольника p
#     p = (a + b + c) / 2

#     # вычисляем площадь треугольника по формуле Герона
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

#     # определяем тип треугольника
#     if a == b == c:
#         triangle_type = 'равносторонний'
#     elif a == b or a == c or b == c:
#         triangle_type = 'равнобедренный'
#     else:
#         triangle_type = 'разносторонний'

#     # возвращаем кортеж, содержащий площадь и тип треугольника
#     return area, triangle_type

# a = 3
# b = 4
# c = 5

# area, triangle_type = triangle_properties(a, b, c)



# def geron(a,b,c):
#     # вычисляем полупериметр треугольника p
#     p = (a + b + c) / 2
#     # вычисляем площадь треугольника по формуле Герона
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5

# def right_triangle_s(a, b):
#     return a*b*0.5
    

# def is_right_triangle(a, b, c):
#     if (b ** 2 + c ** 2) == a ** 2:
#         return True
#     elif (a ** 2 + c ** 2) == b ** 2:
#         return True 
#     elif (a ** 2 + b ** 2) == c ** 2:
#         return True 
#     return False

# def check_type(a, b, c):
#     # определяем тип треугольника
#     if a == b == c:
#         triangle_type = 'равносторонний'
    
#     elif is_right_triangle(a, b, c):
#         triangle_type = 'прямоугольный'

#     else:
#         triangle_type = 'разносторонний'
    
#     return triangle_type

# def triangle_s(a,b,c, type_t='прямоугольный'):
#     type_t = check_type(a,b,c)
#     if type_t == 'прямоугольный':
#         if a<c>b:
#             s = right_triangle_s(a,b)
#         elif a<b>c:
#             s = right_triangle_s(a,c)
#         elif c<a>b:
#             s = right_triangle_s(c,b)
#     else:
#         s = geron(a,b,c)
    
#     return s
        
# a = int(input('Введите первую сторону'))
# b = int(input('Введите вторую сторону'))
# c = int(input('Введите третью сторону'))

# type_t = input('Введите тип треугольника')

# triangle_s(a,b,c)

























#--------------------------с произвольным кол-во параметров------------------------------------------#
""" 
реализуем функцию sum_nums(*nums) возвращает сумму чисел
"""
# def sum_nums(*nums): # nums - кортеж ()
#     s = 0
#     for num in nums:
#         s += num
#     return s
# print(sum_nums(1,78,2,3))





""" 
реализуем функцию f(*nums) возвращает степени чисел

пример
f(3,8,24) -> (3**8)**24
"""

# def func_(*sm):
#   s = sm[0]
#   for i in sm[1:]:
#     s **= i
#   return s

# print(func_(4, 6,7))




# l = [4,9,6,0] 
# print(l)#[4, 9, 6, 0]

# print(l[2:])#[6, 0]

# print(l[:2])#[4, 9]

# print(l[2:4])#[6, 0]

# print(l[1::2])#[9, 0]

# s  = 'Привет'
# print(s[1::2])#'рвт'



#----------------------- Рекурсия ----------------------------#


def f(n):# суммируем значения от n до нуля
    if n == 0:
        return 0
    return f(n-1)+n 

print(f(2))



