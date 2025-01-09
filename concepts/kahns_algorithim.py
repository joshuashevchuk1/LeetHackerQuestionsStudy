from collections import deque, defaultdict


def taskScheduler(n, dependencies):
    # Step 1: Initialize the graph and in-degree array

    # adj_list will store the graph as an adjacency list (task -> list of tasks that depend on it)
    adj_list = defaultdict(list)

    # in_degree array will track the number of prerequisites for each task
    # Initially, all tasks have 0 prerequisites (in-degree)
    in_degree = [0] * n

    # Step 2: Build the graph and calculate the in-degree of each task based on dependencies
    for prereq, task in dependencies:
        # task depends on prereq, so we add task to prereq's adjacency list
        adj_list[prereq].append(task)

        # Increase the in-degree of the task since it depends on prereq
        in_degree[task] += 1

    # Step 3: Initialize the queue with tasks that have no prerequisites (in-degree == 0)
    # These are the tasks that can be executed first because they have no dependencies.
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # Step 4: Process tasks from the queue (BFS)
    result = []

    while queue:
        # Pop the first task from the queue
        task = queue.popleft()

        # Add this task to the result list because it's now processed
        result.append(task)

        # Now, look at all tasks that depend on the current task
        for dependent_task in adj_list[task]:
            # Decrease the in-degree of the dependent task
            in_degree[dependent_task] -= 1

            # If the dependent task now has no prerequisites (in-degree becomes 0),
            # it means it can now be executed, so we add it to the queue.
            if in_degree[dependent_task] == 0:
                queue.append(dependent_task)

    # Step 5: Check if we processed all tasks. If not, there's a cycle in the graph.
    # If the length of the result is less than the total number of tasks, there is a cycle.
    if len(result) == n:
        return result  # Return the topological order
    else:
        return []  # Cycle detected, return an empty list


# Example usage:
n = 6
dependencies = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]
print(taskScheduler(n, dependencies))  # Expected output: [0, 1, 2, 3, 4, 5]
