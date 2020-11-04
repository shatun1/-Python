# user_input = input('Введите несколько символов')
# print(user_input[::2])
# user_input = list(user_input)
# for i in range(0, len(user_input), 2):
#     user_input[i], user_input[i -1] = user_input[i-1], user_input[i]
#     print(' '.join([str(i) for i in user_input]))

user_input = input('Введите несколько символов')
user_input = list(user_input)
finaly_index = len(user_input) if len(user_input) % 2 == 0 else len(user_input) - 1
for i in range(0, finaly_index - 1, 2):
    user_input[i], user_input[i + 1] = user_input[i + 1], user_input[i]
print(user_input)
