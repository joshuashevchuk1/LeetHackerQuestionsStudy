import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        l = len(nums)
        for i in range(l):
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
