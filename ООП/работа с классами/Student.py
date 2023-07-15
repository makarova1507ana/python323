# Создать класс студент
# атрибуты:
# имя
# группа
# средний балл

class Student:
    def __init__(self, name:str='', group:str='', gpa:int=0):
        self.__name = name
        self.__group = group
        self.__gpa = gpa# 100
    
    def show(self):
        print(self.__name,
        self.__group,
        self.__gpa)

    def setGroup(self, group):
        if type(group) == type('str'):
            self.__group = group
        else:
            print( "atribute must be string" )
    # #геттер
    # def getGroup(self):
    #     return self.__group
    # тоже самое, только лучше
    #       # def group(self):
    #        #      return self.__group
    
    @property # @property -декоратор (для методов и функций даете новые вомзонжости)
    #геттер READ-ONLY
    def group(self):
        return self.__group
    
    #   #    # @property # @property -декоратор (для методов и функций даете новые вомзонжости)
    #    # #геттер READ-ONLY
    #    # def getGroup(self):
    #    #     return self.__group

    #     def name(self):
    #     return self.__name