def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    n0 = [1]
    if n == 0:
        return n0
    nx = [n0]
    for i in range(1, n + 1):
        temp = []
        for j in range(i + 1):
            if j == 0:
                temp.append(1)
            elif j == i:
                temp.append(1)
            else:
                temp.append(nx[i - 1][j - 1] + nx[i - 1][j])
        nx.append(temp)
    return nx[-1]
