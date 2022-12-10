# 1 Напишите программу, удаляющую из файла все слова, 
# содержащие "абв".
data1 = open('Text1.txt', 'r', encoding="utf-8")
sentence = data1.read()
data1.close()


res = " ".join(list(filter(lambda x: not 'абв' in x, sentence.split())))
print(res)

