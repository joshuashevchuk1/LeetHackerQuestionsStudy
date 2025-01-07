
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = Node(node)
        else:
            self._insert(self.root, node)

    def _insert(self, node, item):
        if item < node.val:
           if node.left is None:
                node.left = Node(item)
           else:
               self._insert(node.left, item)
        if item > node.val:
           if node.right is None:
                node.right = Node(item)
           else:
               self._insert(node.right, item)

nums = [1,2,3,4]

tree = Tree()

for num in nums:
    tree.insert(num)