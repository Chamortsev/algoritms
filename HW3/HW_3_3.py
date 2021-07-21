# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(0, 20) for i in range(10)]
print(f'Начальный массив: {a}')
minimum = a[0]
max_index = 0
maximum = a[0]
min_index = 0

for i in range(len(a)):
    if a[i] < minimum:
        minimum = a[i]
        min_index = i
    elif a[i] > maximum:
        maximum = a[i]
        max_index = i
print(f' Максимум в массиве: {maximum}, Минимум в массиве: {minimum}')
a[min_index] = maximum
a[max_index] = minimum
print(f'Результат массива {a}')
