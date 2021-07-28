# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

from random import random

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        user_input = int(input(f'Введите значение ячейки  {i + 1}x{j + 1}: '))
        b.append(user_input)
    b.append(sum(b))
    a.append(b)

for x in a:
    print(('{:4d}' * (M + 1)).format(*x))
