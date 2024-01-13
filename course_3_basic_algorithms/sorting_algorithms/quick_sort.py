def quick_sort(input_lst: list) -> list:
    if len(input_lst) <= 1:
        return input_lst
    quick_sort_all(input_lst, 0, len(input_lst) - 1)
    return input_lst


def quick_sort_all(lst, start_index, end_index):
    if start_index >= end_index:
        return
    pivot_index = quick_sort_one(lst, start_index, end_index)
    quick_sort_all(lst, start_index, pivot_index - 1)
    quick_sort_all(lst, pivot_index + 1, end_index)
    return


def quick_sort_one(lst, start_index, pivot_index):
    while start_index != pivot_index:
        is_start_smaller = lst[start_index] <= lst[pivot_index]
        if is_start_smaller:
            start_index += 1
        else:
            lst[pivot_index - 1], lst[start_index] = lst[start_index], lst[pivot_index - 1]
            lst[pivot_index], lst[pivot_index -
                                  1] = lst[pivot_index - 1], lst[pivot_index]
            pivot_index -= 1
    return pivot_index


if __name__ == '__main__':
    items = [1, 0]
    quick_sort(items)
    print(items)

    items = [96, 97, 98]
    quick_sort(items)
    print(items)

    items = [1, 1, 1]
    quick_sort(items)
    print(items)
