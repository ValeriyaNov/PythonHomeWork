# 3 Задайте список из n чисел последовательности 
# (1 + 1 / n)**n и выведите на экран их сумму.

print('Введите число', sep=' ')
n = int(input())
lst = []
for i in range(n):
    lst.append(round((1 + 1 / (i + 1)) ** (i + 1), 4))


def sum_elements (lst1):
    sum = 0
    for i in range(len(lst1)):
        sum = sum + lst1[i]
    return sum


print(f'Список: {lst}')
sum1 = sum_elements (lst)
print (f'Сумма элементов списка = {sum1}')


