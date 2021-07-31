# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


# Решение в лоб
# a = input('Введите первое число в шестнадцатиричном исчислении: ')
# b = input('Введите второе число в шестнадцатиричном исчислении')


a = 'A2'
b = 'C4F'
a_list = list(a)
b_list = list(b)

s1 = hex(int(a, 16) + int(b, 16))
s2 = hex(int(a, 16) * int(b, 16))
print(f"Сумма чисел {a} и {b}: {s1}")
print(f"Произведение чисел {a} и {b}: {s2}")


# Вариант 2 Увы пока не успел реализовать, но тем не менее постараюсь его реализовать.
'''
slovar = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

len_a = len(a_list)
len_b = len(b_list)
if len_b > len_a:
    max_len = len_b
    min_len = len_a
    max_list = b_list
    min_list = a_list
else:
    max_len = len_a
    min_len = len_b
    max_list = a_list
    min_list = b_list

i = max_len - 1
z = min_len - 1
num1 = ''
num2 = ''

for _ in max_list:
    # num1 += str(slovar[max_list[i]])
    print(slovar[_])
    num1 += str(slovar[_])
print(num1)


for _ in min_list:
    # num1 += str(slovar[max_list[i]])
    print(slovar[_])
    num2 += str(slovar[_])
print(num2)

print(int(num1)+int(num2))

'''

'''
while i >= 0:
    print(max_list, i, bin(slovar[max_list[i]]))
    num1 += str(slovar[max_list[i]])
    i -= 1

while z >= 0:
    print(z, bin(slovar[min_list[z]]))
    num2 += str(slovar[min_list[z]])
    z -= 1
print('one',num1)
print('two',num2)
print('3', hex(int(num1+num2)))
'''
