# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import random
import cProfile


def range_change():
    a = [random.randint(0, 1020) for i in range(1000)]
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


def range_change_v2():
    a = [random.randint(0, 1020) for i in range(1000)]
    a = sorted(a)
    a[0], a[len(a)-1] = a[len(a)-1], a[0]
    print(a[0], a[len(a)-1])
    print(a)


cProfile.run('range_change()')

cProfile.run('range_change_v2()')
# Вывод - если отсортировать массив с помошью sorted и затем заменить первый и последний элемент -
# то задача решается быстрее, но при этом нарушается первоначальный вид массива.
