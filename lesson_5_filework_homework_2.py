new_file = open('my_file_2.txt', 'r+', encoding='utf-8')
lines = 0
words = 0
letters = 0

for line in new_file:
    lines += 1
    letters += len(line)

    for letter in line:
        if letter != ' ':
            words += 1
print("Lines:", lines)
print("Words:", words)
new_file.close()
