"""4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на
экран любой символ алфавита от 'a' до 'f' включительно. """


def rand():
    import random
    import re

    err = "Вы где то допустили ошибку ввода. перепроверьте данные"
    try:
        input_from, input_to = [i for i in (input("Введите диапазон в формате (1 20 или a f): ").split())]
        # Проверяем ввод на буквы
        if input_from.isalpha() and input_to.isalpha():
            a = ord(input_from)
            b = ord(input_to)
            if a > b:
                result = chr(random.randint(b, a))
            else:
                result = chr(random.randint(a, b))
        # Проверяем ввод на целое число
        elif input_from.isdigit() and input_to.isdigit():
            a = int(input_from)
            b = int(input_to)
            if a > b:
                result = random.randint(b, a)
            else:
                result = random.randint(a, b)
        elif re.search(r'[/".]', input_from) and re.search(r'[/".]', input_to):
            try:
                a = float(input_from)
                b = float(input_to)
                if a > b:
                    result = random.uniform(b, a)
                else:
                    result = random.uniform(a, b)
            except ValueError:
                print(err)

        else:
            print(err)
        print(result)
    except ValueError:
        print(err)
    except UnboundLocalError:
        print(err)

rand()
