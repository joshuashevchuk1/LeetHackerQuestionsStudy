
from collections import deque

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

    def inOrder_traversal(self, node):
        if node is not None:
            self.inOrder_traversal(node.left)
            print(node.val, end=" ")
            self.inOrder_traversal(node.right)

    def preOrderTraveral(self, node):
        if node is None:
            return
        print(node.val, end=" ")
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

    def lowestCommon(self, node, nodes):
        print("root.val is : ", node.val)
        nodes_set = set(nodes)
        def dig(root):
            if root is None:
                return
            if root.val in nodes_set:
                return root.val
            l = dig(root.left)
            r = dig(root.right)
            print("l : ", l)
            print("r : ", r)
            print("root.value : ", root.val)
            if l and r:
                return root.val
            return l if l else r

        common = dig(node)
        return common

    def findRoot(self, p):
        while p.parent is not None:
            p = p.parent
        return p

    def levelOrder(self,root):
        if not root:  # always return on root!
            return

        result = []
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

                result.append(current_level)

            return result


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

    print("in order ")
    tree.inOrder_traversal(tree.root)
    print("\n")
    print("pre order")
    tree.preOrderTraveral(tree.root)
    tree.findTreeMaximumDepth(tree.root)
    tree.invertTree(tree.root)
    result = tree.levelOrder(tree.root)
    print("result is : " , result)
    print("is balanced?: " , tree.isBalanced(tree.root))

    for element in balanced_input:
        balanced_tree.insert(element)

    print("is balanced tree balanced?: ",  balanced_tree.isBalanced(balanced_tree.root))
    balanced_tree.inOrder_traversal(balanced_tree.root)
    print("common is : ", balanced_tree.lowestCommon(balanced_tree.root, [25, 35]))



