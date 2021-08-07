# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
import sys
result = 0
min_num = 1000
max_num = 0
a = [random.randint(0, 100) for i in range(10)]
print(a)
for b in range(len(a)):
    if a[b] > max_num:
        max_num = a[b]
        max_ind = b
    elif a[b] < min_num:
        min_num = a[b]
        min_ind = b
if max_ind < min_ind:
    tmp = min_ind
    min_ind = max_ind
    max_ind = tmp
elem_1 = min_ind
elem_2 = max_ind
if max_ind-1 == min_ind:
    print(f'Элементы находятся рядом друг с другом  {elem_1}, {elem_2}, результат {result}')
    sys.exit()
min_ind += 1
while min_ind != max_ind:
    result = result + a[min_ind]
    min_ind += 1
print(f'Минимальный и максимальный индекс {elem_1}, {elem_2}, сумма элементов между этими индексами {result}')