# Эратосфен
# n = int(input("До какого числа считать простые числа: "))


# Сложность O(n)
def sieve_func(n):
    sieve = [i for i in range(n)]

    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2   # j = i + i

            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res
# 100 loops, best of 3: 19.7 usec per loop - 100
# 100 loops, best of 3: 240 usec per loop - 1000
# 100 loops, best of 3: 2.68 msec per loop - 10000


# Сложность O(n**2)
def slow_way(n):

    res = []
    k = 0

    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1

        if k == 0:
            res.append(i)
        else:
            k = 0

    return res
# 100 loops, best of 3: 231 usec per loop - 100
# 100 loops, best of 3: 23.7 msec per loop - 1000
# 1 loops, best of 3: 2.97 sec per loop
