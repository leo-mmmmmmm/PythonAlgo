# Написать миникалькулятор.

print('Введите 2 числа для операций.')
a = int(input('Первое число: '))
b = int(input('Второе число: '))

while True:
    print('Выберите операцию:\n'
          '+ для сложения,\n'
          '- для вычитания,\n'
          '* для умножения,\n'
          '/ для деления,'
          '0 для выхода.')
    ans = input('Ответ: ')

    if ans == '0':
        print('КОНЕЦ')
        break
    if ans == '+':
        print(f'a + b = {a + b}\n')
    elif ans == '-':
        print(f'a - b = {a - b}\n')
    elif ans == '*':
        print(f'a * b = {a * b}\n')
    elif ans == '/':
        if a == 0 or b == 0:
            print('На ноль делить нельзя!!!')
        else:
            print(f'a / b = {a / b}\n')




