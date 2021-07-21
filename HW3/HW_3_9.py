# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

N = 4
M = 5
a = []
c = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 11))
    min_num = None
    for m in b:
        if min_num is None:
            min_num = m
        elif m < min_num:
            min_num = m
    c.append(min_num)
    a.append(b)

for x in a:
    print(('{:4d}' * M).format(*x))

max_num = None
for z in c:
    if max_num is None:
        max_num = z
    elif z > max_num:
        max_num = z
print(f'Массив минимумов {c}')
print(f'Максимальное значение из минимумов {max_num}')

