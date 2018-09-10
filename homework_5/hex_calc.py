# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.


HEX_DICT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}
TEN_DICT = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}


def from_hex_to_ten(mas):
    num = 0
    for i in range(len(mas)):
        num = num + HEX_DICT[mas[i]] * (16 ** i)
    return num


def from_ten_to_hex(num):
    n = ''
    while num > 0:
        y = str(num % 16)
        if y in TEN_DICT:
            n = TEN_DICT[y] + n
        else:
            n = y + n
        num = int(num / 16)
    return n


print('Введи 2 шесьнадцатиричных числа.')
num = input('Первое число: ')
f_num = []
for i in num:
    f_num.append(i.lower())
f_num.reverse()

num = input('Второе число: ')
s_num = []
for i in num:
    s_num.append(i.lower())
s_num.reverse()

sum_ = from_hex_to_ten(f_num) + from_hex_to_ten(s_num)
mult_ = from_hex_to_ten(f_num) * from_hex_to_ten(s_num)

print(f'Сумма равна: {from_ten_to_hex(sum_)}')
print(f'Произведение равно: {from_ten_to_hex(mult_)}')



