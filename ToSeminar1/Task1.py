# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

print("Введите число  ")
date = int(input())
if date<1 or date>7:
    print("Некорректный ввод")
    exit()
if date>5:
    print("Выходной")
else:
    print("Не выходной")
