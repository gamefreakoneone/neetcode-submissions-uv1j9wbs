"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldCopy = {}

        curr = head
        while curr:
            oldCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        newHead = oldCopy[curr]
        while curr:
            oldCopy[curr].next = oldCopy.get(curr.next)
            oldCopy[curr].random = oldCopy.get(curr.random)
            curr = curr.next
        
        return newHead