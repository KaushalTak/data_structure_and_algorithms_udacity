def heapsort(arr):
    n = len(arr) - 1
    for i in range(n, -1, -1):
        heapify(arr, i, n)
    for i in range(n, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i - 1)
    return arr


def heapify(arr, start_index, end_index):
    if start_index >= end_index:
        return
    parent = start_index
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2
    largest = parent
    if left_child <= end_index and arr[largest] < arr[left_child]:
        largest = left_child
    if right_child <= end_index and arr[largest] < arr[right_child]:
        largest = right_child
    if largest == parent:
        return
    arr[largest], arr[parent] = arr[parent], arr[largest]
    heapify(arr, largest, end_index)


if __name__ == '__main__':
    arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
    solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
    heapsort(arr)
    print(arr == solution)
    arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
    solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    heapsort(arr)
    print(arr == solution)
