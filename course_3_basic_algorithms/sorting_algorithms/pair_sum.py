def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    """
    first = 0
    last = len(arr) - 1
    arr = sorted(arr)
    while first < last:
        print(arr, first, last)
        if arr[first] + arr[last] == target:
            return [arr[first], arr[last]]
        elif arr[first] + arr[last] < target:
            first += 1
        else:
            last -= 1
    return [None, None]
