""" 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
- проверить ввод, если длинна !=3 то повторить ввод
- если длинна == 3
- то  взять первый символ, сложить его со вторым и с третьим
- взять все символы и перемножить """

import sys


def num_info():
    while True:
        num = int(input('Введите трехзначное число: '))
        sizea = sys.getsizeof(num)
        if len(str(num)) == 3:
            a = num % 10
            size2 = sys.getsizeof(a)
            num = num // 10
            size3 = sys.getsizeof(num)
            b = num % 10
            size4 = sys.getsizeof(b)
            num = num // 10
            size5 = sys.getsizeof(num)
            c = num % 10
            size6 = sys.getsizeof(c)
            result = c + b + a, c * b * a
            size7 =sys.getsizeof(result)
            print(result)
            print(f'В программе задействовано байт памяти: {sizea+size2+size3+size4+size5+size6+size7}')
            sys.exit()
        else:
            print('вы ввели не трех значное число')



if __name__ == '__main__':
    # print(num_info())
    num_info()
