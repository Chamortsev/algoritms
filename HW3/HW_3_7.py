# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

a = [random.randint(0, 10) for i in range(10)]
min_num_1 = 0
min_num_2 = 0
for i in a:
    if a[min_num_1] > i:
        min_num_2 = min_num_1
        min_num_1 = a.index(i)
    elif a[min_num_2] > i:
        min_num_2 = a.index(i)
print(a)
print(f'Первый наименьший элемент {a[min_num_1]} второй наименьший элемент {a[min_num_2]}')
