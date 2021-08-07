# 4. Определить, какое число в массиве встречается чаще всего.

# Если в массиве встретится два числа с одинаковым количеством встреч, то отобразится находящееся раньше
import random

a = [random.randint(0, 100) for i in range(50)]
print(a)
max_count = 0
for i in range(len(a)):
    count = 0
    b = a[i]
    for n in range(len(a)):
        if a[n] == b:
            count += 1
    if count > max_count:
        max_count = count
        max_num = b
print(max_num, max_count)
