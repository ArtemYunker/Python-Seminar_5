from random import randint


player1 = input('Введите имя игрока 1: ')
start_name = randint(1, 2)
boot = 'Computer'
a = 1
if start_name == 1:

    print(f'Начинает {player1} ')

else:

    print(f'Начинает {boot} ')

k = 100  # Количество конфет в игре

count1 = 0
count2 = 0
a = 1
while k > 0:
    a = 1
    if start_name == 1:
        print(f'Ходит игрок {player1}')
        n = int(input('сколько конфет возьмете? '))
        if 1 <= n <= 28:
            k = k-n
            count1 = count1 + n
            print(f'Осталось {k} конфет')
            start_name = a+1
        else:
            print('можно вхять не более 28 конфет')
        if k == 1:
            print(f'Выйграл игрок {boot}')
            print(f'Количество конфет для выйгрыша  {count2}')
            break
    else:
        if k <= 28:
            print(f'Ходит игрок {boot}')
            n = randint(2, k)
            print(f'Computer взял {n} конфет')
            k = k-n
            count2 = count2 + n
            print(f'Осталось {k} конфет')
            start_name = start_name-1
            if k == 1:
                print(f'Выйграл игрок {player1}')
                print(f'Количество конфет для выйгрыша  {count1}')
                break
        else:
            print(f'Ходит игрок {boot}')
            n = randint(1, 28)
            print(f'Computer взял {n} конфет')
            k = k-n
            count2 = count2 + n
            print(f'Осталось {k} конфет')
            start_name = start_name-1
            if k == 1:
                print(f'Выйграл игрок {player1}')
                print(f'Количество конфет для выйгрыша  {count1}')
                break
