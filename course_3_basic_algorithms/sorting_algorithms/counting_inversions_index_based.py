'''
The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.
Here are some examples:
[0,1] has 0 inversions
[2,1] has 1 inversion (2,1)
[3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
[7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
'''


def count_inversions(arr):
    if len(arr) <= 1:
        return 0
    count = count_inversions_rec(arr, 0, len(arr) - 1)
    return count


def count_inversions_rec(arr, start_index, end_index):
    if start_index >= end_index:
        return 0
    mid_index = (start_index + end_index) // 2
    left_count = count_inversions_rec(arr, start_index, mid_index)
    right_count = count_inversions_rec(arr, mid_index + 1, end_index)
    merged_count = merge_inverted_arr(
        arr, start_index, mid_index, mid_index + 1, end_index)
    total_count = left_count + right_count + merged_count

    return total_count


def merge_inverted_arr(arr, first_start_ind, first_end_ind, second_start_ind, second_end_index):
    output = []
    count = 0
    first_start = first_start_ind
    second_start = second_start_ind
    while first_start_ind <= first_end_ind and second_start_ind <= second_end_index:
        if arr[first_start_ind] <= arr[second_start_ind]:
            output.append(arr[first_start_ind])
            first_start_ind += 1
        else:
            count += (first_end_ind - first_start_ind) + 1
            output.append(arr[second_start_ind])
            second_start_ind += 1
    if first_start_ind == first_end_ind + 1 and second_start_ind != second_end_index + 1:
        output += arr[second_start_ind:second_end_index + 1]
    if first_start_ind != first_end_ind + 1 and second_start_ind == second_end_index + 1:
        output += arr[first_start_ind:first_end_ind + 1]
    for i in range(first_start, first_end_ind + 1):
        arr[i] = output.pop(0)
    for i in range(second_start, second_end_index + 1):
        arr[i] = output.pop(0)
    return count


if __name__ == '__main__':
    print(count_inversions([0, 1]) == 0)
    print(count_inversions([2, 1]) == 1)
    print(count_inversions([3, 1, 2, 4]) == 2)
    print(count_inversions([7, 5, 3, 1]) == 6)
