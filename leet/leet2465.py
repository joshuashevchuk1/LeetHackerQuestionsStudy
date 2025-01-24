import heapq
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        min_heap = nums[:]
        heapq.heapify(min_heap)

        # Max-heap (negate the values to simulate max-heap)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        averages = set()

        while min_heap:
            MIN = heapq.heappop(min_heap)
            MAX = -heapq.heappop(max_heap)

            average = (MAX + MIN) / 2
            averages.add(average)

        return len(averages)
