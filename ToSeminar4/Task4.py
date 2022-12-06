# 4 Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

print('Введите степень многочлена k =')
k = int(input())
print('Введите степень многочлена p =')
p = int(input())
import random
list_coefficient = [random.randint(0, 101) for x in range(k + 1)]
print(list_coefficient)
list_coefficient2 = [random.randint(-99, 101) for x in range(p+ 1)]
print(list_coefficient2)

def full_equation(lst, n):
    array = []
    for i  in range(len(lst)):
       array.append(f'{lst[i]}*x^{n-i}')
       
    return array
        
beautiful_lst1 = ' + '.join(full_equation(list_coefficient, k))    
print(beautiful_lst1)

beautiful_lst2 = ' + '.join(full_equation(list_coefficient2, p))    
print(beautiful_lst2)

path = 'File1.txt'
file = open(path, 'w')
file.write(beautiful_lst1)
file.close()

path = 'File2.txt'
file = open(path, 'w')
file.write(beautiful_lst2)
file.close()


# import os
# print (os.listdir(os.getcwd()))
