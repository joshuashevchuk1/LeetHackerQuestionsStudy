# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# the crux of this problem is the

# prev pointer!

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        current = head
        prev = None  # To keep track of the previous node
        seen = set()

        while current:
            if current.val in seen:
                # Duplicate found, remove it
                prev.next = current.next
            else:
                # Add value to the set
                seen.add(current.val)
                prev = current  # Move prev forward

            current = current.next  # Move current forward

        return head
