# l = [0]*5 #
# l[1]=5
# l[2]=5
# print(l)

# l = [[0]*5]*5 #
# l[0][0]=5
# print(l)

# l = [*range(10)] #
# print(l)


# #def f(*args, **kwargs):#args - arguments
#   # concatenate.py
# def concatenate(**kwargs): # передача неограниченного числа ИМЕННОВАННЫХ значений
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     # print(kwargs) # словарь
#     # print(kwargs.values())# список только значений
#     # for arg in kwargs.values():
#     #     print(arg)
#     #     result += arg
#     for key in kwargs:
#         print(key, kwargs[key])
#         result += kwargs[key]
#     return result

# print("****ITOG*****",concatenate(a="Real", b="Python", c="Is", d="Great", e="!")) # concatenate -фукнцияЮ которая склеивает строки
def square(x,power=2):
    return x**power

print(square(3))

class User:
    def __init__(self):
        self.id=0
        

