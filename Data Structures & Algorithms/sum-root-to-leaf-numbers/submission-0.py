# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums= []

        def dfs(curr , currNum):
            # if not curr:
            #     nums.append(currNum)
            currNum = currNum * 10 + curr.val
            if not curr.left and not curr.right:
                nums.append(currNum)
                return
            if curr.left:
                dfs(curr.left , currNum)
            if curr.right:
                dfs(curr.right , currNum)
            return

        
        curr = root
        dfs(curr , 0)
        return sum(nums)
        