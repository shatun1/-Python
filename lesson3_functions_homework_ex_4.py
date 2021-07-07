def my_func(x, y):
    i = 0
    while i > y:
        if i < 0:
            power = power / x
            i -= 1
        else:
            power = 1 / x
            i -= 1
    return power


print(my_func(111, -100))
