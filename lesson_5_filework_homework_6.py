new_file = open('my_file_6.txt', 'r+', encoding='utf-8')
finaly_dict = {}
content = new_file.readlines(1)
for line in content:
    numbers_1 = []
    line = line.split()
    for word in line:
        word = word.replace('(лаб)', ' ')
        word = word.replace('(лекц)', ' ')
        word = word.replace('(пр)', ' ')
        word = word.split()
        # print(word)
        for el in word:
            if el.isdigit():
                el = int(el)
                numbers_1.append(el)
    finaly_dict = finaly_dict(line[0], sum(numbers_1))
    print(finaly_dict)





