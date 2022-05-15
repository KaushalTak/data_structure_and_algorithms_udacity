'''
If we want to store and get store numbers in a way
that allows us to get the maximum or minimum very quickly
we can't use 
arrays(O(1) for insertion, O(n) for removing max/min)
linked_list(O(1) for insertion, O(n) for removing)
Binary Search Trees(O(log n) for inserting, O(n) in worst case when it is just one sided like linked list)
We need Heaps, it has two properties:
1. Complete Binary Tree - A complete binary tree is a special type of binary tree 
    in which all levels must be filled except for the last level. Moreover, 
    in the last level, the elements must be filled from left to right.
2. Heap order property
O(log n) for insertion, O(log n) for removal

Implementation idea:
We are going to implement the complete tree in an array.
A parent at n will have childern at 2n+1 and 2n+2
In array I can keep track of where should next element go.
Now for insertition I can insert at the end and then heapify upwards.
What it means is comparing element with parent and swapping.
Similarly for removing I remove from top and move last element to top
then heapify downwards.
'''

# Implement a class heap


class Heap:
    def __init__(self):
        self.cbt = [None for i in range(10)]
        self.next_index = 0

    def insert(self, value):
        if self.next_index > len(self.cbt) - 1:
            self._handle_overflow()
        self.cbt[self.next_index] = value
        self._up_heapify()
        self.next_index += 1

    def _up_heapify(self):
        # a children at n has parent at (n - 1)//2
        child_index = self.next_index
        parent_index = (child_index - 1) // 2
        while child_index >= 1:
            if self.cbt[child_index] <= self.cbt[parent_index]:
                return
            else:
                child_element = self.cbt[child_index]
                self.cbt[child_index] = self.cbt[parent_index]
                self.cbt[parent_index] = child_element
                child_index = parent_index
                parent_index = (child_index - 1) // 2

    def _handle_overflow(self):
        self.cbt = self.cbt + [None for i in range(len(self.cbt))]

    def remove(self):
        if self.cbt[0] is None:
            return None
        value = self.cbt[0]
        self.cbt[0] = self.cbt[self.next_index - 1]
        print(self.cbt)
        self.next_index -= 1
        self._down_heapify()
        return value

    def _down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            left_index = parent_index * 2 + 1
            right_index = parent_index * 2 + 2
            left_element = None
            right_element = None
            max_element = self.cbt[parent_index]
            if left_index < self.next_index:
                left_element = self.cbt[left_index]
            if right_index < self.next_index:
                right_element = self.cbt[right_index]
            if left_element:
                max_element = max(left_element, max_element)
            if right_element:
                max_element = max(right_element, max_element)
            if self.cbt[parent_index] == max_element:
                return
            elif max_element == left_element:
                self.cbt[left_index] = self.cbt[parent_index]
                self.cbt[parent_index] = left_element
                parent_index = left_index
            else:
                self.cbt[right_index] = self.cbt[parent_index]
                self.cbt[parent_index] = right_element
                parent_index = right_index
            print(max_element)
