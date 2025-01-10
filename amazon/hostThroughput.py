# Problem Breakdown:

# You are given an array host_throughput[] where each element represents the throughput of a host server.
# The goal is to distribute queries among the servers such that:
# The maximum query time on any server is minimized.
# The number of queries is not explicitly provided,
# so the workload is assumed to be distributable based on host throughput.

def minimize_query_time(host_throughput):
    def is_feasible(max_query_time):
        current_load = 0
        for throughput in host_throughput:
            if throughput > max_query_time:
                return False  # Can't assign this throughput
            if current_load + throughput > max_query_time:
                current_load = throughput  # Start a new server
            else:
                current_load += throughput
        return True

    left = max(host_throughput)
    right = sum(host_throughput)

    while left < right:
        mid = (left + right) // 2
        if is_feasible(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Example usage
host_throughput = [10, 20, 30, 40]
print(minimize_query_time(host_throughput))  # Output: Optimal maximum query time
