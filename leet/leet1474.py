# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dn = 0
        dm = 0

        # Function to delete `n` nodes starting from the current node
        def deleteUntilN(node, dn):
            count = 0
            while node and count < n:
                node = node.next
                count += 1
            return node

        # Function to retain `m` nodes and then delete `n` nodes
        def iterate(node, dm):
            if not node:
                return None

            # Retain `m` nodes
            while node and dm < m - 1:
                node = node.next
                dm += 1

            if not node or not node.next:
                return None

            # Delete `n` nodes
            node.next = deleteUntilN(node.next, dn)

            # Continue iteration after deleting
            iterate(node.next, 0)

        iterate(head, dm)

        return head
