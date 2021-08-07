# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random
a = [random.randint(-100, 100) for i in range(15)]
b = a
print(f'Массив до сортировки {a}')


def sort1(array: iter):
    count = 1
    while count < len(array):
        for itm in range(len(array) - count):
            if array[itm] < array[itm + 1]:
                array[itm], array[itm + 1] = array[itm + 1], array[itm]
        count += 1
    return array


def sort2(lst):
    n = 1
    while n < len(lst):
        count = 0
        for i in range(len(lst) - 1 - (n - 1)):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
        if count == 0:
            break
        n += 1
    return lst


print(f'Вариант сортировки 1 {sort1(b)}')
print(f'Вариант сортировки 2 {sort2(a)}')