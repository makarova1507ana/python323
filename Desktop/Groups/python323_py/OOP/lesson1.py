# класс - это пользовательское описание типа данных
#это описание того, какими свойствами и поведением будет обладать объект.
class Person:# Person - название
    #  специальный метод (фукнция)  - инициализатор (создали и сразу присвоили)
    def __init__(self, name:str, age:int):# self(можно переимновать)- обязательный параметр, он указатель на объект, после указываются атрибуты  столько сколько нужно
        # атрибуты - полями класса или свойствами
        self.name_person = name    # имя человека
        self.age = age        # возраст человека
        
#это конец описания

# # создание объекта
# person = Person('Динозавр', 9999)
# person2 = Person('Динозавр2', 9999999)
# print(person.name_person, person.age)
# print(person2.name_person, person2.age)


# ---------------------------------задание-------------------------------------------#
"""
    создать класс самолет
        указать свойства имя самолета, вместимость - кол-во пассажиров, имя рейса
"""
# class Airplane:
#     def __init__(self, name: str, capacity: int, flight: str):

#         self.name = name
#         self.capacity = capacity
#         self.flight = flight

# ---------------------------------задание-------------------------------------------#
"""
    Создать объект типа самолет
"""
# airplane = Airplane('Боинг',200,'Москва-Санкт-Петербург')
# print(airplane.name_airplane,airplane.capacity,airplane.flight)






#---------------------------------------Методы---------------------------------------------#

# class Airplane:
#     def __init__(self, name: str, capacity: int, flight: str):
#         # поля  класса - характеристики 
#         self.name = name
#         self.capacity = capacity # вместимость 
#         self.flight = flight
#         self.passagers = 0 # кол-во пассажиров
    
#     # метод(поведение или действие объекта) - показать характеристики самолета
#     def show(self):
#         print(self.name, self.capacity,self.flight, self.passagers)


        

# airplane = Airplane('Боинг',200,'Москва-Санкт-Петербург')
# airplane.flight = ('Istanbul','Moscow')# очень плохо и так делать не надо
# print(airplane.flight[0])
# airplane.flight = ('Moscow','Istanbul')# очень плохо и так делать не надо
# print(type(airplane.flight))
# airplane.passagers = 10
# airplane.show()

# airplane2 = Airplane('Боинг',300,'Санкт-Петербург')
# airplane2.show()


#---------------------------------------Задание---------------------------------------------#
""" 
Для класса Airplane определить метод, который будет увеличивать кол-во passegers
"""

# class Airplane:
    
#     def __init__(self, name: str, capacity: int, flight: str):
#         # поля  класса - характеристики 
#         self.name = name
#         self.capacity = capacity # вместимость сколько может сесть пассажиров
#         self.flight = flight
#         self.passagers = 0 # кол-во пассажиров
    
#     # метод(поведение или действие объекта) - показать характеристики самолета
#     def show(self):
#         print(self.name, self.capacity,self.flight, self.passagers)


#     #увелечение кол-во пассажиров
#     def buy_ticket(self, count=1):# если не задали count, то 1 
#         empty_places =  self.capacity - self.passagers #200 -150 = 50
#         if empty_places > 0 and empty_places>=count : # 50>0 and 50>=3
#             self.passagers += count # кол-во пассажиров 150+50 =200

#---------------------------------------Дебаггер---------------------------------------------#
# Breakpoint - точки остановки программы
# смотрим на переменные
# airplane = Airplane('Boing',200,'Moscow-Nish')
# airplane.show() # ожидаемый результат 'Boing',200,'Moscow-Nish'
# airplane.passagers = 100
# airplane.show()
# airplane.buy_ticket(50)
# airplane.show() # ожидаемый результат passagers 150
# airplane.buy_ticket() # пытаемся купить 1 билет
# airplane.show()# ожидаемый результат passagers 151
# airplanePobeda = Airplane('Boing',200,'Moscow-Nish')
# airplaneAirflot = Airplane('Boing',400,'Moscow-Kursk')
# airplanePobeda.show()
# airplaneAirflot.show()
# airplaneAirflot.buy_ticket(300)
# airplaneAirflot.show()



#-------------------------Инкапсуляция-------------------------------#
# это скрытие или закрытие доступа  все характеристики класса должны быть закрыты


class Airplane:
    
    def __init__(self, name: str, capacity: int, flight: str):
        # поля  класса - характеристики 
        self.__name = name  # self.__name - только Airplane может что-то изменить внутри 
        self.__capacity = capacity # вместимость сколько может сесть пассажиров
        self.__flight = flight
        self.__passagers = 0 # кол-во пассажиров
    
    # метод(поведение или действие объекта) - показать характеристики самолета
    def show(self):
        print(self.__name, self.__capacity,self.__flight, self.__passagers)


    #увелечение кол-во пассажиров
    def buy_ticket(self, count=1):# если не задали count, то 1 
        empty_places =  self.__capacity - self.__passagers #200 -150 = 50
        if empty_places > 0 and empty_places>=count : # 50>0 and 50>=3
            self.__passagers += count # кол-во пассажиров 150+50 =200
    # ДОБАВИТЬ МЕТОД ВОЗРАТА БИЛЕТА

airplane = Airplane('Boing',1000,'Moscow-Nish')#  на заводе создаем 
airplane.show()
#airplane._Airplane__passagers = 500 # если очень хочется то можно НО НЕЛЬЗЯ
#airplane.show()
airplane.__passagers = 500# ничего не меняет внутри класса
#print(airplane.__passagers)
airplane.buy_ticket(100)
airplane.show()


