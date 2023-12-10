"""
Класс Рейтинг (средняя оценка(передаем сюда кортеж с переменным кол-во оценок)) и метод вычилисть среднюю оценку
Реализовать возможность сравнивать два рейтинг (больше, меньше, равенство) 
Релизовать возможность находнить средний рейтинг для двух рейтингов (объекты)
""" 
class Rating:
    def __init__(self, *marks):# marks (5,3,4) | (2) | () 
        self.__mark = self.avarage_mark(marks)
        
    def avarage_mark(self, marks):
        s = 0
        for mark in marks:
            s += mark  
        return s/len(marks)
    
    @property
    def mark(self):
        return self.__mark
     
    def __gt__(self, other):
        return self.mark > other.mark # возвращается логическое значние
     
    def __add__(self,other):
        return self.mark + other.mark
    
    def __str__(self):
        return "avarage mark: " + str(self.__avarage_mark )

# rating = Rating(5,5,5,5)  
# print(rating > Rating(1,1,1) )
# print((rating + Rating(1,1,1)+Rating(2,2,2))/3 )













""" 
Абстрактный класс - 

множественное наследование и модификаторы доступа при наследовании point-> line -> rectangle
"""







#-------------------------------- Абстрактный класс - ----------------------------------------------------#
""" 
Абстрактный класс - базовый класс, который не предполагает создания экземпляров.
Класс родитель для других классов Свод неких правил методов
"""

# Cat(say my_name)-> Animal  Dog(say my_name) -> Animal
class Animal:# Абстрактный класс 
    
    def say(self):
        return "no sound for this animal"
    
    def show(self):
        return self.name
    
class Cat(Animal):#
    def __init__(self, name):
        self.__name = name    

    @property
    def name(self):
        return self.__name
    
    def say(self):# перезапись  и это пример полиморфизма
        return "Meow "+ self.name

class Wolf(Animal):
    pass

class Dog(Wolf):#
    def __init__(self, name):
        self.__name = name    
    @property
    def name(self):
        return self.__name
    def say(self):
        return "Gav "+ self.__name

class Fox(Animal):
    def __init__(self, name):
        self.__name = name  
    @property
    def name(self):
        return self.__name
class Bird(Animal):
    pass

# print(Cat("Barsik").show(),
# Dog("Rokki").show(),        
# Fox("fox").show())



#-------------------------------- множественное наследование -------------------------------------#
""" 
множественное наследование - наследование сразу от нескольких  классов

object -> Animal-> Wolf -> Dog (последовательное наследование)

"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Line:
    def draw(self):
        return "draw line"
        
class Rectangle(Line, Point):
    def create_Rect(self):
        for i in range(4):
            self.draw()
    

class Grind:
    def do_grain(self):
        return "grind coffee grain"
    
    def get_V(self):
        return "V = 100 gr"

class CoffeeMachine:
    def make_coffee(self):
        return "make cofee"
    
    def get_V(self):
        return "V = 50 ml"
    
class CoffeeMachine_and_Grin(CoffeeMachine, Grind ):
    def choose(self):
        choice = input("1 or 2")
        if choice == "1":
            print(self.do_grain())
        elif choice == "2":
            print(self.make_coffee())
        
            

# #CoffeeMachine_and_Grin().choose()
# print(CoffeeMachine_and_Grin().get_V())










#--------------------------------  модифакторы доступа -------------------------------------#
""" 
модифакторы доступа - это маркеры, которые указывают на уровень доступа к 
атрибутам класса

name - атрибут
public - открытый -> все атрибуты, методы доступны внутри класса и за его пределами класса 

_name - атрибут
protected - защищенный  -> все атрибуты, методы доступны внутри класса  к ним есть доступ,
а за его пределами класса - доступа нет, НО при наследовании эти атрибуты и методы будет доступны у 
класса-наследника

__name - атрибут
private - закрытый -> все атрибуты, методы доступны внутри класса  к ним есть доступ,
а за его пределами класса - доступа нет 

"""



class Human:
    def __init__(self):
        self.name = "NAME" # public
        self._age = 0 # protected
        self.__gender = "GENDER" # private
        
# human = Human()

# human.name = "Ivan"       
# print(human.name)

# human._age = 30   # НИКАК НЕ СПАСАСЕТ, но программист должен соблдать правила
# print(human._age)

# # human.__gender = "M"  #  self.__gender - не будет изменен    
# # print(human.__gender)

# #--------------- модуль
# # accessify - модуль
# # pip install accessify 
# # @private 


#--------------------------------  модифакторы доступа при наследовании -------------------------------------#
""" 

public - передаются дочерним классам
protected - передаются дочерним классам
private - не передаются дочерним классам

"""
class Human:
    def __init__(self):
        age = 0
        if not(self.__check_attribute(age)):
            raise "not int"
        
        self.name = "NAME" # public
        self._age = age # protected
        self.__gender = "GENDER" # private

    def _think(self):
        print( "think")
    
    def __check_attribute(self,age):
        return type(self._age) == int 
    
class Student(Human):
    def __str__(self):
        self._think()
        return self.name + str(self._age) #+ self.__gender - не можем обратиться потому что  private

# print(Student())
# Student._think()













#---------------------------------------Задание- ---------------------------#


""" 
Создать класс weapon (урон) и нанести урон
Создать потомка knife  и метод ближняя атака атака
Создать потомка Pistol  и метод дальняя атака
"""

class Weapon:
    __damage = 50
    
    def _do_damage(self):
        return self.__damage

class Knife(Weapon):
    def attack(self):
        return "attack knife - " + str(self._do_damage())
    
class Pistol(Weapon):
    def attack(self):
        return "attack pistol - " + str(self._do_damage())
    
    
#---------------------------------------Задание- ---------------------------#


""" 
Создать потомка  pistol_bayonet наследовать от knife и Pistol
Создать класс  Player (здоровье=100, инвентарь) для инвенторя реализовать геттер и сеттер
"""
class Pistol_bayonet(Knife, Pistol):
    def attack(self):
        choice = input("choose: ")#"knife"
        if choice == "knife":
            return Knife().attack()
        elif choice == "pistol":
            return Pistol().attack()
     
inventory = [Knife(), Pistol(), Pistol_bayonet() ]

for w in inventory:
   print( w.attack())