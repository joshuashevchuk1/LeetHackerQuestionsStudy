# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        min_level = 0

        while queue:
            level_size = len(queue)
            current_level = []
            min_level += 1
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if not node.left and not node.right:
                    return min_level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return min_level