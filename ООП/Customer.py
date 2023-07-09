class Customer:
    # Свойства - должны быть закрыты
    #Класс Покупатель: Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, Номер банковского счета;
    def __init__(self, lastName:str='', firstName:str='', secondName:str='', adress:str='*', cardNumber:str='*', accountNumber:str ='*'):
        self.__name = {'last name': lastName, 'first name': firstName, 'second name': secondName}#только к одному покупателю
        self.__adress = adress
        self.__cardNumber = cardNumber
        self.__accountNumber = accountNumber
        
        self.id = 0
        
    #Методы:  получение значений атрибутов, вывод информации. 
    def show(self):#вывод информации. 
        print(self.__name, self.__adress, self.__cardNumber, self.__accountNumber, sep='\n')
    
    # получение значений атрибутов
    # геттер - get - получить    (получить значение атрибута)
    def getName(self):
        return self.__name
    
    # (получить значение adress)
    @property # @property -декоратор (для методов и функций даете новые вомзонжости)
    #геттер READ-ONLY
    def adress(self):
        return self.__adress
    
    # сеттер - set - установить    (установить новое значение атрибута)
    @adress.setter
    def adress(self, adress:str):
        if type(adress) == type('str'):
            self.__adress =  adress
        else:
            raise 'not string value' # исключение информация для разработчиков, что они делают что-то не то
        
     # (получить значение cardNumber)
    def getCardNumber(self):
        return self.__cardNumber
    
    # (получить значение accountNumber)
    @property 
    def accountNumber(self):
        return self.__accountNumber
    
    
        
    # редактировать атрибуты класса
    # сеттер - set - установить    (установить новое значение атрибута)
    def setLastName(self, lastName:str):
        self.__name['last name'] =  lastName
    
    