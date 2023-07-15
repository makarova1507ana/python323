# + Создать список из 10 студентов - список объектов
# показать всех студентов из одной группы, -> необхоимо реализовать геттер для группы
# отсортировать студентов по среднему баллу
# осортировать студенту по имени
from Student import Student
import random
students = []
names = ['Ivan Ivanov','Petr Petrov','Vanya Ivanov']
groups = ['p123','q24','q333','t96']

for i in range(10):
    student = Student(names[random.randint(0,2)],#random.randint(0,2) -выбирает случайный индекс
                      groups[random.randint(0,3)],
                      random.randint(0,100))
    students.append(student)


# for i in range(10):
#     students[i].show()#students[i] - это объект 1 студент
#     #print(students[i].group)   #print(students[i].getGroup())
#     #print(students[i].name())   


students[0].setGroup('123')
print(students[0].group)
students[0].setGroup(123)

students[0].setGroup(123)
students[0].setGroup({123})