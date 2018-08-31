# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

MIN_LIMIT = -5
MAX_LIMIT = 5
SIZE = 10

mas = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

min_elem_1 = MAX_LIMIT + 1
min_elem_2 = MAX_LIMIT + 1

for num in mas:
    if num < min_elem_2:
        if num <= min_elem_1:
            min_elem_2 = min_elem_1
            min_elem_1 = num
        else:
            min_elem_2 = num

print('Массив: ', *mas)
print(f'Первое минимальное число: {min_elem_1}')
print(f'Второе минимальное число: {min_elem_2}')
