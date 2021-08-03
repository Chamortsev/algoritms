# 1.Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

import platform
from sys import getsizeof as gs, exit
# Узнаем разрядность платформы
print(platform.architecture())

# Первый вариант
a = input('Введите трехзначное число: ')

b = int(a[0])
c = int(a[1])
d = int(a[2])

sum_numbers = b + c + d
multipl_numbers = b * c * d


print(sum_numbers, multipl_numbers)
print(f'В программе задействовано байт памяти: {gs(a) + gs(b) + gs(c) + gs(d) + gs(sum_numbers) + gs(multipl_numbers)}')

# Python 3.9.5
# ('64bit', 'WindowsPE')
# Введите трехзначное число: 999
# 27 729
# В программе задействовано байт памяти: 192

# Второй вариант


def num_info():
    while True:
        num = int(input('Введите трехзначное число: '))
        sizea = gs(num)
        if len(str(num)) == 3:
            a = num % 10
            size2 = gs(a)
            num = num // 10
            size3 = gs(num)
            b = num % 10
            size4 = gs(b)
            num = num // 10
            size5 = gs(num)
            c = num % 10
            size6 = gs(c)
            result = c + b + a, c * b * a
            size7 = gs(result)
            print(result)
            print(f'В программе задействовано байт памяти: {sizea+size2+size3+size4+size5+size6+size7}')
            exit()
        else:
            print('вы ввели не трех значное число')


num_info()
# Python 3.9.5
# ('64bit', 'WindowsPE')
# Введите трехзначное число: 999
# 27 729
# В программе задействовано байт памяти: 224
