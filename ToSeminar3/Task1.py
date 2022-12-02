# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на 
# нечётной позиции.


print('Введите элемент ')
restart = ''
lst = []
while restart == '':
    lst.append(int(input()))
    restart = input('Рестарт?')
print(lst)


def sum_odd_index (array):
    sum = 0
    for i in range(1, len(array), 2):
        sum = sum + array[i]
    return sum


print(f'Сумма элементов, находящихся на нечетных позициях = {sum_odd_index(lst)}')