
class Node:
    def __init__(self,item):
        self.val = item
        self.right = None
        self.left = None

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = Node(node)
        else:
            self._insert(self.root, node)

    def _insert(self, node, item):
        # according to bst, left is < and right is > from root
        if item < node.val:
            if node.left is None:
                node.left = Node(item) # make the left node if it isn't made
            else:
                self._insert(node.left, item) # recurse deeper on the left side
        if item > node.val:
            if node.right is None:
                node.right = Node(item) # make the right node if it isn't made
            else:
                self._insert(node.right,item) # recurse deeper on the right side

    def InOrder(self,node):
        if node is not None:
            self.InOrder(node.left)
            print(node.val)
            self.InOrder(node.right)

    def preOrder(self,node):
        if node is None:
            return
        print(node.val)
        self.InOrder(node.left)
        self.InOrder(node.right)

    def postOrder(self,node):
        if node is None:
            return
        self.InOrder(node.left)
        self.InOrder(node.right)
        print(node.val)

nums = [1,2,3,4]

tree = Tree()

for num in nums:
    tree.insert(num)

tree.InOrder(tree.root)
tree.preOrder(tree.root)
tree.postOrder(tree.root)
