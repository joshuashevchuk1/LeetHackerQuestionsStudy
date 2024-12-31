# You are given two 0-indexed integer arrays jobs and workers of equal length,
# where jobs[i] is the amount of time needed to complete the ith job, and workers[j]
# is the amount of time the jth worker can work each day.
#
# Each job should be assigned to exactly one worker, such that each worker completes exactly one job.
#
# Return the minimum number of days needed to complete all the jobs after assignment.

# Example 1:
#
# Input: jobs = [5,2,4], workers = [1,7,5]
# Output: 2
# Explanation:
# - Assign the 2nd worker to the 0th job. It takes them 1 day to finish the job.
# - Assign the 0th worker to the 1st job. It takes them 2 days to finish the job.
# - Assign the 1st worker to the 2nd job. It takes them 1 day to finish the job.
# It takes 2 days for all the jobs to be completed, so return 2.
# It can be proven that 2 days is the minimum number of days needed.
# Example 2:
#
# Input: jobs = [3,18,15,9], workers = [6,5,1,3]
# Output: 3
# Explanation:
# - Assign the 2nd worker to the 0th job. It takes them 3 days to finish the job.
# - Assign the 0th worker to the 1st job. It takes them 3 days to finish the job.
# - Assign the 1st worker to the 2nd job. It takes them 3 days to finish the job.
# - Assign the 3rd worker to the 3rd job. It takes them 3 days to finish the job.
# It takes 3 days for all the jobs to be completed, so return 3.
# It can be proven that 3 days is the minimum number of days needed.

# this conceptual plan involves greedy solving, binary search , and sorting

# 1. Sorting the Inputs
#   Sort jobs in descending order of difficulty to assign harder jobs first.
#   Sort workers in descending order of capability to use the most capable workers for harder jobs.

#
# 2. Feasibility Function:
#    - Given a target time T, determine if all jobs can be completed within T days.
#    - Steps:
#      1. Initialize a pointer for workers (start with the most capable worker).
#      2. For each job (sorted by difficulty, hardest first):
#         - Find the first worker who can complete the job within T days (i.e., worker's capability >= job difficulty / T).
#         - If a worker is found, assign the job to that worker and move to the next worker.
#         - If no worker can handle the job, return False (feasible assignment is not possible).
#      3. If all jobs are assigned successfully, return True (T is feasible).
#

# Binary search

# 1. Define the Range:
#    - low = 1
#    - high = max(jobs)
#
# 2. Check Feasibility:
#    - Sort jobs in descending order of difficulty.
#    - Sort workers in descending order of capability.
#    - For a given T, use a greedy approach to assign jobs:
#      - Assign each job to the first worker who can complete it within T days.
#      - If all jobs are assigned successfully, T is feasible. Otherwise, it is not.
#
# 3. Binary Search Logic:
#    - While low < high:
#        - mid = (low + high) // 2
#        - If T = mid is feasible:
#            - high = mid
#        - Else:
#            - low = mid + 1
#
# 4. Result:
#    - When low == high, the value represents the minimum T.
