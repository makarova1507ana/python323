#-----------------------------декораторы------------------------------------#
# def decor_f(func):
#     print('decor_f')
#     def fun():
#         func()
#     return fun


# @decor_f
# def f():
#     print('f')
# f()



from Customer import *
customer = Customer()
print(customer.getCardNumber()) #получение атрибута класса при помощи метода геттер
print(customer.adress) # получение атрибута класса при помощи декоратора геттре

customer.setLastName('New NAme')# установка атрибута класса при помощи  метода сеттера
print(customer.getName())

customer.adress = 'new adress' # установка атрибута класса при помощи декоратора сеттера
print(customer.adress) # получение атрибута класса при помощи декоратора геттре

customer.id = 1
print(customer.id)
