# Посчитать кол-во чётных и нечётных цифр в числе.

num = input('Введите число: ')

chet = 0
nechet = 0

for i in num:
    if int(i) % 2 == 0:
        chet += 1
    else:
        nechet += 1

print(f'Кол-во чётных: {chet}')
print(f'Кол-во нечётных: {nechet}')
