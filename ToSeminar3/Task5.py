# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

memory = {1:1, 2:1}
print('Введите число = ')
number = int(input())


def fib_positive_number(number_positive):
    if number_positive not in memory:
        memory[number_positive] = fib_positive_number(number_positive - 1) + \
                        fib_positive_number(number_positive - 2)
    return memory[number_positive]


def fib_negative_number(number_negative):
    memory[number_negative] = ((-1) ** (number_negative + 1)) * \
                        fib_positive_number(abs(number_negative))
    return memory[number_negative]
    
    
if number > 0:
    print(f'F(number) = {fib_positive_number(number)}')
elif number == 0:
    print('F(number) = 0')
else:
    print(f'F(number) = {fib_negative_number(number)}')