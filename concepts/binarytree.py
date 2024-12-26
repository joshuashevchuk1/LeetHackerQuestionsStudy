class Node:
    def __init__(self, key):
        self.key = key
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
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def inOrder_traversal(self, node):
        if node is not None:
            self.inOrder_traversal(node.left)
            print(node.key , end=" ")
            self.inOrder_traversal(node.right)

    def preOrderTraveral(self, node):
        if node is None:
            return
        print(node.key, end=" ")
        self.preOrderTraveral(node.left)
        self.preOrderTraveral(node.right)


    def display(self, root, space=0, level_spacing=10):
        if root is None:
            return
        space += level_spacing
        # Print the right child first
        self.display(root.right, space)
        # Print current node after space count
        print()
        print(" " * (space - level_spacing) + str(root.key))
        # Print the left child
        self.display(root.left, space)


if __name__ == "__main__":
    tree = BinaryTree()
    elements = [20, 10, 30, 5, 15, 25, 35]
    for element in elements:
        tree.insert(element)

    tree.display(tree.root)
    print("in order ")
    tree.inOrder_traversal(tree.root)
    print("\n")
    print("pre order")
    tree.preOrderTraveral(tree.root)


