def find_longest_word(document, longest_word=""):
    document = document.strip()

    if not document:
        return longest_word

    try:
        words = document.split(maxsplit=1)
        print(words)
        first_word = words[0]
        rest_document = words[1] if len(words) > 1 else ""

    except IndexError:
        first_word = document
        rest_document = ""


    if len(first_word) > len(longest_word):
        longest_word = first_word

    return find_longest_word(rest_document, longest_word)

