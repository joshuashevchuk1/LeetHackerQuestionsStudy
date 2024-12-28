class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

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
                current.left = Node(key, parent=current)  # Set parent
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key, parent=current)  # Set parent
            else:
                self._insert(current.right, key)

    def getNode(self, root, node):
        if root is None:
            return None
        if root.val == node.val:
            return root
        left = self.getNode(root.left, node)
        right = self.getNode(root.right, node)

        if left:
            return left
        if right:
            return right
        return None



class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        return


balanced_input = [20, 10, 30, 5, 15, 25, 35]
balanced_tree = BinaryTree()

for element in balanced_input:
    balanced_tree.insert(element)

new_node = Node(5)
node = balanced_tree.getNode(balanced_tree.root,new_node)
print(node.parent.val)

