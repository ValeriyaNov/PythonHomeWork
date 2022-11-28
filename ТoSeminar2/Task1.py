#1 Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

print('Введите число = ')
number = abs(float(input()))
while (number % 1) != 0:
    number = number * 10
sum = 0
while number > 0:
    sum = sum + (number % 10)
    number = number // 10
print(f'Сумма цифр = {int(sum)}')




