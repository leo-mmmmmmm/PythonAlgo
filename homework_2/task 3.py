# Сформировать из введённого числа обратное по порядку.

num = input('Введите число: ')

mun = ''

for i in range(len(num)-1, -1, -1):
    mun += num[i]

print(mun)

