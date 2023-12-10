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












#--------------------------------------------#
"""
Создать класс Абонемент(кол-во занятий, цена(цена 10%(скидка) от одного занятия  * кол-во ) ) 
атрибута класса должны быть закрыты, для цены релизовать геттер 
"""
""" Создать класс Абономент(кол-во занятий, цена(цена 10% от одного занятия  * кол-во ) )
 атрибута класса должны быть закрыты, для цены релизовать геттер """


class Subs:
    def __init__(self, quant: int, lessonPrice:int):
        self.__quant = quant
        self.__price = lessonPrice * 0.9 * quant

    @property
    def price(self):
        return self.__price

lesson1 = Lesson()
lesson1.price=1000
s1 = Subs(10,lesson1.price)

print(s1.price)






#--------------------------------------------#
"""
РАЗБОР ДЗ

Задание
Создать класс башня, атрибуты: броня, здоровье, регуляторы увеличения и уменьшения здоровья и брони). 
Создать класс стрелковая башня, атрибуты: умеет стрелять, броня, здоровье, регуляторы увеличения и 
уменьшения здоровья и брони. 
Описать логику взаимодействия с башнями.
Описание логики взаимодействия с башнями: можно вызвать методы увеличения/уменьшения здоровья и 
брони для изменения их значений, а также можно вызвать метод стрельбы у стрелковой башни. 

КОД
"""
class Tower:
  def __init__(self, armor, health):
    self.armor = armor
    self.health = health
   

  def set_health(self, value):# value + так и с минусом
    self.health += value

  def set_armor(self, value):
    self.armor += value
 
    
class ArcherTower(Tower):
#   def shoot(self):
#     #print("The archer tower is shooting")
#     #return 50 
    def shoot(self, other):
        other.set_armor(-50)
        other.set_healf(-10)

# # Создание обычной башни
# tower1 = Tower(100, 200, 10, 5)
# # Создание стрелковой башни
# archer_tower1 = ArcherTower(80, 150, 15, 3)
# # Увеличение здоровья обычной башни на 50
# tower1.set_health(50)
# # Уменьшение брони стрелковой башни на 10
# archer_tower1.set_armor(-10)
# # Стрелковая башня выпускает стрелы
# tower1.set_health(archer_tower1.shoot())








class Tower:
    def __init__(self,name: str, armor: int, health: int):
        self.__name = name
        self.__armor = armor
        self.__health = health

    def __repr__(self):
        return self.__name

    # def damage(self):
    #     return self.__health - 10

    @property
    def armor(self):
        return self.__armor

    @property
    def health(self):
        return self.__health

    def __sub__(self, other): # уменьшение здоровья и брони башни
        self.__armor -= other 
        # if self.__armor >= 0:
        #     self.__armor -= other
        #     return self.__armor
        # else:
        #     self.__health -= other
        #     return self.__health

    def show(self):
        print(f'Башня { self.__name}, броня башни составляет {self.__armor},  здоровье башни  {self.__health}')




class Shooter(Tower):               # башня принимает дополнительный параметр стрельба
    def __init__(self,name: str, armor: int, health: int, shoot: int):
        self.__name = name
        self.__armor = armor
        self.__health = health
        self.__shoot = shoot

    # @property
    # def show(self):
    #     print(f'Башня { self.__name}, броня башни составляет {self.__armor},  здоровье башни  {self.__health}, урон башни {self.__shoot}')

defender = Tower('Жук', 100, 100)
strelok = Shooter('Бабуин',100, 100, 10)

#strelok.show
defender.show()
defender - 10 # -> defender.armor == 90
# strelok - 10
strelok.show


# башня
class Tower:
    def __init__(self, armor:int, health:int):
        self.__armor = armor
        self.__health = health

    @property
    def armor(self):
        return self.__armor

    @property
    def health(self):
        return self.__health

    # перегрузка '+' __add__
    def __add__(self, other):
        # max доп.броня_башни/armor = 50 единиц; max целостность_башни/health = 100 единиц
        return Tower(self.__armor + other.armor if (self.__armor + other.armor) < 50 else 50,
                     self.__health + other.health if (self.__health + other.health) < 100 else 100)

    # перегрузка '-' __sub__
    def __sub__(self, other):
        # атака по броне = 50% от атаки; атака по башне = 100% от атаки
        # впервую очередь атака по броне до 0 единиц, затем по башне
        # если во время атаки: armor < 0, e.g. -10, then health attack = |-10|*2 # где *2 -- возврат к 100% атаки
        return Tower(0 if (self.__armor - other.attack/2) < 0 else self.__armor - other.attack/2,
                     self.__health - abs((self.__armor - other.attack/2)*2)
                     if (self.__armor - other.attack/2) <= 0 else self.__health - 0)

#
#

# стрелковая башня
class AttackTower(Tower):
    def __init__(self, attack:int, armor:int, health:int):
        self.__attack = attack
        super().__init__(armor, health)

    @property
    def attack(self):
        return self.__attack


#
#


tower = Tower(20, 60)                   # башня с бронёй = 20 единиц и целостностью = 60 единиц
heal_armor = Tower(5, 0)                # восстановить броню на 5 единиц
# heal_armor = 5
heal_health = Tower(0, 15)              # восстановить башню (целостность) на 15 единиц
# heal_health = 15
attack = AttackTower(50, 5, 25)   # стрелковая башня с атакой в 50 единиц

while True:
    print('БАШНЯ доп.броня/целостность:', tower.armor, "..", tower.health)

    print('''\nукажите номер действия:
    1. атаковать стрелковой башней
    2. добавить брони
    3. ремонт башни''')
    action = int(input('<< '))

    match action:
        case 1: tower = tower - attack
        case 2: tower = tower + heal_armor
        # case 2: tower.armor = tower.armor + heal_armor
        case 3: tower = tower + heal_health
        # case 3: tower.health = tower.health + heal_health

    if tower.health <= 0:
        print('башня повержена')
        break

