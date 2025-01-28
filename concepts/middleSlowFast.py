# the slow fast two pointer approach always returns the middle of an array or a linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def findMiddle(arr):
    slow = 0
    fast = 0

    while fast < len(arr) and fast + 1 < len(arr):
        slow += 1
        fast += 2

    return arr[slow]

