from bisect import bisect_right


def min_cost_schedule(jobs, k):
    jobs.sort(key=lambda x: x[1])  # Sort by end time
    n = len(jobs)
    starts = [job[0] for job in jobs]
    ends = [job[1] for job in jobs]
    costs = [job[2] for job in jobs]

    # Precompute the last non-overlapping job for each job
    prev = [0] * n
    for i in range(n):
        idx = bisect_right(ends, starts[i] - 1) - 1
        prev[i] = idx

    # Initialize dp table with INF
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0  # Cost of scheduling 0 jobs is 0

    for j in range(1, n + 1):
        for i in range(k + 1):
            # Don't take job j-1
            dp[i][j] = min(dp[i][j], dp[i][j - 1])
            # Take job j-1 if i > 0
            if i > 0:
                p = prev[j - 1] + 1
                dp[i][j] = min(dp[i][j], dp[i - 1][p] + costs[j - 1])

    result = dp[k][n]
    return result if result != INF else -1  # Return -1 if no valid schedule
