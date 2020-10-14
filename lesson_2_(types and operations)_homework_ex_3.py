######################################################################### Через dictionary
data_list = {1: 'winter', 2: 'spring', 3: 'wummer', 4: 'autumn'}
data_month = int(input('Введите месяц в виде целого числа от одного до двенадцати : '))
if data_month == 12 or data_month == 1 or data_month == 2:
    print(f'Сейчас {data_list[1]}')
if data_month == 3 or data_month == 4 or data_month == 5:
    print(f"Сейчас {data_list[2]}")
if data_month == 6 or data_month == 7 or data_month == 8:
    print(f'Сейчас {data_list[3]}')
if data_month == 9 or data_month == 10 or data_month == 11:
    print(f'Сейчас {data_list[4]}')

############################################################################### Через list
data_list_1 = ['winter', 'spring', 'summer', 'autumn']
data_month_1 = int(input('Введите месяц в виде целого числа от одного до двенадцати : '))
if data_month_1 == 12 or data_month_1 == 1 or data_month_1 == 2:
    print(f'Сейчас {data_list_1[0]}')
if data_month_1 == 3 or data_month_1 == 4 or data_month_1 == 5:
    print(f'Сейчас {data_list_1[1]}')
if data_month_1 == 6 or data_month_1 == 7 or data_month_1 == 8:
    print(f'Сейчас {data_list_1[2]}')
if data_month_1 == 9 or data_month_1 == 10 or data_month_1 == 11:
    print(f'Сейчас {data_list_1[3]}')
