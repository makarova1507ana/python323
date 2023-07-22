# #статические методы и перегрузки операторов
# class User:
#     #статические атрибуты
#     # id - стал закрытым
#     __id = 0 #статические атрибуты - не присваивается к какому-то конкретному объекту
#     def __init__(self,name:str=""):
#         self.__name=name
#         self.__id = User.__id_up() 
        
#     #статические методы - избавляет от необходимости использовать конкретный объект
#     #__id_up() закрыли
#     @staticmethod
#     def __id_up():# увелечение id
#         User.__id += 1
#         return User.__id
    
#     @property
#     def id(self):
#         return self.__id
    
# user0 = User('Ivan')# id  -общий атрибут для каждого объекта  | self.__id -конкретный атрибут для конкретного объекта
# user1 = User('Vanya')# id  -общий атрибут для каждого объекта | self.__id -конкретный атрибут для конкретного объекта
# user2 = User('Egor')# id  -общий атрибут для каждого объекта | self.__id -конкретный атрибут для конкретного объекта
# print('id',user0.id)# id__  -обращаемся к индивидуальному  атрибут данного объекта
# print('id',user1.id)# id__  -обращаемся к индивидуальному  атрибут данного объекта

# #print('id',user0.id)# id  -общий атрибут для каждого объекта
# #User.id_up()
# #print('id',User.id)
# #User.id_up()
# #print('id',user0.id)
# #print('id',user1.id)
# print('id',user0.id)# id__  -обращаемся к индивидуальному  атрибут данного объекта

# #print('id',user2.id)

# #User.id_up()
# #print('id',User.id)
# # print(user0.id, user1.id, user2.id)
    



# # i = 0
# # def f():
# #     global i 
# #     i+=1
# #     return i

# # print(f())
# # print(f())



import random as r

#статические методы 
class User:
    #статические атрибуты
    # id - стал закрытым
    __id = 0 #статические атрибуты - не присваивается к какому-то конкретному объекту
    def __init__(self,name:str="", password:str=''):
        self.__name=name
        self.__id = User.__id_up() 
        # password=='' пользователь не задал пароль 
        if password=='':
            self.__password = User.generate_password()
        else:
            self.__password = password

        
    #статические методы - избавляет от необходимости использовать конкретный объект
    #__id_up() закрыли
    @staticmethod
    def __id_up():# увелечение id
        User.__id += 1
        return User.__id
    
    
    @staticmethod
    def generate_password():# увелечение id
        alfa_upper = 'ABCD'
        alfa = 'abcd'
        char = '.,/*'
        password = alfa_upper[r.randint(0,3)]+ alfa[r.randint(0,3)] +  char[r.randint(0,3)] +str(r.randint(0,9))
        return password
    
    @property
    def id(self):
        return self.__id
    @property
    def password(self):
        return self.__password
    
user0 = User('Ivan','pass1')# id  -общий атрибут для каждого объекта  | self.__id -конкретный атрибут для конкретного объекта

user_choice = input('would you like to generate a password?')
if user_choice == 'no':
    user1 = User('Vanya')# id  -общий атрибут для каждого объекта | self.__id -конкретный атрибут для конкретного объекта

user_choice = input('would you like to generate a password?')
if user_choice == 'yes':
    password = User.generate_password()  
    user2 = User('Egor', password)# id  -общий атрибут для каждого объекта | self.__id -конкретный атрибут для конкретного объекта

elif user_choice == 'no':
    user2 = User('Egor')# id  -общий атрибут для каждого объекта | self.__id -конкретный атрибут для конкретного объекта

print('id',user0.id, 'password', user0.password)# id__  -обращаемся к индивидуальному  атрибут данного объекта
print('id',user1.id, 'password', user1.password)# id__  -обращаемся к индивидуальному  атрибут данного объекта
print('id',user2.id, 'password', user2.password)# id__  -обращаемся к индивидуальному  атрибут данного объекта


print('id',user0.id)# id__  -обращаемся к индивидуальному  атрибут данного объекта
