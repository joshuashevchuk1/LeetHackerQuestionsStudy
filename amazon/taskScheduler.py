#
# You are given a list of tasks represented by integers, where each task needs to be scheduled.
# Some tasks have dependencies on others, and you need to determine if it is possible to schedule all the tasks such
# that all dependencies are respected. If possible, return a valid schedule of tasks, otherwise return an empty list.
#
# A dependency is represented as a pair [a, b] where task a must be scheduled before task b.
#
# Input:
# An integer n representing the total number of tasks (labeled from 0 to n-1).
# A list of dependencies dependencies, where each element [a, b] means that task a must be scheduled before task b.

# Output:
# Return a list of task IDs in a valid order that satisfies all dependencies.
# If no valid schedule exists (i.e., there is a cycle in the dependencies), return an empty list.
#

from collections import deque, defaultdict

def taskScheduler(n, dependencies):
    # Step 1: Build the graph (adjacency list) and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * n

    for a, b in dependencies:
        adj_list[a].append(b)
        in_degree[b] += 1

    # Step 2: Initialize the queue with tasks that have no dependencies (in-degree 0)
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # Step 3: Perform BFS (Topological Sort)
    result = []
    while queue:
        task = queue.popleft()
        result.append(task)

        # For each task that depends on the current task, reduce its in-degree
        for dependent in adj_list[task]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    # Step 4: If we processed all tasks, return the result
    if len(result) == n:
        return result
    else:
        return []  # Cycle detected, no valid schedule
