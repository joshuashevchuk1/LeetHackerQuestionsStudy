# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def levelOrder(root):
            if not root:  # always return on root!
                return 0

            h = 0
            queue = deque([root])

            while queue:  # iterate until queue is empty. In this case queue is the tree
                level_size = len(queue)
                current_level = []  # add to the current level and pass through

                for _ in range(level_size):
                    node = queue.popleft()  # get the node by popping the queue
                    current_level.append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                h += 1

            return h

        return levelOrder(root)