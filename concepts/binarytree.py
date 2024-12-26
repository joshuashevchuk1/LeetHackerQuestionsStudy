
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

    def postOrderTraveral(self, node):
        if node is None:
            return
        self.preOrderTraveral(node.left)
        self.preOrderTraveral(node.right)
        print(node.key, end=" ")

    def findTreeMaximumDepth(self, node):
        def iterate_node(node):
            if node is None:
                return 0
            return 1 + max(iterate_node(node.left), iterate_node(node.right))

        print("\n")
        print("max depth is : " + str(iterate_node(node)))

    def invertTree(self, node):
        def recurse(node):
            if not node:  # Base case: return when node is None
                return
            # Invert the current node's children
            node.left, node.right = node.right, node.left
            # Recur on left and right children
            recurse(node.left)
            recurse(node.right)

        recurse(node)
        self.inOrder_traversal(node)


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

    def isBalanced(self, node):
        def getHeight(node):
            if node is None:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        l = getHeight(node.left)
        r = getHeight(node.right)

        if abs(l - r) > 1:
            return False
        return True

if __name__ == "__main__":
    tree = BinaryTree()
    elements = [20, 10, 30, 5, 15, 25, 35,34,5,4,5,3,3,3,3,3,3]
    balanced_input = [20, 10, 30, 5, 15, 25, 35]
    balanced_tree = BinaryTree()
    # elements = []
    # for i in range(234):
    #     elements.append(np.random.rand())

    for element in elements:
        tree.insert(element)

    tree.display(tree.root)
    print("in order ")
    tree.inOrder_traversal(tree.root)
    print("\n")
    print("pre order")
    tree.preOrderTraveral(tree.root)
    tree.findTreeMaximumDepth(tree.root)
    tree.invertTree(tree.root)
    print("is balanced?: " , tree.isBalanced(tree.root))

    for element in balanced_input:
        balanced_tree.insert(element)

    balanced_tree.display(balanced_tree.root)
    print("is balanced tree balanced?: ",  balanced_tree.isBalanced(balanced_tree.root))



