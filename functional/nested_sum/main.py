def sum_nested_list(lst):
    if not lst:
        return 0
    
    first_element = lst[0]
    rest_sum = sum_nested_list(lst[1:])

    if isinstance(first_element, list):
        return sum_nested_list(first_element) + rest_sum
    else:
        return first_element + rest_sum

