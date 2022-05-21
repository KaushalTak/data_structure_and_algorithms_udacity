def merge_sorted_arrays(arr1, arr2):
    if len(arr2) == 0:
        return arr1
    if len(arr2) == 0:
        return arr1
    merged = []
    index_1 = 0
    index_2 = 0
    while index_1 < len(arr1) and index_2 < len(arr2):
        if arr1[index_1] <= arr2[index_2]:
            merged.append(arr1[index_1])
            index_1 += 1
        else:
            merged.append(arr2[index_2])
            index_2 += 1
    merged += arr1[index_1:]
    merged += arr2[index_2:]
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_index = len(arr) // 2
    left_arr = merge_sort(arr[:mid_index])
    right_arr = merge_sort(arr[mid_index:])
    return merge_sorted_arrays(left_arr, right_arr)


if __name__ == '__main__':
    arr = [10, 9, 7, 3, 8, 200, 1, 0]
    new = merge_sort(arr)
    print(new)
