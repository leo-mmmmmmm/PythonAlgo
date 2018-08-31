# Определить, какое число в массиве встречается чаще всего.

import random

MIN_LIMIT = -5
MAX_LIMIT = 6
SIZE = 10
RANGE = MAX_LIMIT - MIN_LIMIT

mas = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
mas_twin = [0 for _ in range(RANGE + 1)]

max_ = 0
num = MIN_LIMIT - 1

for i in mas:
    mas_twin[i] += 1

for i, item in enumerate(mas_twin):
    if item > max_:
        max_ = item
        num = i

print('Массив: ', *mas)
print('Чаще всего встречается число', end=' ')

print(f'{num}.' if abs(num - (RANGE + 1)) >= RANGE // 2 else f'{num - (RANGE + 1)}')

print(f'Оно попалось {max_} раз.')


