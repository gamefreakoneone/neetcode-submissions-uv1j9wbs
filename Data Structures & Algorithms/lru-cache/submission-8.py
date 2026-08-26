class LRUNode:
    def __init__(self, key = None, value = None):
        self.key, self.val = key, value
        self.prev , self.next = None , None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leastUsed = LRUNode()
        self.mostUsed = LRUNode()
        self.leastUsed.next , self.mostUsed.prev = self.mostUsed , self.leastUsed 

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next , nextNode.prev = nextNode , prevNode
        self.capacity += 1
        # I should delete the dict call init?
    
    def insert(self, node):
        if self.capacity == 0:
            leastUsed = self.leastUsed.next
            self.remove(leastUsed)
            del self.cache[leastUsed.key]
        self.cache[node.key] = node
        prevNode = self.mostUsed.prev
        prevNode.next = self.mostUsed.prev = node
        node.prev , node.next = prevNode , self.mostUsed
        self.capacity -= 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node) # We are now going to update the locaiton 
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
            return
        newNode = LRUNode(key, value)
        self.insert(newNode)
        