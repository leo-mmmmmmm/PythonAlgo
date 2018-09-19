# Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib
# или встроенной в python функцией hash().

from hashlib import sha1


def get_h_substring(string, len_str):
    substr = {}

    for i in range(len_str):
        for j in range(i + 1, len_str + 1 if i != 0 else len_str):
            if string[i:j] not in substr:
                substr[string[i:j]] = 0

    return substr


def count_substrings(string, substrings):

    len_ = len(string)

    for key in substrings:
        for i in range(len_):
            for j in range(i + 1, len_ + 1):
                if sha1(key.encode('utf-8')).hexdigest() == sha1(string[i:j].encode('utf-8')).hexdigest():
                    substrings[key] += 1

    return substrings


user_string = input('Введите встроку: ')
len_s = len(user_string)

sub_s = get_h_substring(user_string, len_s)

sub_s = count_substrings(user_string, sub_s)

print(sub_s)

