class Queue:
     def __init__(self):
          self.arr = []

     def size(self):
          return len(self.arr)

     def enqueue(self, item):
          self.arr.append(item)

     def dequeue(self):
          return self.arr.pop(0)
