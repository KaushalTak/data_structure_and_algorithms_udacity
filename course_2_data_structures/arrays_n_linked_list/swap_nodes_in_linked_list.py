"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""


def swap_nodes(head, left_index, right_index):
    if head is None:
        return None
    elif left_index == right_index:
        return head
    else:
        i = left_index
        j = right_index
        k = 0
        node = head
        while k < j:
            if i == 0:
                one_prev = None
                one_current = node
            elif k + 1 == i:
                one_prev = node
                one_current = node.next
            if k + 1 == j:
                second_prev = node
                second_current = node.next
            node = node.next
            k += 1
        second_prev.next = one_current
        temp = one_current.next
        one_current.next = second_current.next
        second_current.next = temp
        if one_prev is None:
            return second_current
        else:
            one_prev.next = second_current
            return head
