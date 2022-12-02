# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

import random
array=[round(random.uniform(-99.999, 100), 3) for x in range(11)]
print(array)


def diff_max_min_fract(lst):
    new_lst = []
    for i in range(len(lst)):
        if (lst[i] % 1) == 0:
            continue
        new_lst.append(float(abs(lst[i]) - abs(int(lst[i]))))
    max = min = new_lst[0]
    for i in range(len(new_lst)):
        if new_lst[i] > max:
            max = new_lst[i]
        if new_lst[i] < min:
            min = new_lst[i]
    diff = max - min 
    return diff


print(diff_max_min_fract(array))




