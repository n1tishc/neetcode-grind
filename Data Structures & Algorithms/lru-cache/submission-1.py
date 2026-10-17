# Create a DLL class for 
class DLL:
    def __init__(self, value=-1, nxt=None, prev=None, key=-1):
        self.value = value
        self.nxt = nxt
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        # Dummy head and tail nodes
        self.dummy_head = DLL()
        self.dummy_tail = DLL()

        # Link the dummy noes to each other
        self.dummy_head.nxt = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

        self.cache_map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # Just returns the node value and updates the LRU order
        if key not in self.cache_map: return -1
        else:
            node = self.cache_map[key]
            if self.dummy_head.nxt is node: return node.value
            else:
                # Get the left and right nodes of the node
                left = node.prev
                right = node.nxt

                # link the left and right parts with eachother
                left.nxt = right
                right.prev = left

                # Update he head pointer to the updated node
                old_head = self.dummy_head.nxt
                self.dummy_head.nxt = node
                node.nxt = old_head
                node.prev = self.dummy_head
                old_head.prev = node
            
                return node.value

    def put(self, key: int, value: int) -> None:
        # First case the key is new, aka not in cache_map
        if key not in self.cache_map:
            new_node = DLL(value=value, key=key)
            # Place the new node as the most recent mode in the start 
            old_head = self.dummy_head.nxt
            self.dummy_head.nxt = new_node
            old_head.prev = new_node
            new_node.nxt = old_head
            new_node.prev = self.dummy_head

            # add key to cache map
            self.cache_map[key] = new_node

            # If the capacity is filled
            if len(self.cache_map) == (self.capacity + 1):
                # Just remove the tail node, aka the least used one
                old_tail = self.dummy_tail.prev
                old_tail.prev.nxt = self.dummy_tail
                self.dummy_tail.prev = old_tail.prev

                del self.cache_map[old_tail.key]
        # The key exixts we just update the vluse and make it the most recent one, here it cannot exceed capacity as it is just updating existing nodes
        else:
            node = self.cache_map[key]
            node.value = value 

            if self.dummy_head.nxt is node: return 
            else:
                # Get the left and right nodes of the node
                left = node.prev
                right = node.nxt

                # link the left and right parts with eachother
                left.nxt = right
                right.prev = left

                # Update he head pointer to the updated node
                old_head = self.dummy_head.nxt
                self.dummy_head.nxt = node
                node.nxt = old_head
                node.prev = self.dummy_head
                old_head.prev = node
        
