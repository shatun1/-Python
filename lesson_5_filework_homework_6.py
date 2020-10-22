new_file = open('my_file_6.txt', 'r', encoding='utf-8')
finaly_dict = {}
content = new_file.readlines()
for line in content:
    line = line.split()
    for word in line:
        word = word.replace('(лаб)', ' ')
        word = word.replace('(лекц)', ' ')
        word = word.replace('(пр)', ' ')
        line = line.replace(':', ' ')
        word = word.split()
        name = line[0]
        numbers = [int(el) for el in word if el.isdigit()]
        finaly_dict.update({name: sum(numbers)})
print(finaly_dict)
