# Вычислить число π c заданной точностью d

print('Введите точность d = ')
d = float(input())


def calculation_pi_nilakant(accuracy):
    pi_finding = 3
    import math
    pi_reference = math.pi
    count = 2
    count_degree = 2
    while abs(pi_finding - pi_reference) > accuracy:
        pi_finding = pi_finding + (((-1) ** count_degree) * (4 / (count * (count + 1) * (count + 2))))
        count_degree += 1
        count += 2
    return pi_finding

print(f'Пи = {calculation_pi_nilakant(d)}')

