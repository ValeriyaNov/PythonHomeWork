# Задача, если бот настроен на выигрыш

from random import randint
max_step = 28


def input_dat():
    x = int(input(f'введите количество конфет от 1 до {max_step}   '))
    while x < 1 or x > max_step:
        x = int(input('некорректный ввод, попробуйте снова   '))
    return x


def p_print(k, value):
    print(f'вы взяли {k}, осталось {value} конфет')


value = int(input("Введите количество конфет на столе: "))
count = 1

while value > 28:
    if count % 2 != 0 :
        k = input_dat()
        value -= k
        flag = False
        p_print(k, value)
        count = count + 1
    else:
        if k < max_step:
            k = min(value, max_step - k)
            value -= k
        elif k == 28:
            l = value % max_step
            if l!= 0:
                k = l
            else: k = randint(1, k)
        count = count + 1    
        print(f'бот взял {k} конфет, осталось {value} конфет')

if count % 2 != 0:
    print('Вы выиграли')
else:
    print('Вы проиграли')