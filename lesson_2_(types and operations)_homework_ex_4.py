words = input('Введите несколько слов, разделив их пробелами :')
words = words.split(" ")
for i in range(0, len(words)):
    if len(words[i]) > 10:
        words[i] = (words[i][:10])
    print(f'{i + 1} : {words[i]}')
