new_file = open('my_file_3.txt', 'r+', encoding='utf-8')
salary = []
for line in new_file:
    line = line.split()
    # print(line)
    for letter in line:
        # print(letter)
        if letter.isdigit():
            # print(letter)
            letter = int(letter)
            if letter < 20000:
                salary.append(letter)
                print(line[1])
salary = sum(salary)
print(salary)
new_file.close()
