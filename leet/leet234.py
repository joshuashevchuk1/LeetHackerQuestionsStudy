# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# note in the palindrome, l < r to not approach index out of range

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        numbers = []
        while current:
            numbers.append(current.val)
            current = current.next

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] != numbers[r]:
                return False
            l += 1
            r -= 1

        return True

# technically better O(1) space complexity

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Compare the first and second half
        left, right = head, prev
        while right:  # Only need to check the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
