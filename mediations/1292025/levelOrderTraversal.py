from collections import deque

from django.db.models.expressions import result
from networkx.classes import nodes
from sympy.physics.units import current


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

def levelOrder(root):

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val) # add actionables on the node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

tree = BinaryTree()
nums = [1, 2, 3, 4, 5, 6, 7]
tree.root = tree.insertBalanced(nums, 0, len(nums) - 1)
result = levelOrder(tree.root)
print(result)


# process the binary from bottom up rather than top down
def reverse_level_order(root):
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

result = reverse_level_order(tree.root)
print(result)