class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leastUsed = Node()
        self.mostUsed = Node()
        self.leastUsed.next = self.mostUsed
        self.mostUsed.prev  = self.leastUsed

    def remove(self , node):
        prevNode , nextNode = node.prev , node.next
        prevNode.next , nextNode.prev = nextNode , prevNode
        return
    
    def insert(self , node):
        if node.key in self.cache:
            prevNode = self.cache[node.key]
            self.remove(prevNode)
        
        prevNode = self.mostUsed.prev
        prevNode.next = self.mostUsed.prev = node
        node.prev , node.next = prevNode , self.mostUsed
        self.cache[node.key] = node  


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        returned_node = self.cache[key]
        self.remove(returned_node)
        self.insert(returned_node)
        return  returned_node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            leastUsed = self.leastUsed.next
            self.remove(leastUsed)
            del self.cache[leastUsed.key]
        newNode = Node(key , value)
        self.insert(newNode)
            
