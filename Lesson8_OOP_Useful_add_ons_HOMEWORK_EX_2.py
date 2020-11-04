class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input('Введите число, которое хотите поделить')
inp_data_1 = input('Введите число, на которое хотите поделить')
try:
    inp_data = int(inp_data)
    inp_data_1 = int(inp_data_1)
    if inp_data_1 == 0:
        raise OwnError('Деление на ноль невозможно')
except (ZeroDivisionError, OwnError) as err:
    print(err)
except ValueError:
    print('Введите числовое значение')
else:
    print(f"Все хорошо. результат вашего деления: {inp_data / inp_data_1}")
