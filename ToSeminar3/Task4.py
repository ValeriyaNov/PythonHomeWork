# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

print('Введите число = ')
number = int(input())


def conver_dec_to_bin(digit):
    n = []
    while digit > 0:
        n.append(str(digit % 2))
        digit //= 2
    print('Данное число в двоичной системе = ', ''.join(n[::-1]))


conver_dec_to_bin(number)

