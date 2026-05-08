# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root, curr_level):
            if not root:
                return None
            if len(res) == curr_level:
                res.append([])
            
            res[curr_level].append(root.val)
            dfs(root.left , curr_level+1)
            dfs(root.right, curr_level+1)
        
        dfs(root, 0)
        return res
        