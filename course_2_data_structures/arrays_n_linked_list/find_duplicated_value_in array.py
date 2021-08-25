def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    arr_len = len(arr)
    if arr_len > 2:
        unique_sum = (arr_len - 2) * (arr_len - 1) / 2
        array_sum = sum(arr)
    else:
        return 0
    return array_sum - unique_sum
