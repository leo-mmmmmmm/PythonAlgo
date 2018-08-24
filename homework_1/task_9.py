# Вводятся 3 числа. Найти среднее.

print('Введите 3 разных числа.')

a = int(input('Первое число = '))
b = int(input('Второе число = '))
c = int(input('Третье число = '))

ma = a
mi = c

if ma > b:
    if ma > c:
        if mi < b:
            sr = b
        else:
            mi = b
            sr = c
    else:
        ma = c
        mi = b
        sr = a
else:
    ma = b
    if ma > c:
        if mi < a:
            sr = a
        else:
            mi = a
            sr = c
    else:
        ma = c
        mi = a
        sr = b

print(f'Среднее число = {sr}')



