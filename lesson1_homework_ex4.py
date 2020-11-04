number = int(input('Введите число'))
max_num = 0
while number != 0:
    number1 = number % 10
    if number1 > max_num:
        max_num = number1
    number = number // 10
print(f'Самое большое число {max_num}')
