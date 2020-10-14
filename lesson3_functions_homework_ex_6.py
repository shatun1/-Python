def right_words():
    words = 'I gulay s собакой'
    words = words.split()
    good_letter = []
    good_word = []
    def right_letter(words):
        for word in words:
            for letter in word:
                if ord(letter) in range(96, 123):
                    good_word.append(word)
        return good_word
    return right_letter(words)
a = right_words()
a = str(a)
a = a.title()
print(a)
