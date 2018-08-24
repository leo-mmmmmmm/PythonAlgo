# Найти сумму и произведение цифр, введённого пользователем трёхзначного числа.

num = int(input('Введите трёъзначное число: '))

# Находим сумму цифр
summ = (num//100) + ((num//10) % 10) + (num % 10)
# Находим произведение цифр
proizv = (num//100) * ((num//10) % 10) * (num % 10)

print(f'Сумма цифр = {summ}')
print(f'Произведение цифр = {proizv}')
