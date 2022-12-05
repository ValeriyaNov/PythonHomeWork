# 3 Задайте последовательность чисел. Напишите 
# программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

import random
lst=[(random.randint(0, 100)) for x in range(11)]
print(lst)


def unrepit_number(array):
    new_lst = []
    count = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array [i] == array[j]:
                count += 1   
        if count == 1:
            new_lst.append(array[i])
        count = 0
    return new_lst


print(unrepit_number(lst))


