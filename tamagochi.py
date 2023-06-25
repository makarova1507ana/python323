import datetime

name = input('Введите имя Тамогочи:\n>')

happiness = 50
satiety = 50
dream = 50
time_list = []


def attributes(x):
    n = x
    if x <= 90:
        x += 10
    elif 90 < x < 100:
        n = 100 - n
        x += n
    return x


def stats():
    print(f'\nТамагочи:{name}\n\nСчастье:{happiness}\nСытость:{satiety}\nСон:{dream}')


while True:
    if happiness <= 0 or satiety <= 0 or dream <= 0:
        print('Ваш тамогочи погиб')
        break
    else:
        datatime_first = datetime.datetime.now()  # точная дата до ввода команды
        # print(datatime_first.second)
        input_ = input('\nвведите команду [играть, кормить, спать, характеристики, конец]\n> ')
        datatime_second = datetime.datetime.now()  # точная дата после ввода команды
        # print(datatime_second.second)
        minute_dif = datatime_second.minute - datatime_first.minute  # кол-во пройденых минут
        # print(f'mindif = {min_dif}')
        if minute_dif == 0:  # проверка на то сколько минут прошло от начала ввода команды и до её ввода
            sec_dif = datatime_second.second - datatime_first.second
            time_list.append(sec_dif)
            res = sum(time_list)
            # print(res)
            # print(time_list)
            if res >= 10:
                while res >= 10:  # кол-во секунд
                    happiness -= 1
                    satiety -= 1
                    dream -= 1
                    res -= 10
                    time_list = [res]
        elif minute_dif >= 1:
            b = minute_dif * 60 - datatime_first.second + datatime_second.second
            time_list.append(b)
            res = sum(time_list)
            # print(res)
            # print(time_list)
            if res >= 10:
                while res >= 10:  # кол-во сек
                    happiness -= 1
                    satiety -= 1
                    dream -= 1
                    res -= 10
                    time_list = [res]

        if input_ == 'играть':
            happiness = attributes(happiness)
        elif input_ == 'кормить':
            satiety = attributes(satiety)
        elif input_ == 'спать':
            dream = attributes(dream)
        elif input_ == 'характеристики':
            stats()
        elif input_ == 'конец':
            break
        else:
            print('Вы ввели что то не то 0_о')
        print(f'\nТамагочи:{name}\n\nСчастье:{happiness}\nСытость:{satiety}\nСон:{dream}')
