def func_1(num_1, num_2):
    try:
        division = num_1 / num_2
        return division
    except ZeroDivisionError:
        print('Слушай, я конечно понимаю, что в PYTHONe всё можно, но ноль так не считает')


print(func_1(int(input('Введите первое число :')), int(input('Введите второе число :'))))
