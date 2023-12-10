""" 
Класс Покупатель: Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, Номер банковского счета;





Методы: установка значений атрибутов, получение значений атрибутов, вывод информации. 
Создать массив объектов(экземпляры класса) данного класса. Вывести список покупателей в алфавитном порядке и 
список покупателей,
у которых номер кредитной карточки находится в заданном диапазоне.
"""


class Customer:
    # Свойства - должны быть закрыты
    #Класс Покупатель: Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, Номер банковского счета;
    def __init__(self, lastName:str='', firstName:str='', secondName:str='', adress:str='*', cardNumber:str='*', accountNumber:str ='*'):
        self.__name = {'last name': lastName, 'first name': firstName, 'second name': secondName}#только к одному покупателю
        self.__adress = adress
        self.__cardNumber = cardNumber
        self.__accountNumber = accountNumber
        
    #Методы:  получение значений атрибутов, вывод информации. 
    def show(self):#вывод информации. 
        print(self.__name, self.__adress, self.__cardNumber, self.__accountNumber, sep='\n')
    
    # получение значений атрибутов
    # геттер - get - получить    (получить значение атрибута)
    def getName(self):
        return self.__name
    
    # (получить значение adress)
    def getAdress(self):
        return self.__adress
    
     # (получить значение cardNumber)
    def getCardNumber(self):
        return self.__cardNumber
    
    # (получить значение accountNumber)
    def getAccountNumber(self):
        return self.__accountNumber
        
    # редактировать атрибуты класса
    # сеттер - set - установить    (установить новое значение атрибута)
    def setLastName(self, lastName:str):
        self.__name['last name'] =  lastName
    # сеттер - set - установить    (установить новое значение атрибута)
    def setAdress(self, adress:str):
        self.__adress =  adress

# # customer = Customer('Makarov','Ivan', 'ivanovich', 'st. bulvar 25', 222, 2222)
# # print(customer.name)
# # customer2 = Customer('Ivanov','Ivan', 'ivanovich', 'st. bulvar 25', 222, 2222)
# # print(customer2.name['last name'])
# customer = Customer()# класс с значением по умолчанию
# print(customer.getAccountNumber())
# customer.show()
# customer = Customer('Ivanov','Ivan', 'Ivanovich',)
# print(customer.getName()['last name'])
# customer.setLastName('kAC')
# print(customer.getName())

# customer.show()



#------------------------------Задание-----------------------------------------#
"""
класс кот
кличка (задает игрок или по умолчанию)
возраст (задает игрок или по умолчанию)
сытость (50) 
сон (50)
счастье (50)

методы: играть(+1 счастье, -1 сон, -1 сытость), спать(+0 счастье, +1 сон, -1 сытость), кушать(+1 счастье, +0 сон, +1 сытость),  показать состояние
"""
class Cat:
    def __init__(self, name: str = 'Tamo', age: int = 1):
        self.__name = name
        self.__age = age
        self.__satiety = 50
        self.__dream = 50
        self.__happiness = 50

    def play(self):
        self.__happiness += 1
        self.__dream -= 1
        self.__satiety -= 1

    def eat(self):
        self.__happiness += 1
        self.__satiety += 1

    def sleep(self):
        self.__dream += 1
        self.__satiety -= 1

    def show(self):
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nCытость: {self.__satiety}\n'
              f'Сон: {self.__dream}\nСчастье: {self.__happiness}\n')

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age
        
catVasya = Cat('Vasya')
catVasya.play()
catVasya.show()
 