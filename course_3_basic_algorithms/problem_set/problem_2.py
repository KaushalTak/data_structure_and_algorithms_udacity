def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    len_arr = len(input_list)
    index = _rotated_array_search(input_list, 0, len_arr - 1, number)
    return index


def _rotated_array_search(arr, start_index, end_index, number):
    if start_index > end_index:
        return -1
    mid_index = (start_index + end_index) // 2
    if arr[mid_index] == number:
        return mid_index
    left_sorted = arr[start_index] <= arr[mid_index]
    right_sorted = arr[mid_index] <= arr[end_index]
    if left_sorted:
        if arr[start_index] <= number < arr[mid_index]:
            return _rotated_array_search(arr, start_index, mid_index - 1, number)
        else:
            return _rotated_array_search(arr, mid_index + 1, end_index, number)
    elif right_sorted:
        if arr[mid_index] < number <= arr[end_index]:
            return _rotated_array_search(arr, mid_index + 1, end_index, number)
        else:
            return _rotated_array_search(arr, start_index, mid_index - 1, number)
    else:
        raise Exception('Undefined region in arr')


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[2], 2])
    test_function([[], 1])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
