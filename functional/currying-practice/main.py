def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_lenght(doc):
            count = 0
            doc_split = doc.split()
            for line in doc_split:
                if sequence in line:
                    count += 1
            return count

        return with_lenght

        # ?

    return with_char

