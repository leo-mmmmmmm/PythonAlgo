# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

MIN_LIMIT = -100
MAX_LIMIT = -1
SIZE = 10

mas = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

max_el = MIN_LIMIT - 1
max_el_ind = -1

for i, item in enumerate(mas):
    if item > max_el:
        max_el = item
        max_el_ind = i

print('Массив: ', *mas)
print(f'Максимальный отрицательный элемент -- это {max_el}, а его позиция -- это {max_el_ind}')
