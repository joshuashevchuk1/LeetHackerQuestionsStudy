
from itertools import combinations
from typing import List

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        def is_k_free(subset, k):
            # Check if subset is k-free
            for i in range(len(subset)):
                for j in range(i + 1, len(subset)):
                    if abs(subset[i] - subset[j]) == k:
                        return False
            return True

        # Generate all subsets
        subsets = []
        for r in range(len(nums) + 1):
            subsets.extend(combinations(nums, r))

        # Count k-free subsets
        k_free_count = sum(1 for subset in subsets if is_k_free(subset, k))

        return k_free_count


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        def find_all_subsets(paramArray):
            subsets = []
            num_subsets = 2 ** len(paramArray)

            for i in range(num_subsets):
                subset = []
                for j in range(len(paramArray)):
                    if (i & (1 << j)) > 0:
                        subset.append(paramArray[j])
                subsets.append(subset)
            return subsets

        subsets = find_all_subsets(nums)
        print(subsets)

        def count_k(subset, k, kcount):
            for j in range(len(subset)):
                diff = abs(subset[j] - subset[j - 1])
                if diff == k:
                    return kcount
                else:
                    return kcount + 1

        kcount = 0
        for subset in range(len(subsets)):
            if len(subsets[subset]) > 1:
                kcount = count_k(subsets[subset], k, kcount)
            else:
                kcount += 1
        return kcount


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        def find_all_subsets(paramArray):
            subsets = []
            num_subsets = 2 ** len(paramArray)

            for i in range(num_subsets):
                subset = []
                for j in range(len(paramArray)):
                    if (i & (1 << j)) > 0:
                        subset.append(paramArray[j])
                subsets.append(subset)
            return subsets

        subsets = find_all_subsets(nums)

        def count_k(subset, k):
            # Check if the subset is k-free
            for i in range(len(subset)):
                for j in range(i + 1, len(subset)):
                    if abs(subset[i] - subset[j]) == k:
                        return False
            return True

        kcount = 0
        for subset in subsets:
            if count_k(subset, k):
                kcount += 1

        return kcount

# fastest solution

from typing import List

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [1] * n  # Base case: each element alone forms a valid subset

        for i in range(n):
            for j in range(i):
                if abs(nums[i] - nums[j]) != k:
                    dp[i] += dp[j]

        return sum(dp)
