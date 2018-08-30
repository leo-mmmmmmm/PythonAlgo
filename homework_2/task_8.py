# Определить, сколько раз встречается цифра
# во введённой последовательности чисел.

posl = ''
total = 0

num = int(input('Сколько чисел хочешь ввести: '))

for i in range(1, num + 1):
    n = input(f'Введи число №{i}: ')
    posl += n

find = input('Какую цифру хочешь найти? ')

for i in posl:
    if i == find:
        total += 1

print(f'Цифра {find} встречается {total} раз')