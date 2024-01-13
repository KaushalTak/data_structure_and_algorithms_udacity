def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) <= 1:
        return input_list
    zero_index = 0
    two_index = len(input_list) - 1
    index = 0
    while index <= two_index:
        current_element = input_list[index]
        if current_element == 0:
            input_list[index] = input_list[zero_index]
            input_list[zero_index] = 0
            zero_index += 1
            index += 1
        elif current_element == 1:
            index += 1
        else:
            input_list[two_index] = input_list[two_index]
            input_list[two_index] = 2
            two_index -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([])
    test_function([0])
    test_function([0, 0, 0, 0])
    test_function([1, 0, 0, 0, 0])
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0,
                   2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1,
                   1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
