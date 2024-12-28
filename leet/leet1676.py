# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nd = []
        for node in nodes:
            nd.append(node.val)
        nodes_set = set(nd)

        def dig(root):
            if root is None:
                return
            if root.val in nodes_set:
                return root
            l = dig(root.left)
            r = dig(root.right)
            if l and r:
                return root
            return l if l else r

        common = dig(root)
        return common