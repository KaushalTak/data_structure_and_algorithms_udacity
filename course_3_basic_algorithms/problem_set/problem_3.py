def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 2:
        return input_list
    sorted_array = merge_sort(input_list)
    number_1 = str(sorted_array[-1])
    number_2 = str(sorted_array[-2])
    for i in range(len(sorted_array) - 3, -1, -2):
        number_1 += str(sorted_array[i])
        number_2 += str(sorted_array[i - 1]) if i - 1 >= 0 else ''
    return [int(number_2), int(number_1)]


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    mid_index = len(input_list) // 2
    sorted_left = merge_sort(input_list[0: mid_index])
    sorted_right = merge_sort(input_list[mid_index:])
    sorted_merge = merge_sorted_arrays(sorted_left, sorted_right)
    return sorted_merge


def merge_sorted_arrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    left_index = 0
    right_index = 0
    merged = []
    while left_index < len(arr1) and right_index < len(arr2):
        if arr1[left_index] < arr2[right_index]:
            merged.append(arr1[left_index])
            left_index += 1
        else:
            merged.append(arr2[right_index])
            right_index += 1
    merged += arr1[left_index:]
    merged += arr2[right_index:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[], []])
    test_function([[1], [1]])
    test_function([[1, 2, 3], [32, 1]])
