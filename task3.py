# 3.	Создайте программу для игры в "Крестики-нолики".

from random import randint


sp = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print(type(sp))
player1 = input('Введите имя игрока 1: ')
player2 = input('Введите имя игрока 2: ')

start_name = randint(1,2)
if start_name ==1:
    print(f'Начинает {player1} ')

else:
    print(f'Начинает {player2} ')

k = 1  # Количество ходов в игре


i = 0
j = 0
array = [ (i,j), (i,j+1), (i,j+2), (i+1,j), (i+1,j+1), (i+1,j+2), (i+2,j), (i+2,j+1), (i+2,j+2)]

print(*sp, sep='\n')
while k <= 9:
    
    print()
    print(' Ход - цифра от 1 до 9 ')
    perv = int(input('Ходите!!!  '))
    a = list(array[perv-1])
    sp[a[0]][a[1]] = 'X'
    print(*sp, sep='\n')

    
    
    vtor = int(input('Ходите!!!  '))
    b = list(array[vtor-1])
    sp[b[0]][b[1]] = '0'
    print(*sp, sep='\n')
    k = k + 1