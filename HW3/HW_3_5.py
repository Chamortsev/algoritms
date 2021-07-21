# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import random
a = 0
n = []
for i in range(10):
    n.append(int(random() * 10) - 5)
print(n)
for i in range(len(n)):
    if n[i] < a:
        a = n[i]
        b = i
print(f'Индекс {b}, Значение {a}')
