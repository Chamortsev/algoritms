"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
# Вариант 1
n = int(input('Введите n: '))
a = 0
for i in range(1, n + 1):
    a = a + i

print(f'результат последовательного сложения: {a}')
print(f'результат работы  формулы  n(n+1)/2 : {int(n * (n + 1) / 2)}')
if a == n * (n + 1) / 2:
    print('Значения равны')

# Вариант 2
# n = int(input('Введите n: '))


def my_count(n):
    if n == 1:
        return n
    else:
        return n + my_count(n - 1)


i = 1
while i != n:
    if my_count(i) == i * (i + 1) / 2:
        print(f'1+2+...+n = {my_count(i)} ')
        print(f'n(n+1)/2  = {int(i * (i + 1) / 2)}')
        print(f'{my_count(i)} = {int(i * (i + 1) / 2)}')
    else:
        print(f'Ошибка для {i}')
        break
    i += 1
