# Доказать, что
# 1+2+3+...+n = n*(n+1)/2,
# для любого натурального n.


def summ_ar(n):
    return int(n*(n+1)/2)

n = int(input('Докажем, что \n'
              '1+2+3+...+n = n*(n+1)/2,\n'
              'для любого натурального n.\n'
              'Введи n: '))

total = 0

for i in range(1, n+1):
    total += i

if total == summ_ar(n):
    print('Красота!!!\n'
          f'{total} == {summ_ar(n)}')
else:
    print('Что-то пошло не так...\n'
          f'{total} != {summ_ar(n)}')



