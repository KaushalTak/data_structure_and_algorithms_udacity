class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1, llist_2):
    sset = set()
    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        sset.add(node1.value)
        node1 = node1.next
    while node2:
        sset.add(node2.value)
        node2 = node2.next
    llist_u = LinkedList()
    for i in sset:
        llist_u.append(i)
    return llist_u


def intersection(llist_1, llist_2):
    # Your Solution Here
    sset_1 = set()
    sset_2 = set()
    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        sset_1.add(node1.value)
        node1 = node1.next
    while node2:
        sset_2.add(node2.value)
        node2 = node2.next
    sset_i = sset_2.intersection(sset_1)
    llist_i = LinkedList()
    for i in sset_i:
        llist_i.append(i)
    return llist_i


def test():
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]
    for i in element_1:
        linked_list_3.append(i)
    for i in element_2:
        linked_list_4.append(i)
    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))

    # Test case 3 --> edge case where one linked list is empty
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_1 = [1, 2, 3, 4]
    element_2 = []
    for i in element_1:
        linked_list_3.append(i)
    for i in element_2:
        linked_list_4.append(i)
    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))

    # Test case 4 --> edge case where both linked lists are empty
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_1 = []
    element_2 = []
    for i in element_1:
        linked_list_3.append(i)
    for i in element_2:
        linked_list_4.append(i)
    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))


if __name__ == '__main__':
    test()
