# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def find_letter():
    a = int(input('Введите номер буквы латинского алфавита от a до z где a=1 z=26: ').lower())
    print( f' Ваша буква: {chr(a+ord("a")-1)}')

find_letter()
