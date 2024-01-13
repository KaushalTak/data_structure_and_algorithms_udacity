class Doubly_linked_list(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 1 or type(capacity) != int:
            # Will it be better if I raise an exception here? Instead of priniting out message?
            print("Capacity needs to be an integer with value greater than 0")
            return
        self.capacity = capacity
        self.cache = {}
        self.cache_size = 0
        self.head = Doubly_linked_list()
        self.tail = Doubly_linked_list()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            _dll = self.cache[key]
            self._remove(_dll)
            self._add(_dll)
            return _dll.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.cache:
            if self.cache_size == self.capacity:
                self._remove()
                _dll = Doubly_linked_list(key, value)
                self._add(_dll)
                self.cache[key] = _dll
            else:
                _dll = Doubly_linked_list(key, value)
                self._add(_dll)
                self.cache[key] = _dll
                self.cache_size += 1

    def _add(self, node):
        h = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = h
        h.prev = node

    def _remove(self, node=None):
        if self.cache_size > 0:
            if node:
                p = node.prev
                n = node.next
                p.next = n
                n.prev = p
            else:
                del self.cache[self.tail.prev.key]
                p = self.tail.prev.prev
                p.next = self.tail
                self.tail.prev = p


def test():
    # Test 1
    print("Test 1, output should be 1 2 -1 -1")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))
    print(our_cache.get(2))
    print(our_cache.get(9))
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(3))

    # Test 2
    print('\n--------------------------------------------------------------------------------')
    print("Test 2, output should be 'Capacity needs to be an integer with value greater than 0'")
    our_cache = LRU_Cache(0)

    # Test 3
    print('\n--------------------------------------------------------------------------------')
    print("Test 3, output should be 'Capacity needs to be an integer with value greater than 0'")
    our_cache = LRU_Cache(1.5)

    # Test 4
    print('\n--------------------------------------------------------------------------------')
    print("Test 4, output should be -1 2 -1")
    our_cache = LRU_Cache(3)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))
    print(our_cache.get(2))
    our_cache.set(5, 5)
    print(our_cache.get(3))


if __name__ == '__main__':
    test()
