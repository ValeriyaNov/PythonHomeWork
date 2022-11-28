# 2 Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

print('Введите N = ')
N = input()
if N.isdigit():
    N = int(N)
else:
    print('Ошибка')
    exit()
p = 1
for i in range(1, N + 1):
    if i < N + 1:
        p = p * i
        print(p, end=', ')

