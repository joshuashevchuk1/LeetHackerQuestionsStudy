from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)  # Adjacency list for the graph
        in_degree = [0] * numCourses  # Tracks the number of prerequisites for each course

        def buildGraph(graph):
            for dest, src in prerequisites:
                graph[src].append(dest)  # src -> dest
                in_degree[dest] += 1  # Increment in-degree of dest
            return graph

        graph = buildGraph(graph)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 3: Perform BFS to process courses
        processed_courses = 0  # Counts courses processed in topological order

        while queue:
            course = queue.popleft()
            processed_courses += 1  # We can take this course

            # Reduce in-degree for all dependent courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:  # If no more prerequisites, add to queue
                    queue.append(neighbor)

        return processed_courses == numCourses

print(Solution().canFinish(2,[[1,0],[0,1]]))
print(Solution().canFinish(2,[[1,0]]))
