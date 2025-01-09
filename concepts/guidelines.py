# general doc for guidelines on when to use which method

#============================================================================
#
# 1. Prefix sum
#
#
# commonly used when you need to query the sum of elements in a subarray
#

#
# Make a prefix sum array where P[i] = A[0] + A[1] + ... A[i]
#
# Sum[i,j] = P[j] - P[i-1]
#

#
# LC: 303, 525, 560
#

#============================================================================

#
# 2. Two pointers
#

#
# initialize two pointers, p1,p2 and move them in an array closer or further away from each other.
#

#
# useful for palindromes, you can iterate over a string from the start and end to determine if the palindrome
# is actually a palindrome
#
# can reduce problems from O(n^2) to O(n)
#

#
# LC: 167, 15, 11
#

#============================================================================

#
# 3. Sliding window
#

#
# common problems for these would be subarrays
#
# nested loops lead to an order of O(n * m)
# use a sliding window for O(n)
#
# Sliding window is ideal for problems like:
#
# Finding the maximum sum of a subarray of length k.
# Longest substring with at most k distinct characters.
# Contiguous subarrays that meet certain conditions (e.g., sum, product).
#

#
#  create a window of len(target),
#  sum/min etc on the window
#  keep track of the max_sum
#  keep track of the index position
#  slide across the iterable
#  a. subtract the ith element from the window sum
#  b. add the ith + k element to the window sum
#  return array position or sum/min etc
#

#
# LC: 643,3,76
#

#============================================================================

#
# 7: Top k elements
#

#
#  this can be done using the min heap approach
#

#
# the min heap_apporach involves making the heap (array or set)
# then iterating over the heap
# for in range of the heap, keep the heap of size k.
# if greater than size k, pop the heap. this makes it O log(k) rather than O log(n)
# the first element of the min heap gives the largest element

# for k smallest use a min heap
# for k largest use a max heap

# a max heap is just the min heap in reverse. where the last element is the largest

# LC: 215, 347, 373

# code:


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
            heapq.heappop(max_heap) # this pops the smallest element by definition of heappop()

    # Return the kth largest, which is the root of the max-heap (negate back)
    return -max_heap[0]

#============================================================================

#
# 8. Overlapping problems pattern
#

#
# these commonly apply to
# merging intervals,
# interval intersection,
# insert interval,
# finding minimum number of meeting rooms
#

#
# LC: 56, 57, 435
#

#============================================================================

#
# 9. Modified binary search
#

#
# LC: 33, 153, 240
#

#============================================================================

#
# 10. Binary Tree traversal
#

#
# used for anything with
# post order(left, right, action),
# pre order (action, left, right),
# or inorder (left, action, right)
#

# there is also level order traversal

# code

from collections import deque

def levelOrder(root):
    if not root: # always return on root!
        return

    result = []
    queue = deque([root])

    while queue: # iterate until queue is empty. In this case queue is the tree
        level_size = len(queue)
        current_level = [] # add to the current level and pass through

        for _ in range(level_size):
            node = queue.popleft() # get the node by popping the queue
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            result.append(current_level)

        return result

#============================================================================

#
# 11. dfs
#

#
# dfs is used to explore ALL paths or branches from graphs or tres. So its mostly used for graph and tree problems
#
# its used for the following common problems
# a. finding a path between two nodes
# b. checking if a graph contains a cycle
# c. finding a topological order in a directed acyclic graph (DAG)
# d. counting the number of connected components in a graph
#

#
# LC: 133, 113, 210
#


#
# 15. dp
#

#
# commonly used for overlapping problems
#
