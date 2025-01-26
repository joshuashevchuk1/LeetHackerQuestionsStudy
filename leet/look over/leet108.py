# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# note in this specifc case,
# we are not building the bst based on wether left < right etc. we are building based on the middiel point of the tree
# the middle element becomes the root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insert(nums, left, right):
            if left > right:
                return None  # Base case: no elements to insert

            # Choose the middle element as the root
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively construct the left and right subtrees
            node.left = insert(nums, left, mid - 1)
            node.right = insert(nums, mid + 1, right)

            return node  # Return the subtree root

        # Start by constructing the tree from the entire array
        return insert(nums, 0, len(nums) - 1)
