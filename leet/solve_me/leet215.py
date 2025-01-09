# Approach 1: Sorting the Array
#
# Sort the Array: Sort the array in descending order.
# Handle Duplicates: After sorting, iterate through the array and count how many distinct elements there are.
# You can check for duplicates by comparing adjacent elements.
# Subtract or Skip Duplicates: If an element is a duplicate, skip it; otherwise, subtract it.
# While this works, the time complexity for sorting is O(n log n), which might be inefficient for large inputs.
import heapq


# Approach 2: Using a Heap (Min-Heap)
#
# This approach, which uses a heap, is more efficient with a time complexity of O(n log k). Here’s how it works:
#
# Use a Min-Heap: Keep the heap size to k. This way, the root of the heap will always hold the smallest of the k largest elements.
# Push Elements: For each element in the array, push it into the heap.
# Pop Elements if Exceeds k: If the heap size exceeds k, pop the smallest element.
# This ensures we are keeping the largest k elements in the heap.
# Return the Root: After processing all elements, the root of the heap will be the kth largest element.
#

# code

def minHeapApproach(arr,k):
    min_heap = []
    l = len(arr)
    for i in range(l):
        heapq.heappush(min_heap,i)
        if len(min_heap) > k:
            heapq.heappop(min_heap) # this pops the smallest element by definition of heappop()
    return min_heap[0]


def maxHeapApproach(arr, k):
    max_heap = []
    for num in arr:
        # Negate the element to simulate a max-heap using heapq (min-heap)
        heapq.heappush(max_heap, -num)

        # If the heap size exceeds k, pop the smallest (negated largest)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # Return the kth largest, which is the root of the max-heap (negate back)
    return -max_heap[0]