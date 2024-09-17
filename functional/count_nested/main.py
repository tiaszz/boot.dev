def count_nested_levels(nested_documents, target_document_id, level=1):
    if target_document_id in nested_documents:
        return level

    def check_document(doc):
        if isinstance(nested_documents[doc], dict):
            result = count_nested_levels(nested_documents[doc], target_document_id)
            if result != -1:
                return result + 1
        return None

    results = list(filter(lambda x: x is not None, map(check_document, nested_documents)))

    return results[0] if results else -1

