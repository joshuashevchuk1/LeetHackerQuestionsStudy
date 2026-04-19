class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = None
        n = len(nums)
        items = {}
        for i in range(n):
            if nums[i] not in items.keys():
                items[nums[i]] = 1
            else:
                items[nums[i]] += 1
        for k in items.keys():
            if items[k] >= n/2:
                majority = k
        return majority


    def majorityElement_fast(self, nums: list[int]) -> int:
        app=len(nums)//2
        for i in set(nums):
            if nums.count(i)>app:
                return i

s = Solution()
print(Solution.majorityElement_fast(s,nums=[3,2,3]))
items = [1,1,2,3]
print(set(items))
for i in set(items):
    print(items.count(i))