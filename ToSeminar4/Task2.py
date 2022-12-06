# 2 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

print('Введите число ')
num = int(input())


def Factorization(number):
    result = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            result.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        result.append(number)
    return result


print(f'При N = {num} - {Factorization(num)}')