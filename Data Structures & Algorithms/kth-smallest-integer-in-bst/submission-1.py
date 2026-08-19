# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        count = k
        result = root.val

        def dfs(node):
            nonlocal count, result
            if not node: # We reached the end of the tree
                return 
            dfs(node.left) # We are going directly to the lwoest value
            count -= 1 # Now that we have rreturned, reduce the count since we already traveled to the lwoer values
            if count == 0: # This is the lowest value
                result = node.val
                return
            dfs(node.right) # Because we still ahve to follow the order to find the n'th samllest value
        
        dfs(root)
        return result
        
        