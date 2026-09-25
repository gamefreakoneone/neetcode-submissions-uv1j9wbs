# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root
        head = root

        # while curr:
        if key < curr.val:
            curr.left = self.deleteNode(curr.left , key)
        elif key > curr.val:
            curr.right = self.deleteNode(curr.right , key)
        elif curr.val == key:
            if not curr.right:
                return curr.left
            elif not curr.left:
                return curr.right
            else:
                succ = curr.right
                while succ.left:
                    succ= succ.left
                curr.val = succ.val
                curr.right = self.deleteNode(curr.right , succ.val)
                return curr

        return head
