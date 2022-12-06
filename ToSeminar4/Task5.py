'''
5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.
'''

data1 = open('File1.txt', 'r')
polynomial1 = data1.read()
data1.close()
print(polynomial1)

data2 = open('File2.txt', 'r')
polynomial2 = data2.read()
data2.close()
print(polynomial2)


def lst_full(poly):
    pol = poly.split('+')
    l1 = [x[x.find('^') +1:] for x in pol]
    l2 = [x[:x.find('*')] for x in pol]
    ll = tuple(zip(list(map(int, l1)), list(map(int, l2))))
    return ll


arr1 = lst_full(polynomial1)
arr2 = lst_full(polynomial2)
print(arr1)
if len(arr2) > len(arr1):
    arr1, arr2 = arr2, arr1
def lst_conv(tupll):
    arr = [0] * (int(tupll[0][0]) + 1)
    for i in range(0, len(tupll)):
        index = int(tupll[i][0])
        arr[index] = int(tupll[i][1])
        index == 0
    return arr


new_lst1 = lst_conv(arr1)
new_lst2 = lst_conv(arr2)
print(new_lst1)
print(new_lst2)
def sum_lst(array1, array2):
    sum_lst = []
    for i in range(len(array1)):
        if i < len(array2):
            sum_lst.append(array1[i]+array2[i])
        else:
            sum_lst.append(array1[i])
            
    return sum_lst

coef_sum = sum_lst(new_lst1, new_lst2)
coef_sum = coef_sum[::-1]
array = []
for i  in range(len(coef_sum)):
    array.append(f'{coef_sum[i]}*x^{len(coef_sum) - i - 1}')
beautiful_lst = ' + '.join(array)    


path = 'File.txt'
file = open(path, 'w')
file.write(beautiful_lst)
file.close()