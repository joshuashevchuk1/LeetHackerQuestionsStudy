
# to serialize the binary tree,
# conceptually the simplest is just to do level order traversal backwards and forwards.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string using level-order traversal.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = [root]
        result = []

        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        # Remove trailing "null" values for more compact serialization
        while result and result[-1] == "null":
            result.pop()

        return "_".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree using level-order traversal.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split("_")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1

        while queue:
            node = queue.pop(0)
            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
