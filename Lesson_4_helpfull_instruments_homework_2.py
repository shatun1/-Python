import random
first_list = [random.randrange(1, 101) for i in range(10)]
print(first_list)
n = 1
second_list = [first_list[n] for n in range(n, len(first_list)) if first_list[n] > first_list[n - 1]]
print(second_list)
