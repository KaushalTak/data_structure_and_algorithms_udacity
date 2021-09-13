# Solution
def subsets(arr):
    return return_subsets(arr, 0)


def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)
    print(arr, index, small_output)
    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)
    print(output)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output
