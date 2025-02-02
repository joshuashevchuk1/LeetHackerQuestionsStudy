class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answer = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                answer[stack.pop()] = num
            stack.append(num)

        return [answer.get(num, -1) for num in nums1]
