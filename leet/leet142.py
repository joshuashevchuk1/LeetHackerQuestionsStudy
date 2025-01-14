# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break

        if cycle is True:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow
        return
