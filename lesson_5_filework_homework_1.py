new_file = open('my_file_1.txt', 'r+', encoding='utf-8')
while True:
    control = input('Если вы хотите продолжить - нажмите enter, если нет - нажмите q').upper()
    if control == 'Q':
        break
    new_file.write(f"{input('Введите текст, который вы хотите записать')} \n")
    for line in new_file:
        new_file.seek(2)
new_file.close()
