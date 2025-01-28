
# uses a monotonic stack to get the next greater element

def nextGreater(vals):
    answer = [0] * len(vals)
    stack = []
    for i in range(len(vals)):
        # at the first iteration stack is empty so just append(i)
        while stack and vals[i] > vals[stack[-1]]:  # shorthand top of list
            # if stack is not empty and the current i
            # (should be 2..n at the 2nd iteration)
            # is greater than the top of the stack
            # pop the top of the stack and append to answers
            index = stack.pop()
            answer[index] = vals[i]
        stack.append(i)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                answer[stack.pop()] = num
            stack.append(num)

        return [answer.get(num, -1) for num in nums1]


# next greater element 2
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        answer = [-1] * n

        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                index = stack.pop()
                answer[index] = num

            if i < n:
                stack.append(i)

        return answer