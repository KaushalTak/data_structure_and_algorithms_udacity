class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    if self.head is None:
        self.head = Node(value)
    else:
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    return


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend


def append(self, value):
    """ Append a value to the end of the list. """
    if self.head is None:
        self.head = Node(value)
    else:
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)


LinkedList.append = append


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    node = self.head
    while node.next:
        if node.value == value:
            return node
        node = node.next
    return None


LinkedList.search = search


def remove(self, value):
    """ Remove first occurrence of value. """
    if self.head.value == value:
        self.head = self.head.next
        return
    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        else:
            node = node.next


LinkedList.remove = remove


def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head:
        value = self.head.value
        self.head = self.head.next
        return value


LinkedList.pop = pop


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
    # TODO: Write function to insert here
    if self.head is None:
        self.head = Node(value)
    else:
        if pos == 0:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            return
        i = 0
        node = self.head
        while node.next:
            print(i)
            if i == pos - 1:
                temp = node.next
                node.next = Node(value)
                node.next.next = temp
            i += 1
            node = node.next

        if pos > i:
            node.next = Node(value)


LinkedList.insert = insert
