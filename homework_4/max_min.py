# В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.

import cProfile

import random

MIN_LIMIT = 0
MAX_LIMIT = 100
SIZE = 10

massiv = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]


def max_min(mas):

    max_elem = max(mas)
    min_elem = min(mas)

    max_elem_in = mas.index(max_elem)
    min_elem_in = mas.index(min_elem)

    mas[max_elem_in], mas[min_elem_in] = mas[min_elem_in], mas[max_elem_in]
# 100 loops, best of 3: 110 usec per loop - 100
# 100 loops, best of 3: 1.08 msec per loop - 1000
# 100 loops, best of 3: 10.8 msec per loop - 10000


def max_min_for(mas):

    min_elem = MAX_LIMIT - 1
    max_elem = MIN_LIMIT + 1

    min_elem_in = -1
    max_elem_in = -1

    for i, item in enumerate(mas):
        if item > max_elem:
            max_elem = item
            max_elem_in = i
        if item < min_elem:
            min_elem = item
            min_elem_in = i

    mas[max_elem_in], mas[min_elem_in] = mas[min_elem_in], mas[max_elem_in]
# 100 loops, best of 3: 109 usec per loop - 100
# 100 loops, best of 3: 1.1 msec per loop - 1000
# 100 loops, best of 3: 11.1 msec per loop - 10000





# max_min(massiv)
# max_min_for(massiv)
