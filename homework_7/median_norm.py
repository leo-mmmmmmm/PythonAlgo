# Нормальный вариант поиска медианы через сортировку merge sort.
import random
from homework_7.merge_sort import merge_sort, merge


def find_median(array):
    if len(array) % 2 != 0:
        return array[len(array) // 2]
    else:
        return array[len(array) // 2 - 1]


m = int(input('Введите m: '))
print(f'Массив будет размером {2*m + 1}')

mas = [random.randint(1, 2*m + 1) for i in range(2*m + 1)]
print(mas)

merge_sort(mas, 0, 2*m)
print(mas)

print(find_median(mas))

