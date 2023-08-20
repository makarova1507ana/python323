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
    
class Cat(Animal):#
    def __init__(self, name):
        self.__name = name    

    def say(self):# перезапись  и это пример полиморфизма
        return "Meow "+ self.__name

class Wolf(Animal):
    pass

class Dog(Wolf):#
    def __init__(self, name):
        self.__name = name    

    def say(self):
        return "Gav "+ self.__name

class Fox(Animal):
    def __init__(self, name):
        self.__name = name  

# print(Cat("Barsik").say(),
# Dog("Rokki").say(),        
# Fox("fox").say())



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

class CoffeeMachine:
    def make_coffee(self):
        return "make cofee"
    
class CoffeeMachine_and_Grin(Grind,CoffeeMachine ):
    def choose(self):
        choice = input("1 or 2")
        if choice == "1":
            print(self.do_grain())
        elif choice == "2":
            print(self.make_coffee())
            

CoffeeMachine_and_Grin().choose()