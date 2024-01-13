def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    if number == 0 or number == 1:
        return number
    upper_bound = number
    lower_bound = 0
    while upper_bound - lower_bound > 1:
        mid = (upper_bound + lower_bound) // 2
        if mid * mid == number:
            return mid
        elif mid * mid > number:
            upper_bound = mid
        else:
            lower_bound = mid
    return lower_bound


if __name__ == '__main__':
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (10 == sqrt(100)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (26 == sqrt(676)) else "Fail")
