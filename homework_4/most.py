# Определить, какое число в массиве встречается чаще всего.

import random

MIN_LIMIT = -5
MAX_LIMIT = 6
SIZE = 100
RANGE = MAX_LIMIT - MIN_LIMIT

massiv = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]


# Сложность O(2*n)
def most(mas):

    mas_twin = [0 for _ in range(RANGE + 1)]
    max_ = 0
    num = MIN_LIMIT - 1

    for i in mas:
        mas_twin[i] += 1

    for i, item in enumerate(mas_twin):
        if item > max_:
            max_ = item
            num = i
    return num if abs(num - (RANGE + 1)) >= RANGE // 2 else num - (RANGE + 1), max_

# 100 loops, best of 3: 118 usec per loop - 100
# 100 loops, best of 3: 1.17 msec per loop - 1000
# 100 loops, best of 3: 11.7 msec per loop - 10000

print(most(massiv))
print('Массив: ', *massiv)
print(f'Чаще всего встречается число {most(massiv)[0]}', end=' ')

print(f'Оно попалось {most(massiv)[1]} раз.')


