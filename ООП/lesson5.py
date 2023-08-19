"""
Создать класс Занятие(цена, дата, время) атрибута класса должны быть закрыты,
для цены релизовать геттер, для даты и времени геттеры и сеттеры
"""
""" 
from datetime import *
    
class Lesson:
    def __init__(self, date:str='01/01/1900', time:str='12:00'):
        self.__price = 0
        self.__date = date
        self.__time = time
    
    @property
    def price(self):
        return self.__price
    
    @property
    def date(self):
        return self.__date
    
    @property
    def time(self):
        return self.__time
    
    @date.setter
    def date(self,  date:str):
        self.__date = date
        
    @time.setter
    def time(self, time:str):
        self.__time = time
        
    def __str__(self):
        return self.__date +' ' + self.__time

today = datetime.today()        
#print(today.strftime("%d/%m/%Y, %H:%M"))# преобразовать к строке

lesson = Lesson(today.strftime("%d/%m/%Y"), today.strftime("%H:%M"))
print(lesson)
""" 
#-----------------------------------------------------------------------------------#

"""
Создать класс Занятие(цена, дата, время) атрибута класса должны быть закрыты,
для цены,  для даты и времени релизовать  геттеры и сеттеры
А также создать Администратор(есть права на создание и редактирование)
и Кассир (есть права на создание)
"""


from datetime import *
    
class Lesson:
    def __init__(self, date:str='01/01/1900', time:str='12:00'):
        self.__price = 0
        self.__date = date
        self.__time = time
    
    @property
    def price(self):
        return self.__price
    
    @property
    def date(self):
        return self.__date
    
    @property
    def time(self):
        return self.__time
    
    @price.setter
    def price(self,  price:float):
        self.__price = price
        
    @date.setter
    def date(self,  date:str):
        self.__date = date
        
    @time.setter
    def time(self, time:str):
        self.__time = time
        
    def __str__(self):
        return 'price: '+str(self.price) +", date: "+self.date +', time: ' + self.time

today = datetime.today()        
#print(today.strftime("%d/%m/%Y, %H:%M"))# преобразовать к строке

lesson = Lesson(today.strftime("%d/%m/%Y"), today.strftime("%H:%M"))
print(lesson)

role = "Adminstrator" # авторизация под...
if role == "Adminstrator":
    choice = "edit lesson" # create lesson
    if choice == "create lesson":
       lesson = Lesson(today.strftime("%d/%m/%Y"), today.strftime("%H:%M"))
    elif choice == "edit lesson":
        obj_edit = "price" #time date
        if obj_edit == "price":
            price = 400
            lesson.price = price
            print('Admin->  ',lesson)
elif role == "Cassir":
    pass
