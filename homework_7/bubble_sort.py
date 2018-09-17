# Сортировка "пузырьком" без повторений.
import random


def bubble_sort(array):
    swapped = False

    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break

    return array


mas = [i for i in range(-100, 100)]
random.shuffle(mas)
print(mas)
print(bubble_sort(mas))


