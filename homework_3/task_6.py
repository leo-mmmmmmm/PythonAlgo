# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

MIN_LIMIT = 0
MAX_LIMIT = 100
SIZE = 10

mas = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

min_elem = MAX_LIMIT - 1
max_elem = MIN_LIMIT + 1

min_elem_in = -1
max_elem_in = -1

count = 0

for i, item in enumerate(mas):
    if item > max_elem:
        max_elem = item
        max_elem_in = i
    if item < min_elem:
        min_elem = item
        min_elem_in = i

if max_elem_in > min_elem_in:
    for i in range(min_elem_in + 1, max_elem_in, 1):
        count += mas[i]
else:
    for i in range(max_elem_in + 1, min_elem_in, 1):
        count += mas[i]

print('Массив: ', *mas)
print(f'Максимальный элемент: {max_elem}')
print(f'Минимальный элемент элемент: {min_elem}')
print(f'Сумма между ними разна: {count}')