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
