# Игра Алхимия. 
# (Задача — выращивать в саду разные растения, нуждающиеся в определенных условиях. Когда растения вырастут, из них можно готовить разные зелья.  )
# Программа должна:
# В начале игры у пользователя 100 монет 
# Пользователь вправе посадить растение:
# подорожник2_0 10 монет
# ХПетрушкаХ 20 монет
# Черемух 30 монет
# Растения  добавляется в инвентарь сразу же после посадки (посадили и моментально вырастили)
# Пользователь вправе приготовить зелье:
# Целебный отвар (нужно 3шт подорожник2_0)
# Приятель (ХПетрушкаХ и Подоржник2_0 2шт)
# Прилив сил ( Черемух 3шт + ХПетрушкаХ 2шт + Подорожник2_0)
# Зелья добавляет в коллекцию зельев:
# Пользователь вправе продать зелья и заработать денег:
# Целебный отвар 35 монет
# Приятель 45 монет
# Прилив сил 150 монет
# Деньги зачисляет после продажи
# Деньги списываются после приготовления

# Функция приготовления зелья
def making_a_potion(items_plant,items_potions):
    while True:
        print("""
            1. Приготовить целебный отвар
            2. Приготовить приятель
            3. Приготовить прилив сил.
            4. Выход
            """)
        print(f'Ваш баланс: {coins}',f'Ваши зелья: {items_potions}',f'Ваши растения {items_plant}')
        play_choice = int(input('Введите, что хотите сделать: '))
        if play_choice == 4:
            break
        else:
            if play_choice == 1:
                if items_plant['plantain'] >= 3:
                    items_plant['plantain'] -= 3
                    items_potions['healing_decoction'] += 1
                else:
                    print('у вас недостаточно ингридиентов')
            elif play_choice == 2:
                if items_plant['plantain'] >= 2 and  items_plant['parsley'] >= 1:
                    items_plant['plantain'] -= 2
                    items_plant['parsley'] -= 2
                    items_potions['buddy'] += 1
                else:
                    print('у вас недостаточно ингридиентов')
            elif play_choice == 3:
                if items_plant['bird_cherry_tree'] >= 3 and items_plant['parsley'] >= 2 and items_plant['plantain'] >= 1:
                    items_potions['surge_of_strengt'] += 1
                    items_plant['bird_cherry_tree'] -= 3
                    items_plant['parsley'] -= 2
                    items_plant['plantain'] -= 1
                else:
                    print('у вас недостаточно ингридиентов')
    print(items_potions)
    return items_plant,items_potions



# Функция продажи зелья
def sale(items_potions, coins ):
    while True:
        cost = 0
        
        print("""
          Что желаете продать?
          1 - Целебный отвар
          2 - Приятель
          3 - Прилив сил
          4 - Выход
          """)
        print(f'Ваш баланс: {coins}',f'Ваши зелья: {items_potions}')
        choice = int(input("Введите цифру от 1 до 4: "))
        if choice == 4:
            break
        else:
            if choice == 1 and items_potions['healing_decoction'] >= 1:
                cost += 35
                coins['money'] += cost 
                items_potions['healing_decoction'] -= 1
                print("Вы получили", cost, "монет")
            elif choice == 2 and items_potions['buddy'] >= 1:
                cost += 45
                coins['money'] += cost 
                items_potions['buddy'] -= 1
                print("Вы получили", cost, "монет")
            elif choice == 3 and items_potions['surge_of_strengt'] >= 1:
                cost += 150
                coins['money'] += cost 
                items_potions['surge_of_strengt'] -= 1
                print("Вы получили", cost, "монет")
            elif choice == 4:
                print ('Спасибо за посещение магазина')
                break
            elif choice >= 5:
                print("Вы ввели некорректный вариант")
            else:
                print('У вас нет такого зелья')
            print("Ваш баланс:", coins, "монет")
        # answer = input("Желаете продать что-то еще? (Да/Нет) ")
        # if answer.lower() == 'да':
        #     continue
        # elif answer.lower() == 'нет':
        #     break
        # else:
        #     print("Вы ввели некорректный ответ")
        #     break
    print('Вы заработали', cost)
    return coins, items_potions


# Функция посадки растений 
def plant_a_plant(coins, items_plant):
    while True:
        
        print(''' Что Вы хотите посадить?'
                                1. Подорожник = 10 монет
                                2. Петрушка = 20 монет
                                3. Черемух = 30 монет
                                4. Выйти
            ''')
        print(f'Ваш баланс: {coins}',f'Ваши растения: {items_plant}')
        player_choice = int(input('Введите цифру: '))
        if player_choice == 4:
            break
        else:
            if player_choice == 1 and coins['money'] >= 10:
                items_plant['plantain'] += 1
                coins['money']  -= 10
                print('Ваш баланс:', coins)
            elif player_choice == 2 and coins['money'] >= 20 :
                items_plant['parsley'] += 1
                coins['money'] -= 20
                print('Ваш баланс:', coins)
            elif player_choice == 3 and coins['money'] >= 30:
                items_plant['bird_cherry_tree'] += 1
                coins['money']  -= 30
                print('Ваш баланс:', coins)
            else:
                print('У вас недостаточно средств ')
    return coins, items_plant

# ----------------------------------------------ИГРА-------------------------------------------
print('Добро пожаловать в игру: Алхимия')
items_plant = {'plantain': 0,'parsley': 0, 'bird_cherry_tree': 0}
coins = {'money': 100}
items_potions = {'healing_decoction': 0, 'buddy': 0,'surge_of_strengt': 0}
while True:
    print("""
          Вы можете:
          1. Посадить растения.
          2. Приготовить зелье
          3. Продать зелья
          4. Просмотреть инвентарь
          5. Выйти из игры.
          """)
    #print(items_potions)
    #print(items_plant)
    play_choice = int(input('Введите ваше дейсвие: '))
    if play_choice == 5:
        print('Ваш инвентарь')
        print(coins,items_potions,items_plant)
        print('Всего ХОРОШЕГО')
        break
    else:
        if play_choice == 1:
            res =  plant_a_plant(coins,items_plant)
            coins, items_plant = res[0],res[1]
            print(res)
        elif play_choice == 2:
            res2 = making_a_potion(items_plant,items_potions)
            items_plant, items_potions = res2[0], res2[1]
            print(res2)
            
        elif play_choice == 3:
            res3 = sale(items_potions, coins)
            items_potions, coins = res3[0], res3[1]
            print(res3)
        elif play_choice == 4:
            print('Ваш инветарь')
            print('Растяния: ',items_plant)
            print('Ваши зелья:', items_potions)
            print('Баланс: ',coins)
        else: 
            print('Вы ввели что-то не то')
