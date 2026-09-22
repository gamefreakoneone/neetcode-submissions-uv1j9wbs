# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        answer = ListNode()
        currPointer = answer

        while curr1 or curr2 or carry:
            calc = (curr1.val if curr1 else 0) + ( curr2.val if curr2 else 0) + carry
            carry = calc//10
            remain = calc % 10
            currNode = ListNode(val=remain)
            answer.next = currNode
            answer = answer.next
            curr1 = curr1.next if curr1 else 0
            curr2 = curr2.next if curr2 else 0
        
        return currPointer.next

