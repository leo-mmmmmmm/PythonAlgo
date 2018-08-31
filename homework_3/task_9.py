# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

MIN_LIMIT = -5
MAX_LIMIT = 5
SIZE_X = 5
SIZE_Y = 2

mas = [[random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE_X)] for __ in range(SIZE_Y)]

mas_min = [0] * SIZE_X
min_el = MAX_LIMIT + 1

for i in range(SIZE_X):
    for j in range(SIZE_Y):
        if mas[j][i] < min_el:
            min_el = mas[j][i]
    mas_min[i] = min_el
    min_el = MAX_LIMIT + 1


max_el = MIN_LIMIT - 1
for i in mas_min:
    if i > max_el:
        max_el = i

print('Массив: ')
for i in range(SIZE_Y):
    print(*mas[i])

print('Массив ммнимальных элементов: ', *mas_min)
print(f'Максимальное из минимальных: {max_el}')