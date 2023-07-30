class My_Class(object):
    def __new__(cls):# конструктор -> создание объекта выделяется место
        print("Python is great!")
        return super(My_Class, cls).__new__(cls)
    
    def __init__(self):# инициализатор ->  к объектам присваевается значения
        self.a1 = 0
        self.a2 = 0
        print("Finxter42")
        
# my_cls =My_Class()# создаем объект
# print (my_cls)
# print(type(5))

# class Vector(list):
#     def __init__(self,l,direct=0):
#         self.d = direct
#         self.l = l
    
#     def __str__(self):
#         return ' '.join(self.l)
# l1 = ['1','2','3']
# print(l1)
# l = Vector(['1','2','3'])
# print(l)   




class Fruit:# класс - родитель или предок
    def __init__(self, name:str='', color:str='red', size:int=1):#полиморфизм перегрузка оператора =
        print('Fruit__init()__')
        self.__name = name # инкапсулция
        self.color = color
        self.size  = size
        
    @property
    def name(self):
        return self.__name

    def __eq__(self, other):#полиморфизм перегрузка оператора == 
        return self.name == other.name 

class Apple(Fruit):#наследование # класс - потомок
    def __init__(self, name:str='', size:int=1):# переопределили у родителя overwriting
        super().__init__(name=name,  size=size)#обращение к родителю
        print('Apple__init()__')
        self.__power_healf = 5 #сила лечения
        
    def heal(self):
        print(self.name + ' heal ++')

    def __str__(self):
        return f'this is {self.name}, my color {self.color}, my size {self.size} and {self.__power_healf}'

# apple = Apple('Gold apple', size=5)
# print(apple)



# def f(name:str='', color:str='red', size:int=1):
#     print(name, color, size)
# f()
# f(size=5, name='Name')



"""
1 step
Создать  класс Figure с методами вычисления площади и периметра, 
а также методом, выводящим информацию о фигуре на экран. 

2 step
Создать производные классы:
Rectangle (прямоугольник), Circle (круг), Triangle (треугольник) со своими методами
вычисления площади и периметра.

3 step
Создать список n фигур и вывести полную информацию 
о фигурах на экран.
"""

#----------------------------------------------------------------------------#

# 1 step
# Создать  класс Figure с методами 
# 1.1 вычисления площади 
# 1.2 и периметра, 
# 1.3 а также методом, выводящим информацию о фигуре на экран. 
class Figure:
  
    def get_S(self):
        return -1 #Площадь должна быть определена в потомках
    
    def get_P(self, *sides):
        P = 0
        for side in sides:
            P += side
        return P
    
    def __str__(self):# self- обращение к конкретному объекту
        return f'P = {self.get_P()} and S = {self.get_S()}'
  
# 2 step
# Создать производные классы:
# 2.1 Rectangle (прямоугольник), 
# 2.2 Circle (круг), 
# 2.3 Triangle (треугольник) 
# со своими методами вычисления площади и периметра.

class Rectangle(Figure):
    def __init__(self, a:int=1, b:int=1):
        super().__init__()
        if a <= 0 or b <= 0: raise "side below zero"
        self.__a = a
        self.__b = b
        self.__P = super().get_P(a, b, a, b) # обращаемся к родительскому методу 
        self.__S = self.get_S()# обращаемся к методу Rectangle
    
    def get_S(self):# перезаписали - полиморфизм
        return self.__a * self.__b
    
    def get_P(self):# перезаписали - полиморфизм
        return self.__P

class Circle(Figure):
    __pi = 3.14
    def __init__(self, r:int=1): 
        self.__r = r
        self.__P = self.get_P() # обращаемся к методу Circle
        self.__S = self.get_S()# обращаемся к методу Circle
    
    def get_P(self):# p - длина окружности
        return 2*self.__pi*self.__r
    
    def get_S(self):
        return self.__pi*self.__r**2
    
class Triangle(Figure):
    def __init__(self, a:int=1, b:int=1, c:int=1):
        super().__init__()
        if a <= 0 or b <= 0: raise "side below zero"
        self.__a = a
        self.__b = b
        self.__c = c
        self.__P = super().get_P(a, b, c) # обращаемся к родительскому методу 
        self.__S = self.get_S()# обращаемся к методу Triangle
        
    def get_S(self):# перезаписали - полиморфизм
        a = self.__a 
        b = self.__b 
        c = self.__c
        p = self.__P/2
        self.__S =(p*(p-a)*(p-b)*(p-c))**0.5
        return self.__S
    
    def get_P(self):# перезаписали - полиморфизм
        return self.__P
    
rect = Rectangle(5, 4)
print(rect)  
circle = Circle(5)
print(circle)  
    
    