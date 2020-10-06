proceeds = int(input('Введите размер вашей выручки : '))
costs = int(input('Введите размер издержек вашей компании :'))
profit = proceeds - costs
if proceeds > costs:
    print(f'Физма рентабильна , размер прибыли равен: {profit}')
elif proceeds == costs:
    print('Чтож, главное это стабильность, но вам есть куда стремиться!(Размер выручки равен размеру издержек)')
else:
    print(f'Фирма нерентабельна, размер убытков равен: ({profit})')
profitability = profit / proceeds
print(f'Рентабельность выручки составялет : {profitability}')
staff = int(input('Введите количество сотрудников вашей фирмы'))
profit_for_one_staff = int(profit / staff)
print(f'Прибыль на одного сотрудника составляет : {profit_for_one_staff} ')