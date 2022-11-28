# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

print('Введите N = ')
n = int(input())


def full_list(N):
    import random
    lst = []
    for i in range(N):
        lst.append(random.randint(-N, N))
    return lst


array = full_list(n)
print(array, '\t')


def replace_list(lst):
    for i in range(len(lst) - 1):
        if i == 0:
            temp = lst[i]
            lst[i] = lst[len(lst) - 1]
            lst[len(lst) - 1] = temp
        elif i == (len(lst) - 1) / 2:
            temp = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = temp
        else:
            temp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = temp

    return lst


def random_replace_list(lst):
    import random
    for i in range(n - 1):
        index = random.randint(0, n - 1)
        temp = lst[i]
        lst[i] = lst[index]
        lst[index] = temp
    return lst


new_array = replace_list(array)
print(new_array, '\t')
other_new_array = random_replace_list(array)
print(array, '\t')


