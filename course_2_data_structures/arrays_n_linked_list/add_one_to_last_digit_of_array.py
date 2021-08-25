def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    if arr[-1] < 9:
        arr[-1] = arr[-1] + 1
        return arr
    arr = arr[::-1]
    tens = False
    for i in range(len(arr)):
        if arr[i] + 1 == 10:
            arr[i] = 0
            tens = True
        else:
            arr[i] = arr[i] + 1
            tens = False
            return arr[::-1]
        if i + 1 == len(arr) and tens is True:
            arr.append(1)
            arr = arr[::-1]
    return arr
