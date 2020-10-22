numbers_set = [7, 5, 2, 2, 1]
user_number = int(input('Введите новый элемент рейтинга в виде числа от 1 до 10(Для выхода введите 11)'))
while user_number != 11:
    for i in range(len(numbers_set)):
        if user_number == numbers_set[i]:
            numbers_set.insert(i + 1, user_number)
            break
        elif user_number < numbers_set[-1]:
            numbers_set.append(user_number)
        elif user_number > numbers_set[0]:
            numbers_set.insert(0, user_number)
        elif numbers_set[i] > user_number and user_number > numbers_set[i + 1]:
            numbers_set.insert(i + 1, user_number)
    print(f'Текущий рейтинг - {numbers_set}')
    user_number = int(input("Введите число "))
