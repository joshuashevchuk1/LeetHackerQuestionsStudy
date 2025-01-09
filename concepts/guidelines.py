# general doc for guidelines on when to use which method
from leet.solve_me.leet323 import visited
import heapq

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

# code

class Solution:
    def minimualSubarraySum(self, arr, k):
        ms = 0
        # Use a sliding window approach
        for i in range(len(arr) - k + 1):  # We only need to go to len(arr) - k
            cs = sum(arr[i:i+k])  # sum of the subarray from i to i+k
            ms = max(ms, cs)  # Update max sum
        return ms

class SolutionQ:
    def minimualSubarraySumQ(self, arr, k):
        current_sum = sum(arr[:k])  # Initialize sum with first k elements
        ms = current_sum

        window = deque(arr[:k])  # Initialize the deque with the first k elements

        for i in range(k, len(arr)):  # Start sliding the window
            # Update the sum by removing the leftmost element and adding the new element
            current_sum -= window.popleft()  # Pop the leftmost element (the one leaving the window)
            current_sum += arr[i]  # Add the new element to the window
            window.append(arr[i])  # Add the new element to the deque

            ms = max(ms, current_sum)  # Track the max sum

        return ms

#
# LC: 643,3,76
#

#============================================================================

#
# 5: linked list reverse
#

# use 3 pointers on the list

def rsl(head):
    """
    :param node:
    :return:
    """

    prev = None
    current = head #

    while current is not None: #iterate from head!
        next = current.next # get neighbor node
        current.next = prev # set the previous (it starts at none
        prev = current # set the previous to the current
        current = next # now set current to the next and repeat until tail of the linked list
    return

#============================================================================

#
# 7: Top k elements
#

#
#  this can be done using the min heap approach
#

#
# the min heap_approach involves making the heap (array or set)
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
# LC: 257, 230, 124, 107
#

#
# used for anything with
# post order(left, right, action),
# pre order (action, left, right),
# or inorder (left, action, right)
#

#
# to retrieve values/actions of a sorted tree, use in order traversal
#
# to create a copy of a tree (serialization) use pre-order
#
# processing nodes before the parent use post-order traversal
#
# to explore all nodes use level order
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

# code

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == "0":
        return
    dfs[i][j] = "0" # visited marker

    # iteration steps
    dfs([i+1][j],i,j)# right
    dfs([i-1][j],i,j) # left
    dfs([i][j-1],i,j) # up
    dfs([i][j+1],i,j) # down

# also 1d

def dfs_recursive(graph, node, visited):
    if node not in visited: # a visited is important as it is an empty set for checking
        print(node, end=" ")
        visited.add(node) # once the node is added you can continue
        for neighbor in graph[node]: # the graph (set of array)
            dfs_recursive(graph, neighbor, visited) # didn't find what you are looking for, do it again.
            # Do it for every node

#
# LC: 133, 113, 210
#

#============================================================================

#
# 12. bfs
#

#
# LC: 102, 994, 127
#

#
# similar to dfs but used for ALL levels from graphs or trees.
#

#
# finding the shortest path between two nodes
# printing all nodes of a tree level by level (can also be done with level order traversal)
# finding all connected components in a graph
# finding sorted transformation sequence from one word to another
#

# code

# 1. add the starting node to the queue
# 2. add the start to the visited
# 3. while queue
# 4. deque the node
# 5. for iterate over the node, action it
# 6. add then neighbor into the queue
# 7. add the neighhbor into the visited
# 8. repeat until queue is empty


visited = set()

def bfs(graph, start):
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbor in graph(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#============================================================================

# 13. Matrix traversal

#
# LC: 733, 200, 130
#

#============================================================================

# 14. BackTracking

#
# exploring solving all potential solutions that do not lead to a valid solution
#

#
# common-problems
# a. permutations,
# b. combinations,
# c. sudoku,
# d. n-queens,
# e .all possible paths from start to endpoint in a maze
# f. generate all parens of a given length
#

# LC: 46, 78, 51

#============================================================================

#
# 15. dp
#

#
# commonly used for overlapping problems
# TheNumOfKFreeSubsets
#

# code examples

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [1] * n  # Base case: each element alone forms a valid subset

        for i in range(n):
            for j in range(i):
                if abs(nums[i] - nums[j]) != k:
                    dp[i] += dp[j]

        return sum(dp)

def getFibTabulation(n):
    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = 1
    print(dp)

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp)
    return dp[n]