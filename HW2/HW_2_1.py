"""1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""


while True:
    try:
        a = int(input('Введите первое число: '))
        c = input('Введите необходимую операцию (*,/,+,-) или 0 для выхода из программы: ')
        if c == '0':
            break
        b = int(input('Введите второе число: '))
    except ValueError:
        print('Ошибка в воде данных!')

    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        try:
            result = a / b
        except ZeroDivisionError:
            print('Деление на 0 ')
    print(f'{a} {c} {b} = {result}')
