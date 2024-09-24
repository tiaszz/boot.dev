def word_count_aggregator():
    count = 0
    def doc_builder(doc):
        nonlocal count
        word_count = len(doc.split())
        count += word_count
        return count

    return doc_builder

