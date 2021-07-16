# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def middle_num():
    a, b, c = map(int, input('Введите три числа: ').split())

    if b > a > c or c > a > b:
        result = a
    elif a > b > c or c > b > a:
        result = b
    elif a > c > b or a > c > b:
        result = c
    else:
        result ='вычислить не возможно'
    print(f'Среднее число: {result}')
middle_num()
