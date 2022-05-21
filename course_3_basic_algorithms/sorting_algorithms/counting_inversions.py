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
    count, arr = count_inversions_rec(arr)
    return count


def count_inversions_rec(arr):
    if len(arr) <= 1:
        return 0, arr
    mid_index = len(arr) // 2
    left_count, left_arr = count_inversions_rec(arr[:mid_index])
    right_count, right_arr = count_inversions_rec(arr[mid_index:])
    merged_count, merged_arr = merge_arr(left_arr, right_arr)
    return left_count + right_count + merged_count, merged_arr


def merge_arr(left_arr, right_arr):
    if len(left_arr) == 0:
        return 0, right_arr
    if len(right_arr) == 0:
        return 0, left_arr
    left_index = 0
    right_index = 0
    count = 0
    merged = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            merged.append(left_arr[left_index])
            left_index += 1
        else:
            merged.append(right_arr[right_index])
            count += len(left_arr) - left_index
            right_index += 1
    merged += left_arr[left_index:]
    merged += right_arr[right_index:]
    return count, merged


if __name__ == '__main__':
    print(count_inversions([0, 1]) == 0)
    print(count_inversions([2, 1]) == 1)
    print(count_inversions([3, 1, 2, 4]) == 2)
    print(count_inversions([7, 5, 3, 1]) == 6)
