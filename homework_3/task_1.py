# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

mas = [i for i in range(2, 100)]
digits = [i for i in range(2, 10)]

count = 0

for j in digits:
    for i in mas:
        if i % j == 0:
            count += 1
    print(f'Числу {j} крастно {count} чисел.')
    count = 0





