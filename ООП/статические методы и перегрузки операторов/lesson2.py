#------------------Перегрузка операторов--------------------------#

class Point:
    def __init__(self,x:float=0,y:float=0):#перегрузка оператора =
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    # def sumPoint(self, otherPoint):
    #     point_r = Point(self.__x + otherPoint.x, self.__y + otherPoint.y)
    #     return point_r
    
    #перегрузка (новое действие) оператора + __add__ # ovrloading(overwrite)  operator
    def __add__(self, otherPoint):# otherPoint -просто переменная
        return Point(self.x + otherPoint.x, self.y + otherPoint.y) #можно вернуть все что вы хотите
    
    #перегрузка (новое действие) оператора == __eq__
    def __eq__(self, other):
        # if (self.x == other.x) and (self.y == other.y):
        #     return True
        # return False
        return (self.x == other.x) and (self.y == other.y)
    
    def __str__(self): #перегрузка (новое действие) магический метод для str()
       # return '('+str(self.x) +', '+ str(self.y)+')' #обязательно должна быть строка
        return f'({str(self.x)}, {str(self.y)})'

# # a = 5
# # b = 5
# # c = a==b
# # print(c)
# # # pointA = Point(1,2)
# # # pointB = Point(5,5)
# # pointA = Point(5,5)
# # pointB = Point(5,5)
# # pointC = pointA == pointB
# # print(pointC)


# pointC = pointA + pointB #Point.sumPoint(pointA, pointB)#pointA.sumPoint(pointB) 
# print(pointC)

#print(pointC.x, pointC.y)
a = 5
a = str(a)
print(type(a))
A = Point(2,2)
# A = str(A)
# print(type(A),A, A[0], A[5] )
A = str(A)
print(type(A),A )
