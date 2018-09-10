# Вывести сумму n членов прогрессии: 1, -0.5, 0.25 и т.д.

import sys

MEMORY_EATEN = 0


def sum_geom(b1, q, n, memory=0):
    memory = (sys.getsizeof(b1) + sys.getsizeof(q) + sys.getsizeof(n))
    return b1*(q**n - 1)/(q - 1), memory


n = int(input('Введите кол-во членов: '))
MEMORY_EATEN += sys.getsizeof(n)

print(f'Ответ: {sum_geom(1, -0.5, n)[0]}')
MEMORY_EATEN += sum_geom(1, -0.5, n)[1]
print(f'Всего было съедено {MEMORY_EATEN} байт.')