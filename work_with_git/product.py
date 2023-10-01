""" 
1.Решить задачу
Создать класс товар (имя, цена, тип), реализовать метод по редактированию цены товара (не может быть меньше 0)

2.Добавить  коммит в репозиторий с указанием " файл.py  added  
Params for class Product:

@name - name of product
@cost - cost of product
@type - type of product
@cost - updating cost is the method of product "


3.Отправить измения на удаленный репозиторий  
"""


#1.Решить задачу
#Создать класс товар (имя, цена, тип), реализовать метод по редактированию цены товара (не может быть меньше 0)

# ---ссылки на сеттеры ---------#
#https://highload.today/getters-setters-python/#:~:text=%D0%A1%D0%B5%D1%82%D1%82%D0%B5%D1%80%20%D0%B2%20Python%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4,%D1%81%D0%BA%D1%80%D1%8B%D1%82%20%D0%BE%D1%82%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9%20%D0%B8%D0%B7%D0%B2%D0%BD%D0%B5%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0.
#https://docs.python.org/3/library/functions.html?highlight=property#property


"""
Class 

method  price - редактирование цены
"""

class Product:
    def __init__(self, name, price, types): #ctrl + shilt + l - мультикурсор
        if type(name) is not(str):
            raise " name Не соответсует заявленному типа string"  
        
        self.__price_checker(price) 
        
        if type(types) is not(str):
            raise "types Не соответсует заявленному типа string"  
        
        self.name = name
        self.__price = price
        self.types = types
        
    def __price_checker(self, value):
        if not(type(value) in [float, int]):
            raise "price Не соответсует заявленному типа int or float"  
        if value < 0:
            raise "price < 0"
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price_checker(value) 
        self.price = value
        
        
        