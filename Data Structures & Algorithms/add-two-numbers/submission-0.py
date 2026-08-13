# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        resultNode = ListNode()
        start = resultNode
        carry = 0
        while l1 or l2 or carry != 0:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry
            carry = sum // 10
            val = sum % 10
            newNode = ListNode(val)
            resultNode.next = newNode
            resultNode = resultNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return start.next


