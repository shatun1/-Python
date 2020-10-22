new_file = open('my_file_1.txt', 'r+', encoding='utf-8')
new_file.write(f"{input('Введите текст, который вы хотите записать')} \n")
for line in new_file:
    new_file.seek(2)
    break
new_file.close()
