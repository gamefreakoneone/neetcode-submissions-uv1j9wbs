# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 1
        queue = deque()
        # visited = set()
        queue.append(root)
        answer = []
        while len(queue) > 0:
            curr = []
            for i in range(len(queue)):
                level_node = queue.popleft()
                curr.append(level_node.val)
                if level_node.left:
                    queue.append(level_node.left)
                if level_node.right:
                    queue.append(level_node.right)
            answer.append(curr)
            level += 1
        return answer
