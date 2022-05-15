def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index
    first_index = find_first_index(arr, number, 0, len(arr) - 1)
    last_index = find_last_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]


def find_first_index(arr, number, start_index, end_index):
    # recursive solution
    # Base case, start_index > end_index return -1
    if start_index > end_index:
        return -1
    # find middle index
    middle_index = (start_index + end_index) // 2
    # check if element at middle index is equal to number
    if arr[middle_index] == number:
        # current_pos = check fo first half of arr ind
        current_pos = find_first_index(
            arr, number, start_index, middle_index - 1)
    # if current_pos = -1
        if current_pos == -1:
            start_pos = middle_index
        else:
            start_pos = current_pos
        return start_pos
    # check if el at mid ind is less than number
    elif arr[middle_index] < number:
        return find_first_index(arr, number, middle_index + 1, end_index)
    # check if el at mid ind is high than number
    else:
        return find_first_index(arr, number, start_index, middle_index - 1)


def find_last_index(arr, number, start_index, end_index):
    if start_index > end_index:
        return -1
    middle_index = (start_index + end_index) // 2
    if arr[middle_index] == number:
        current_pos = find_last_index(arr, number, middle_index + 1, end_index)
        if current_pos == -1:
            start_pos = middle_index
        else:
            start_pos = current_pos
        return start_pos
    elif arr[middle_index] < number:
        return find_last_index(arr, number, middle_index + 1, end_index)
    # check if el at mid ind is high than number
    else:
        return find_last_index(arr, number, start_index, middle_index - 1)
