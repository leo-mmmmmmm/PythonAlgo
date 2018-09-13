# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import sys

MEMORY_EATEN = 0

SEASONS = ['осень', 'зиму', 'весну', 'лето']
MEMORY_EATEN += sys.getsizeof(SEASONS)

kol_vo = int(input('Сколько всего предприятий: '))
factories = [0]*kol_vo
MEMORY_EATEN += sys.getsizeof(kol_vo)
MEMORY_EATEN += sys.getsizeof(factories)


print('Введи значение прибыли за каждый квартал.')
for i in range(kol_vo):
    print(f'Для {i + 1}-го предприятия.')
    for j in range(4):
        factories[i] += int(input(f'Прибыль за {SEASONS[j]} составила: '))
MEMORY_EATEN += sys.getsizeof(i)
MEMORY_EATEN += sys.getsizeof(j)

average = sum(factories) / kol_vo
MEMORY_EATEN += sys.getsizeof(average)
less_ave = []
more_ave = []

for i, profit in enumerate(factories):
    if profit <= average:
        less_ave.append(i)
    else:
        more_ave.append(i)
MEMORY_EATEN += sys.getsizeof(profit)
MEMORY_EATEN += sys.getsizeof(less_ave)
MEMORY_EATEN += sys.getsizeof(more_ave)

print(f'Среднее значение: {average}')
print(f'Номера предприятий, заработавших менее среднего значения:', end=' ')
for i, item in enumerate(less_ave):
    if i == len(less_ave) - 1:
        print(item + 1, end='.\n')
    else:
        print(item + 1, end=', ')

print(f'Номера предприятий, заработавших более среднего значения или равного ему:', end=' ')
for i, item in enumerate(more_ave):
    if i == len(more_ave) - 1:
        print(item + 1, end='.\n')
    else:
        print(item + 1, end=', ')

print(f'Было съедено {MEMORY_EATEN} байт.')


