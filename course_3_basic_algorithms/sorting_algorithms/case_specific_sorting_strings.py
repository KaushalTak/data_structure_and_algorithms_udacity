def case_sort(string):
    '''
    Given a string with just lower and upper case characters return
    a case sorted string, i.e., at index where there was a upper
    character keep upper and lower where there was lower
    input: string example, fedRTSersUXJ
    output: string example, deeJRSfrsTUX
    '''
    sorted_string = sorted(string)
    lower_index = 0
    upper_index = 0
    new_string = ''
    for i, el in enumerate(sorted_string):
        if el.islower():
            lower_index = i
            break
    for i, el in enumerate(string):
        if el.islower():
            new_string += sorted_string[lower_index]
            lower_index += 1
        else:
            new_string += sorted_string[upper_index]
            upper_index += 1
    return new_string


if __name__ == '__main__':
    print(case_sort('fedRTSersUXJ') == "deeJRSfrsTUX")
    print(case_sort('defRTSersUXI') == "deeIRSfrsTUX")
