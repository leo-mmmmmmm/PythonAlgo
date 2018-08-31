# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

MIN_LIMIT = 0
MAX_LIMIT = 100
SIZE = 10

mas = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

index_mas = []

for i in range(len(mas)):
    if mas[i] % 2 == 0:
        index_mas.append(i)

print('Массив:', *mas)
print('Ответ: :', *index_mas)


