class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add(self, node):
        """Add node right after head (most recent)"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove(self, node):
        """Remove node from list"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_last(self):
        """Remove and return the last node (least recent)"""
        if self.size == 0:
            return None
        last = self.tail.prev
        self.remove(last)
        return last

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.cache = {}  # key → Node
        self.freq_map = {}  # frequency → DoublyLinkedList
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._update(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.val = value
            self._update(node)
        else:
            # New key
            if len(self.cache) >= self.capacity:
                # Evict LFU item
                lfu_list = self.freq_map[self.min_freq]
                lru_node = lfu_list.remove_last()
                del self.cache[lru_node.key]
            
            # Add new node with frequency 1
            new_node = Node(key, value)
            self.cache[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add(new_node)
            self.min_freq = 1
    
    def _update(self, node):
        """Update frequency of a node"""
        # Remove from current frequency list
        freq = node.freq
        self.freq_map[freq].remove(node)
        
        # If this was the last node at min_freq, update min_freq
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        
        # Add to new frequency list
        node.freq += 1
        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].add(node)