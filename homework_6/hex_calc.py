# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

import sys

MEMORY_EATEN = 0

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
MEMORY_EATEN += sys.getsizeof(HEX_DICT)
TEN_DICT = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}
MEMORY_EATEN += sys.getsizeof(TEN_DICT)


def from_hex_to_ten(mas, memory=0):
    num = 0
    for i in range(len(mas)):
        num = num + HEX_DICT[mas[i]] * (16 ** i)
    memory += sys.getsizeof(i)
    memory += sys.getsizeof(num)
    return num, memory


def from_ten_to_hex(num, memory=0):
    n = ''
    while num > 0:
        y = str(num % 16)
        if y in TEN_DICT:
            n = TEN_DICT[y] + n
            n = y + n
        num = int(num / 16)
    memory += sys.getsizeof(y)
    memory += sys.getsizeof(n)
    memory += sys.getsizeof(num)
    return n, memory


print('Введи 2 шесьнадцатиричных числа.')
num = input('Первое число: ')
f_num = []
for i in num:
    f_num.append(i.lower())
f_num.reverse()

MEMORY_EATEN += sys.getsizeof(f_num)

num = input('Второе число: ')
s_num = []
for i in num:
    s_num.append(i.lower())
s_num.reverse()

MEMORY_EATEN += sys.getsizeof(f_num)
MEMORY_EATEN += sys.getsizeof(num)

sum_ = 0
mult_ = 0

sum_ += from_hex_to_ten(f_num)[0]
sum_ += from_hex_to_ten(s_num)[0]
mult_ += from_hex_to_ten(f_num)[0]
mult_ *= from_hex_to_ten(s_num)[0]

MEMORY_EATEN += from_hex_to_ten(f_num)[1]
MEMORY_EATEN += from_hex_to_ten(s_num)[1]
MEMORY_EATEN += from_hex_to_ten(f_num)[1]
MEMORY_EATEN += from_hex_to_ten(s_num)[1]

MEMORY_EATEN += sys.getsizeof(sum_)
MEMORY_EATEN += sys.getsizeof(mult_)

print(f'Сумма равна: {from_ten_to_hex(sum_)}')
print(f'Произведение равно: {from_ten_to_hex(mult_)}')
print(f'Всего было съедено {MEMORY_EATEN} байт')



