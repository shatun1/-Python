def generator():
    list_generator = [num for num in range(1, 10)]
    for el in list_generator:
        fact_list = []
        fact = 1
        while el > 1:
            fact = fact * el
            el = el - 1
        fact_list.append(fact)
        yield fact_list


for el in generator():
    print(el)
