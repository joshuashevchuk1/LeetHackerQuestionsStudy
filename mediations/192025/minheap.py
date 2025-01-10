import heapq


def minheap(arr,k):
    min_heap = []
    ls = len(arr)
    for i in range(ls):
        heapq.heappush(min_heap,i)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    if len(min_heap) > 0:
        return min_heap[0]

def maxHeapApproach(arr, k):
    max_heap = []
    for num in arr:
        # Negate the element to simulate a max-heap using heapq (min-heap)
        heapq.heappush(max_heap, -num)

        # If the heap size exceeds k, pop the smallest (negated largest)
        if len(max_heap) > k:
            heapq.heappop(max_heap) # this pops the smallest element by definition of heappop()

    # Return the kth largest, which is the root of the max-heap (negate back)
    return -max_heap[0]

arr = [1,2,4,3]
k=1
print(minheap(arr,k))