# Вывести коды символов ASCII c 23-го по 127 включительно.
# По 10 пар в строке.

START = 32
END = 127

for i in range(START, END + 1):
    if ((i - START) % 10) == 0 and i != START:
        print('\n')

    print(f'{i} == {chr(i)}', end=' ')


