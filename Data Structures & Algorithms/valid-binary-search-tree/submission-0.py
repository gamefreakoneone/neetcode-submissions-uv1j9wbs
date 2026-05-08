# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node , left_limit , right_limit):
            if not node:
                return True
            if not (left_limit < node.val < right_limit):
                return False
            
            return valid(node.left , left_limit , node.val) and valid(node.right, node.val , right_limit)
        
        return valid(root , float("-inf"), float("inf"))