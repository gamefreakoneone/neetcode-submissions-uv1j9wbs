# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # Fast and slow pointer
        slow = head
        fast = head
        while fast:
            fast = fast.next
            if slow == fast:
                return True
            slow = slow.next
            if fast:
                fast = fast.next
        return False
            