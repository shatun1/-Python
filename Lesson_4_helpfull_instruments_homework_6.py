from sys import argv
from itertools import count, cycle
script_name, begin_number = argv
begin_number = int(begin_number)
numbers_list = []
number = None
n = 0
for number in count(begin_number):
    numbers_list.append(number)
    if number > 15:
        print(numbers_list)
        for el in cycle(numbers_list):
            print(el)
            n += 1
            if n >= len(numbers_list):
                raise StopIteration
