# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1 = headA
        c2 = headB

        while c1 != c2:
            c1 = headA if c1 is None else c1.next
            c2 = headB if c2 is None else c2.next

        return c1