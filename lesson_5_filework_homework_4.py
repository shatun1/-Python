russian_numbers = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
result = []
new_file = open('my_file_4', 'r+', encoding='utf-8')
for line in new_file:
    word_1 = line.split()
    # print(word_1)
    if word_1[0] in russian_numbers:
        word = russian_numbers[word_1[0]]
        result.append(f'{word} - {word_1[2]}\n')
# print(result)
new_file_1 = open('my_file_4_1', 'r+', encoding='utf-8')
new_file_1.writelines(result)
