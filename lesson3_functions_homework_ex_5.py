def sum_of_sum():
    '''Функция принимает числа, далее проверяет строку на наличие строчных чисел и преобразует их в обычные. Так же
    присутсвует временный список, который хранит в себе числа введенные пользователем для подсчета первичной суммы.'''
    numbers_ = []
    numbers_time = []
    n = None
    while n != 'q':
        numbers = input('Введите числа через пробел :').split()
        print(numbers)
        for n in numbers:
            if n.isdigit():
                n = int(n)
                numbers_time.append(n)
                numbers_.append(n)
                sum_ = sum(numbers_)
                sum_time = sum(numbers_time)
            if n == 'q':
                print(f'Сумма всех чисел - {sum_}')
                break
        print(f'{sum_time}, {sum_}')
        numbers_time = []


sum_of_sum()
