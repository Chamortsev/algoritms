# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for i in range(2, 10):
    result = []
    for a in range(2, 100):
        if a % i == 0:
            result.append(a)
    my_len = len(result)
    print(f'Для числа {i}  кратных чисел {my_len} ')
