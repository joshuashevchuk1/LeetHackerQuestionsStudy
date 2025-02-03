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

