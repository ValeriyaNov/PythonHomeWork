# Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй 
# и предпоследний и т.д.

'''
Раньше просто задала список 
lst = [0, 2, 2.3, -4, 5, 6]
Сейчас решила вручную задать
'''
print('Введите элементы списка через пробел   ')
lst = list(map (int, input().split( )))


def multiplication_pair_number(array):
    array_mult = []
    for i in range((len(array) + 1) // 2):
        array_mult.append(array[i] * array[len(array) - 1 - i])
    return array_mult


lst_mult = multiplication_pair_number(lst)
print(f'Произведение пар элементов = {lst_mult}')
