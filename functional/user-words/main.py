def user_words(initial_words):
    words_copy = list(initial_words)
    def add_word(word):
        words_copy.append(word)
        return tuple(words_copy)
    return add_word


