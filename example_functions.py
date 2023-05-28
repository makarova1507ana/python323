""" 
Задание 

треугольник 
3 стороны 
написать функцию, которая  возвращает площадь этого треугольника 
triangle_s(a,b,c, type_t='прямоугольный')
"""

def geron(a,b,c):
    # вычисляем полупериметр треугольника p
    p = (a + b + c) / 2
    # вычисляем площадь треугольника по формуле Герона
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def right_triangle_s(a, b):
    return a*b*0.5


def is_right_triangle(a, b, c):
    if (b ** 2 + c ** 2) == a ** 2:
        return True
    elif (a ** 2 + c ** 2) == b ** 2:
        return True 
    elif (a ** 2 + b ** 2) == c ** 2:
        return True 
    return False

def check_type(a, b, c):
    # определяем тип треугольника
    if a == b == c:
        triangle_type = 'равносторонний'

    elif is_right_triangle(a, b, c):
        triangle_type = 'прямоугольный'

    else:
        triangle_type = 'разносторонний'

    return triangle_type

def triangle_s(a,b,c, type_t='прямоугольный'):
    type_t = check_type(a,b,c)
    if type_t == 'прямоугольный':
        if a<c>b:
            s = right_triangle_s(a,b)
        elif a<b>c:
            s = right_triangle_s(a,c)
        elif c<a>b:
            s = right_triangle_s(c,b)
    else:
        s = geron(a,b,c)

    return s

a = int(input('Введите первую сторону'))
b = int(input('Введите вторую сторону'))
c = int(input('Введите третью сторону'))

type_t = input('Введите тип треугольника')

triangle_s(a,b,c)
