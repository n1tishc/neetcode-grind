# LRU Cache, O(1) get and put
# Part 1: hash map + doubly linked list with sentinel head/tail
# Part 2: optional time-to-live per key (time passed in as `now` so it's testable)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node(None, None)  # most recent sits right after head
        self.tail = Node(None, None)  # least recent sits right before tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_front(node)
        else:
            if len(self.map) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
            node = Node(key, value)
            self.map[key] = node
            self._add_front(node)
