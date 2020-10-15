def right_words(words):
    words = words.split()
    good_word = []
    def right_letter(words):
        for word in words:
            good_letter = []
            for letter in word:
                if ord(letter) in range(96, 123):
                    good_letter.append(letter)
                    if len(good_letter) == len(word):
                        good_word.append(word)
                        good_letter = []
        a = good_word
        a = str(a)
        a = print(a.title())
        return a
    return right_letter(words)


right_words(input('Введите слова на латинском и других языках ЧЕРЕЗ ПРОБЕЛ для сортировки : '))
