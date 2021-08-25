class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self. head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    def reverse(self):
        new_list = LinkedList()
        old_node = None
        for item in self:
            new_node = Node(item)
            new_node.next = old_node
            old_node = new_node
        new_list.head = old_node
        return new_list


def main():
    llist = LinkedList()
    for value in [4, 2, 5, 1, -3, 0]:
        llist.append(value)
    flipped = llist.reverse()
    is_correct = list(flipped) == list(
        [0, -3, 1, 5, 2, 4]) and list(llist) == list(flipped.reverse())
    print("Pass" if is_correct else "Fail")


if __name__ == '__main__':
    main()
