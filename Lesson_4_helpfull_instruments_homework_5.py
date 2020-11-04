from functools import reduce
def my_f(numbers_1, numbers_2):
    return numbers_1 * numbers_2
numbers_list = [number for number in range(100, 1000) if number % 2 == 0]
print(reduce(my_f, numbers_list))
