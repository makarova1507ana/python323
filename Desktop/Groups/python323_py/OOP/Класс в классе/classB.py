class B:
    def __init__(self, name, date):
        self.__name =  name
        self.__date = date
    
    @property
    def name(self):
        return self.__name