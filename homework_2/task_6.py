# Угадай-ка за 10 попыток. Числа от 1 до 100.

import random

MIN = 1
MAX = 100
SHOTS = 10

num = random.randint(MIN, MAX)

for i in range(SHOTS):
    ans = int(input('Введи ответ: '))

    if ans == num:
        print('Угадал! Молодец!!!')
        break
    elif ans > num:
        print('Твой ответ больше!')
    else:
        print('Твой ответ меньше!')

if i == 10:
    print(f'А ответ был {num}')
