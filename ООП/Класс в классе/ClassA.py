from classB import *

class A:
    def __init__(self, count_season:int=1, *series):
        self.__count_season =  count_season
        self.__list_of_series = []
        for serie in series:#serie - object of classB
            self.__list_of_series.append(serie) # list of series
    
    def show_series(self):
        for serie in self.__list_of_series: #serie - object of classB
            print(serie.name)
            
b1 = B('serie1','12-02-2000')
b2 = B('serie2','13-02-2000')

a = A(1,b1, b2)
a.show_series()