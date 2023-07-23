class User:
    def __init__(self,name:str=""):
        self.__name=name    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
user = User('Ivan')
user.name = 'Vanya'
print(user.name)