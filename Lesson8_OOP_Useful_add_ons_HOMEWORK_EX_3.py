class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OwnError1(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
while True:
    num_ = input('Введите число для заполнения списка, для прекращения нажмите Q').lower()
    try:
        if num_ == 'q':
            raise OwnError1(f'Действие программы завершено, вот текущий список: {num_list}')
        if not num_.isdigit():
            raise OwnError('Нужно ввести числовое значение')
    except(ValueError, OwnError) as err:
        print(err)
    except (ValueError, OwnError1) as err1:
        print(err1)
        break
    else:
        num_list.append(int(num_))
        print(f'Все прошло удачно, вот текущий список: {num_list}')
