def deep_reverse(arr):
    new_list = []
    for i in range(len(arr) - 1, -1, -1):
        if isinstance(arr[i], list):
            output = deep_reverse(arr[i])
            new_list.append(output)
        else:
            new_list.append(arr[i])
    return new_list
