def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):
    ind = recursive_binary_search(target, source)
    if ind == 0:
        return 0
    if ind is None:
        return None
    smaller = ind
    while True:
        if source[smaller - 1] == target:
            smaller -= 1
        else:
            return smaller


def contains(target, source):
    ind = recursive_binary_search(target, source)
    if ind is not None:
        return True
    return False
