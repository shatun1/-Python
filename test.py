new_file = open('my_file_6.txt', 'r', encoding='utf-8')
finaly_dict = {}
for line in new_file.readlines():
    line = line.replace('(лаб)', ' ')
    line = line.replace('(лекц)', ' ')
    line = line.replace('(пр)', ' ')
    line = line.replace(':', ' ')
    line = line.split()
    name = line[0]
    hours_in_lesson = [int(el) for el in line if el.isdigit()]
    finaly_dict.update({name: sum(hours_in_lesson)})
print(finaly_dict)
