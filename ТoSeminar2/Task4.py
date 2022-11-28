# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

print('Введите N = ')
n = int(input())


def full_list(N):
    import random
    lst = []
    for i in range(N):
        lst.append(random.randint(-N, N))
    return lst


array = full_list(n)
print(array)
print('Введите позицию первого элемента')
index1 = int(input())
print('Введите позицию второго элемента')
index2 = int(input())
print(f'Произведение элементов = {array[index1] * array[index2]}')






