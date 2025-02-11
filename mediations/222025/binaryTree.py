from collections import deque

from django.db.models.expressions import result
from sympy.physics.units import current

from concepts.queueExample import queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.val:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def insertBalanced(self,nums,left,right):
        if left > right:
            return None

        mid = (left + right) // 2
        node = Node(nums[mid])

        node.left = self.insertBalanced(nums, left, mid - 1)
        node.right = self.insertBalanced(nums, mid + 1, right)

        return node


    def inOrderTraversal(self,node):
        if node is not None:
            self.inOrderTraversal(node.left)
            print(node)
            self.inOrderTraversal(node.right)

    def preOrderTraversal(self,node):
        if node is not None:
            print(node)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self,node):
        if node is not None:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node)

    def levelOrderTraversal(self,root):
        if not root:
            return

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                result.append(current_level)

        return result

    def levelOrderTraversalBottomUp(self, root):
        if not root:
            return

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.pop()
                current_level.append(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
                result.append(current_level)

        return result

    def minDepth(self,root):
        if not root:
            return

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
                    queue.append(node.left)

        return min_level
