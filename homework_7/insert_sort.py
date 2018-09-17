# Сортировка "вставками".
import random


def insertion_sort(array):

    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while (i > -1) and key < array[i]:
            array[i + 1] = array[i]
            i = i - 1

        array[i + 1] = key
        print(array)
    return array


mas = [i for i in range(-10, 1)]
random.shuffle(mas)
print(mas)
print(insertion_sort(mas))

