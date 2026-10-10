class Node:
    def __init__(self, key, val):
        self.key,self.val = key,val
        self.prev,self.next = None,None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # The Map (Dictionary)
        
        # The Doubly Linked List (Dummy Head and Tail)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: Put a node at the very back (Most Recently Used)
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    # Helper: Cut a node out of the list
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
            
        new_node = Node(key, value)
        self.map[key] = new_node
        self._add(new_node)
        
        if len(self.map) > self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.map[lru_node.key]
