class Node:
    def __init__(self, key=0 , value=0):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leastUsed = Node()
        self.mostUsed = Node()
        self.leastUsed.next , self.mostUsed.prev = self.mostUsed , self.leastUsed

    def insert(self, node):
        prevNode = self.mostUsed.prev
        prevNode.next = self.mostUsed.prev = node
        node.prev, node.next = prevNode , self.mostUsed
    
    def remove(self, node):
        prevNode , nextNode = node.prev , node.next
        prevNode.next , nextNode.prev = nextNode , prevNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.capacity:
            leastUsedNode = self.leastUsed.next
            self.remove(leastUsedNode)
            del self.cache[leastUsedNode.key]
            del leastUsedNode 
        
