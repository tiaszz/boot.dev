def count_nested_levels(nested_documents, target_document_id, level=1):
    if target_document_id in nested_documents:
        return level
    
    max_depth = -1

    for key, value in nested_documents.items():
        if isinstance(value, dict):
            depth = count_nested_levels(value, target_document_id, level + 1)
                if depth != -1:
                max_depth = max(max_depth, depth)

    return max_depth if max_depth != -1 else -1

