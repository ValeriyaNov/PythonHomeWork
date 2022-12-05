# 4 Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

print('Введите степень многочлена k =')
k = int(input())
import random
list_coefficient = [random.randint(0, 100) for x in range(k + 1)]
print(list_coefficient)


def full_equation(lst, n):
    for i  in range(len(lst)-1):
        print(f'{lst[i]}x^{n-i}', end=' + ')
    print(f'{lst[n]}')
    return ' '
        
    
print(full_equation(list_coefficient, k))

path = 'File1.txt'
file = open(path, 'w')
file.full_equation([1, 2, 5, 8], 3)
file.close()

import os
print (os.listdir(os.getcwd()))
