class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
            return

    def to_list(self):
        temp = []
        node = self.head
        while node:
            temp.append(node.value)
            node = node.next
        return temp


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)
    node = linked_list.head
    while node:
        print(node.value)
        node = node.next
    print(linked_list.to_list())
