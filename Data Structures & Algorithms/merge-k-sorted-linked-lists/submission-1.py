# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        currHead = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val , i, node.next))
            currHead.next = node
            currHead = currHead.next
        
        currHead = dummy.next
        dummy.next = None
        del dummy
        return currHead