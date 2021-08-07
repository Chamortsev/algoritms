# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random

m = random.randint(5, 15)
size = 2 * m + 1
my_array = [random.randint(0, 50) for _ in range(size)]


def median(lst, first, last):
    ind = len(lst) // 2
    if first >= last:
        return lst[ind]
    a = lst[ind]
    i = first
    j = last
    while i <= j:
        while lst[i] < a:
            i += 1
        while lst[j] > a:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    if ind < i:
        lst[ind] = median(lst, first, j)
    elif j < ind:
        lst[ind] = median(lst, i, last)
    return lst[ind]


def merge_sort(arr):
    def merge(fst, snd):
        res = []
        i, j = 0, 0
        while i < len(fst) and j < len(snd):
            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1
            else:
                res.append(snd[j])
                j += 1
        res.extend(fst[i:] if i < len(fst) else snd[j:])
        return res

    def div_half(lst):
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))
    return div_half(arr)


print(f'2*{m}+1 массив состоит из {size}  элементов:', my_array, sep='\n')
print(f'Медиана в массиве равна {median(my_array, 0, len(my_array) - 1)}')
print('Результат отсортированного массива: ', merge_sort(my_array), sep='\n')
