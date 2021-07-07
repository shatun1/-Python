def max_number(arg_1, arg_2, arg_3):
    list_numbers = [arg_1, arg_2, arg_3]
    min_number = min(list_numbers)
    list_numbers.pop(min_number)
    return list_numbers


print(max_number(3, 1, 2))
