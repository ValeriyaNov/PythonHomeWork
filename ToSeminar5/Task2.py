# 2 Создайте программу для игры с конфетами человек против человека.

from random import randint
max_step = 28
def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > max_step:
        x = int(input(f"{name}, ввод некорректный, попробуйте снова: "))
    return x


def p_print(name, k, value):
    print(f"Ходил(а) {name}, он взял(а) {k}. Осталось на столе {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2)
if flag:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")

while value > 1:
    if flag:
        k = input_dat(player1)
        value -= k
        flag = False
        p_print(player1, k, value)
    else:
        k = input_dat(player2)
        value -= k
        flag = True
        p_print(player2, k, value)

if flag:
    print(f"Выиграл(а) {player1}")
else:
    print(f"Выиграл(а) {player2}")
