def new_collection(initial_docs):
    lst_copy = initial_docs.copy()
    def append(doc):
        lst_copy.append(doc)         
        return lst_copy
    return append

