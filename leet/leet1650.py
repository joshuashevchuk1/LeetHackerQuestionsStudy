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
        a,b = p,q
        def findCommon(a,b):
            while a != b:
                a = a.parent if a else q
                b = b.parent if b else p
            return a
        return findCommon(a,b)

class Solution_faster:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Step 1: Calculate depths of both nodes
        def get_depth(node):
            depth = 0
            while node:
                node = node.parent
                depth += 1
            return depth

        depth_p = get_depth(p)
        depth_q = get_depth(q)

        # Step 2: Align the depths of both nodes
        while depth_p > depth_q:
            p = p.parent
            depth_p -= 1
        while depth_q > depth_p:
            q = q.parent
            depth_q -= 1

        # Step 3: Traverse upwards until we find the common ancestor
        while p != q:
            p = p.parent
            q = q.parent

        return p

setNode = set()

balanced_input = [20, 10, 30, 5, 15, 25, 35]
balanced_tree = BinaryTree()

for element in balanced_input:
    balanced_tree.insert(element)

new_node = Node(5)
setNode.add(new_node)
node = balanced_tree.getNode(balanced_tree.root,new_node)
print(node.parent.val)

