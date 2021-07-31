"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""


def sum_num(num):
    summa = 0
    for a in num:
        summa += int(a)
    return summa


list_num = [i for i in input('Введите числа: ').split()]
max_num = 0
max_sum = 0
for i in list_num:
    if sum_num(i) > max_sum:
        max_num = i
        max_sum = sum_num(i)

print(f'Число {max_num} имеет максимальную сумму цифр - {max_sum}')
