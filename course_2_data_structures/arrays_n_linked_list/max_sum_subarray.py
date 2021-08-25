def max_sum_subarray1(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    sum_list = []
    for i in range(len(arr)):
        su = arr[i]
        sum_list.append(su)
        for j in range(i + 1, len(arr)):
            su += arr[j]
            sum_list.append(su)
    max_sum = sum_list[0]
    for i in sum_list:
        if i > max_sum:
            max_sum = i
    return max_sum


# Solution
'''
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let `current_sum` denotes the sum of a subarray, and `max_sum` denotes the maximum value of `current_sum`.
3. LOOP STARTS: For each element of the array, update the `current_sum` with the MAXIMUM of either:
 - The element added to the `current_sum` (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
4. Return `max_sum`
'''

def max_sum_subarray2(arr):

    current_sum = arr[0]  # `current_sum` denotes the sum of a subarray
    # `max_sum` denotes the maximum value of `current_sum` ever
    max_sum = arr[0]

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:

        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        current_sum = max(current_sum + element, element)
        print(current_sum)
        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)

    return max_sum
