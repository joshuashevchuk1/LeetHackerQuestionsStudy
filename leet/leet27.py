class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

# better solution using pop

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Initialize a pointer to iterate through the list
        index = 0
        while index < len(nums):
            if nums[index] == val:
                # Remove the element by overwriting it with the last element
                nums[index] = nums[-1]
                nums.pop()
            else:
                # Move the pointer forward
                index += 1
        return len(nums)