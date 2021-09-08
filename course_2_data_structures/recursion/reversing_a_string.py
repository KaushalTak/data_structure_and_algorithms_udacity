
def reverse_string(input):
    if len(input) == 0:
        return ''
    string = reverse_string(input[1:]) + input[0]
    return string
