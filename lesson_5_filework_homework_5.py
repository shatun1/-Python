new_file = open('my_file_5.txt', 'w+', encoding='utf-8')
new_file.write(input('Введите числа, которые нужно посчитать'))
new_file.seek(0)
sum_numbers = []
for line in new_file:
    line = line.split()
    for number in line:
        number = int(number)
        sum_numbers.append(number)
print(sum(sum_numbers))
