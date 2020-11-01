numbers_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(numbers_list)
numbers_list_1 = [number for number in numbers_list if numbers_list.count(number) < 2]
print(numbers_list_1)
