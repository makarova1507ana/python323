def min_divider(a):# a - число , для которого ищем делитель
    if a == 1 or a == 0:
        return a
    for el in range(2, a+1):
        if a % el == 0:
            return el # точка выхода из функции


#просто функция
def f():
    return 0
            