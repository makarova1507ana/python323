# инкапсулция - скрытие чего-либо, но и  организация логику доступа и изменения
# полиморфизм - назначение новой возможности или новой реализации или способ вызова уже существующему действию 
# наследование - это способ расширения(улучшение) одного класса другим классом.

class Fruit:# класс - родитель или предок
    def __init__(self, name:str=''):#полиморфизм перегрузка оператора =
        self.__name = name # инкапсулция
    
    @property
    def name(self):
        return self.__name
    
    def __eq__(self, other):#полиморфизм перегрузка оператора == 
        return self.name == other.name

class Apple(Fruit):#наследование # класс - потомок
    def heal(self):
        print(self.name + ' heal ++')
    
# name_fruit = input('your favourite fruit')
# fruit = Fruit(name_fruit)
# fruit2 = Fruit('orange')
# fruit3 = Fruit('banana')
# apple = Apple('apple')
# apple.heal()

# if fruit == fruit3:
#     print(' equals')













#-----------------------------------------ЗАДАНИЕ-----------------------------------------------------------#
# Создать класс стул (умеет стоять). Создать класс наследник стул на колесиках (умеет стоять и ездить)


class Chair:
        
    def __init__(self, name: str = ''):
        self.__name = name
        self.__stand = 'stand'
        
    @property
    def name(self):
        return self.__name
    
    @property
    def stand(self):
        return self.__stand
   

class Chair1(Chair):
    
    def __init__(self, name:str='', height:str=0):# переопредили родительский метод __init__()
        super().__init__(name)    # обращение к родительскому классу
        self.__height = height
        
    @property
    def height(self):
        return self.__height
    
    def go(self):
        print('Умеет:',self.stand + 'ездить' )

 
# #Class()-> __new__() ->__init__()
# chair = Chair('chair old')

# chair1 = Chair1('chair new',100)
# print(chair1.height)

# chair1.go()


class My_Class(object):
    def __new__(cls):# конструктор -> создание объекта выделяется место
        print("Python is great!")
        return super(My_Class, cls).__new__(cls)
    
    def __init__(self):# инициализатор ->  к объектам присваевается значения
        print("Finxter42")
        
My_Class()# создаем объект