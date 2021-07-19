"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""


def find_num():
    import random
    import sys

    a = random.randrange(0, 100)
    i = 10
    while i != 0:
        b = int(input('Введите число: '))
        if b == a:
            print('Победа! Вы угадали!')
            sys.exit()
        elif b > a and i != 1:
            print(f'Ваше число больше загаданного. У вас осталось {i-1} попыток')
        elif b < a and i != 1:
            print(f'Ваше число меньше загаданного. У вас осталось {i-1} попыток')
        i -= 1
    print(f'Вы проиграли, загадано было число {a}')


find_num()