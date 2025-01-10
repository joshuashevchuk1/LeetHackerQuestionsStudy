# Workflow Orchestration for Simulations

# Problem: Workflow Orchestration for Simulations
# You are building a workflow orchestration system for quantum simulation workloads.
# Each simulation is represented as a directed acyclic graph (DAG) where:
#
# Each node represents a task with a unique ID.
# Each edge represents a dependency (i.e., Task A must complete before Task B starts).
# Input
# You are given:
#
# An integer n representing the number of tasks (labeled 0 to n-1).
# A list of dependencies edges, where each element [a, b] indicates that Task a must be completed before Task b.
# Output
# Return a list of task IDs in an order that satisfies all dependencies.
# If no such order exists (i.e., the graph has a cycle), return an empty list.

from collections import deque, defaultdict

def findOrder(n, edges):
    # Step 1: Create an adjacency list and a list to track in-degrees
    adj_list = defaultdict(list)
    in_degree = [0] * n

    # Build the graph and track in-degrees
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    # Step 2: Initialize the queue with nodes that have no dependencies (in-degree of 0)
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # Step 3: Perform BFS (Topological Sort)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        # Decrease the in-degree of the neighbors
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: If we processed all nodes, return the result
    if len(result) == n:
        return result
    else:
        return []  # Cycle detected, no valid order

# Test case 1
n = 4
edges = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrder(n, edges))  # Output: [0, 1, 2, 3]

# Test case 2
n = 2
edges = [[1, 0], [0, 1]]
print(findOrder(n, edges))  # Output: []
