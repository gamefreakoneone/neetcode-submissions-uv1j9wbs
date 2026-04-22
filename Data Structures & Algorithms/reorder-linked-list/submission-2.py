# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        runner = head
        while runner:
            runner = runner.next
            count +=1
        
        #Now we split the Linkedlist
        new_head = head
        runner= head

        for i in range((count-1)//2):
            runner = runner.next
        
        new_2_head = runner.next
        runner.next = None


        prev = None
        curr_head = new_2_head
        while curr_head:
            next_node = curr_head.next
            curr_head.next = prev
            prev = curr_head
            curr_head = next_node

        new_2_head = prev
        runner = new_head
        runner_2 = new_2_head
        while runner and runner_2:
            next_node_1= runner.next
            next_node_2 = runner_2.next
            runner.next = runner_2
            runner_2.next = next_node_1
            runner = next_node_1
            runner_2 = next_node_2

