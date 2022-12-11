# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

path = 'file_in.txt'
data  = open(path,'r')

for line in data:
    print(line)

data.close

array = []
k=0
for i in range(len(line)-1):
    k=k+1
    if line[i]!=line[i+1]:
        res = (f'{k}{line[i]}')
        array.append(res)
        k=0
print(*array)

data = (open('file_out.txt', 'a'))
data.writelines(array)
data.close

string = str(input('Введите текст для дешифровки:  '))

# 12W1B12W3B24W1B14W


n = ''
res = ''
for i in range(len(string)):

    if string[i].isdigit():
        n = n+string[i]
        
    else:
        res = res + string[i] * int(n)
        n = ''

print(res)

data = (open('file_out.txt', 'a'))
data.write(res + '\n')
data.close