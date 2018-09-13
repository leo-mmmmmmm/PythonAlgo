# Найти медиану, или я самый умный ;D
import random
import statistics

m = int(input('Введите m: '))

print(f'Массив будет размером {2*m + 1}')

mas = [random.randint(-m, m) for i in range(2*m + 1)]
print(mas)
# Доказать, что всё верно ищет)
mas.sort()
print(mas)
print(statistics.median(mas))


