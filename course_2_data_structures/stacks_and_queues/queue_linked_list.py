class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail.next = new_node
            # shift the tail (i.e., the back of the queue)
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    # TODO: Add the size method

    def size(self):
        return self.num_elements

    # TODO: Add the is_empty method
    def is_empty(self):
        return self.head is None
