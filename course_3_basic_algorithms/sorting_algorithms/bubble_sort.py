def bubble_sort_1(l):
    '''
    sort elements in array.
    input: list
    output: unsorted list
    '''
    for _ in range(len(l) - 1):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l


def bubble_sort_2(l):
    '''
    sort based on two elements like a list of tuple or list of list.
    for example: [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
    input: unsorted array
    output: sorted_array
    '''
    for _ in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]
            if this[0] < prev[0]:
                continue
            elif this[0] == prev[0]:
                if this[1] <= prev[1]:
                    continue
                else:
                    l[index - 1] = this
                    l[index] = prev
            else:
                l[index - 1] = this
                l[index] = prev
    return l
