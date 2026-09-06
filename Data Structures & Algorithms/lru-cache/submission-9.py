class Node:
    def __init__(self , key,value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.most = Node(0 , 0)
        self.least = Node(0,0)
        self.least.next , self.most.prev = self.most , self.least

    def insert(self , node):
        prev_node = self.most.prev
        prev_node.next = self.most.prev = node
        node.prev = prev_node
        node.next = self.most
    
    def remove(self , node):
        curr = node
        prev_node , next_node = curr.prev , curr.next
        prev_node.next , next_node.prev = next_node , prev_node

        

    def get(self, key: int) -> int:
        if key in self.cache:
            curr = self.cache[key]
            self.remove(curr) # It is now the most used element
            self.insert(curr) # It is now the 
            return curr.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node =  self.cache[key]
            self.remove(node)
            node.value = value
            self.insert(node)
            self.cache[key] = node
            return
        elif self.capacity == 0:
            leastUsed = self.least.next
            self.remove(leastUsed)
            del self.cache[leastUsed.key]
            del leastUsed
            self.capacity += 1
        newNode = Node(key ,value)
        self.cache[key] = newNode
        self.capacity -= 1
        self.insert(newNode)
        return         

