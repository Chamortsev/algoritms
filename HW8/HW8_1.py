# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import hashlib


def under_string(inp):
    u_input = str(inp).lower()
    inp_len = len(u_input)
    hash_set = set()
    for i in range(inp_len + 1):
        for j in range(i + 1, inp_len + 1):
            h = hashlib.sha1(u_input[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)
    return len(hash_set)
inp_len = 'hello my friend'
print(f'К-во подстрок в строке {inp_len}: {under_string(inp_len)}')
