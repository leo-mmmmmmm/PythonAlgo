# Написать программу, которая генерирует в указанных пользователем границах:
# - случайное целое число;
# -случайное вещественное;
# -случайный символ;

import random

print('Введите:\n'
      'i – для целых числел;\n'
      'F – для вещественных числел;\n'
      'L – для символов.\n')

ans = input('Ответ: ')

if ans == 'i':
    print('Введите диапазон целых чисел, где a > b.\n')
    a = int(input('Целое a = '))
    b = int(input('Целое b = '))

    res = random.randint(a, b)

    print(f'Случайное число = {res}')
elif ans == 'F':
    print('Введите диапазон вещественных чисел, где a > b.\n')
    a = float(input('Вещ-ое a = '))
    b = float(input('Вещ-ое b = '))

    res = random.uniform(a, b)

    print(f'Случайное число = {res:.3f}')
else:
    print('Введите диапазон символов в алфавитном порядке.\n')
    a = input('Символ a = ')
    b = input('Символ b = ')

    a = ord(a)
    b = ord(b)

    res = random.randint(a, b)

    print(f'Случайное число = {chr(res)}')

