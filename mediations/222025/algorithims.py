# prefix-sum calc
import heapq

nums = [1,2,3,4]
k = 2

def ps(nums):
    prev = 0
    ps = []
    for num in nums:
        prev += num
        ps.append(prev)

def get_max(ps,j,i):
    if i == 0:
        return ps[j]
    return ps[j] - ps[i-1]

# min/max heap

def minHeap(nums,k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap,num)
        if min_heap > k:
            heapq.heappop(min_heap)

    return min_heap[0]

def maxHeap(nums,k):
    nums = -1*nums
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if min_heap > k:
            heapq.heappop(min_heap)

    return -1*min_heap[0]

max = minHeap(nums,k)
min = maxHeap(nums,k)

# max sum, two sum

def ksum(nums):
    cs = ms = nums[0]
    for num in nums[1:]:
        cs = max(num, cs + num)
        ms = max(ms,cs)
    return ms

# greedy

def coinChange(coins, amount):
    # Sort coins in descending order for greedy choice
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if amount == 0:
            break
        # Use as many coins of this denomination as possible
        count += amount // coin
        amount %= coin

    # If amount becomes 0, we have found the minimum number of coins
    return count if amount == 0 else -1  # -1 if it's not possible to make the amount


# Example usage
coins = [1, 5, 10, 25]
amount = 30
print(coinChange(coins, amount))  # Output: 2 (1 coin of 25, 1 coin of 5)

# dp

def fibN(n):

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i+2]

    return dp[n]

def twoPointerBackForth(nums):
    l = 0
    r = len(nums)

    while l < r:
        l += 1
        r -= 1
        if nums[l] == nums[r]:
          return True
    return False

def twoPointerBinarySearch(nums,target):
    l = 0
    r = len(nums)

    while l <= r:
        mid = (l + r)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
             r = mid - 1
        if nums[mid] < target:
             l = mid + 1

def twoPointerMiddle(nums):
    slow = 0
    fast = 0

    while fast < len(nums) and fast + 1 < len(nums):
        slow += 1
        fast += 2

    return nums[slow]

