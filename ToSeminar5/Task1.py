# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
# данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

data1 = open('Data_input.txt', 'r')
sent = data1.read()
data1.close()


def compres_data(sentence):
    array = list(''.join(sentence))
    count = 1
    array1 = []
    for i in range(len(array) - 1):
        if array[i] == array[i + 1] :
            count = count + 1
        else:
            if count > 9 :
                array1.append(f'{9}{array[i]}')
                array1.append(f'{count-9}{array[i]}')
            else:
                array1.append(f'{count}{array[i]}')
                index = i
            count = 1
    if count > 1 or (array[len(array) - 2] != array[-1]): 
        array1.append(f'{count}{array[-1]}')
    array1 = ''.join(array1)
    return array1


def recovery_data(array2):
    array2 = list(''.join(array2))
    recov_array = []
    for i in range(0, len(array2), 2):
        recov_array.append(int(array2[i])*array2[i+1])
    recov_array = ''.join(recov_array)
    return recov_array


with open('Data_output.txt','w',encoding='UTF-8') as outputdata:
    outputdata.write(compres_data(sent)+"\n")
    outputdata.write(recovery_data(compres_data(sent)))