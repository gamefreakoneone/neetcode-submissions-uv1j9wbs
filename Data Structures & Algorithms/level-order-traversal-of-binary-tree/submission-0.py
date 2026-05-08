# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_result = []

        def traverse(root , curr_level):
            if not root:
                return None
            if len(level_result) == curr_level: # Remember that depth is 1 sorted and level_result is 0 sorted
                level_result.append([]) # We are now creating a new_level for the uninitialsed
            
            level_result[curr_level].append(root.val)
            traverse(root.left , curr_level+1)
            traverse(root.right , curr_level+1)
        traverse(root , 0)
        return level_result
        