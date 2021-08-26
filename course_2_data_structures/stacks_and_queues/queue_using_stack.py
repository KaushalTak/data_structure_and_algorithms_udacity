# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def size(self):
        return self.in_stack.size() + self.out_stack.size()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.size() == 0:
            while self.in_stack.size() != 0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
