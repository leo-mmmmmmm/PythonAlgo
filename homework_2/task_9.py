# Среди натуральных чисел, которые были введены, найти наибольшее.
# Вывести его и сумму его цифр.

summ = 0
max_n = 0
max_c = 0

while True:
    n = input('Введите число или 0 для выхода: ')

    if n == '0':
        break
    else:
        for i in n:
            summ += int(i)

        if summ > max_c:
            max_n = int(n)
            max_c = summ
            summ = 0

print(f'Число с максимальной суммой цифр: {max_n}\n'
      f'Сумма цифр равна: {max_c}')

