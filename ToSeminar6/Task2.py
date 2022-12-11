# 4 Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

print('Введите степень многочлена k =')
k = int(input())

import random
list_coefficient = [random.randint(0, 101) for x in range(k + 1)]  # я так создавала список
print(list_coefficient)


def full_equation(lst, n):
    array = []
    for i  in range(len(lst)):
       array.append(f'{lst[i]}*x^{n-i}')
       
    return array
        
beautiful_lst1 = ' + '.join(full_equation(list_coefficient, k))    
print(beautiful_lst1)

path = 'File1.txt'
file = open(path, 'w')
file.write(beautiful_lst1)
file.close()
