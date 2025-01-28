# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


# faster solution using a monotonic stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        vals = []

        while current:
            vals.append(current.val)
            current = current.next

        # next greater
        answer = [0] * len(vals)
        stack = []
        for i in range(len(vals)):
            while stack and vals[i] > vals[stack[-1]]:  # shorthand top of list
                index = stack.pop()
                answer[index] = vals[i]
            stack.append(i)

        return answer


# slow solution
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        answer = []
        vals = []

        while current:
            vals.append(current.val)
            current = current.next

        def next_greater_elements(vals):
            queue = deque(vals)
            answer = []

            for i, num in enumerate(vals):
                next_greater = None
                for val in queue:
                    if val > num:
                        next_greater = val
                        break

                if next_greater is None:
                    answer.append(0)
                else:
                    answer.append(next_greater)
                queue.popleft()
            return answer

        return next_greater_elements(vals)