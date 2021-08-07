# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def my_sort(my_array):
    if len(my_array) < 2:
        return my_array
    a = len(my_array) // 2
    left = my_sort(my_array[:a])
    right = my_sort(my_array[a:])
    return my_list(left, right)


def my_list(ml_1, ml_2):
    result = []
    i = 0
    j = 0
    while i < len(ml_1) and j < len(ml_2):
        if ml_1[i] <= ml_2[j]:
            result.append(ml_1[i])
            i += 1
        else:
            result.append(ml_2[j])
            j += 1
    result += ml_1[i:]
    result += ml_2[j:]
    return result


numbers = [random.uniform(0, 50) for _ in range(15)]
print(numbers)
print(my_sort(numbers))
