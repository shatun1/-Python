def generator():
    list_generator = input('Введите числа через пробел').split()
    for el in list_generator:
        el = float(el)
        fact_list = []
        fact = 1
        while el > 1:
            fact = fact * el
            el = el - 1
            if el == 0:
                fact = 1
        fact_list.append(fact)
        yield fact_list


for el in generator():
    print(el)
