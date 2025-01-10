from collections import deque

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

    def inOrderTravesal(self,node):
        if node is not None:
            self.inOrderTravesal(node.left)
            print(node.val)
            self.inOrderTravesal(node.right)

    def preOrderTravesal(self,node):
        if node is not None:
            print(node.val)
            self.preOrderTravesal(node.left)
            self.preOrderTravesal(node.right)

    def postOrderTravesal(self,node):
        if node is not None:
            self.postOrderTravesal(node.left)
            self.postOrderTravesal(node.right)
            print(node.val)

    def leveltraversl(self,root):
        if not root:
            return

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                current_level = 2 * node.val
                print(current_level)
                # node.val = node.val *2 can do an action

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                result.append(current_level)




nums = [1,2,3,4]

tree = Tree()

for num in nums:
    tree.insert(num)

tree.inOrderTravesal(tree.root)
tree.preOrderTravesal(tree.root)
tree.postOrderTravesal(tree.root)
print("level----------")
tree.leveltraversl(tree.root)
print("level----------")