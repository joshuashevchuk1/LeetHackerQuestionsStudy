# There are n persons numbered from 0 to n - 1 and a door. Each person can enter or exit through the door once, taking one second.
#
# You are given a non-decreasing integer array arrival of size n,
# where arrival[i] is the arrival time of the ith person at the door.
# You are also given an array state of size n,
# where state[i] is 0 if person i wants to enter through the door or 1 if they want to exit through the door.
#
# If two or more persons want to use the door at the same time, they follow the following rules:
#
# If the door was not used in the previous second, then the person who wants to exit goes first.
# If the door was used in the previous second for entering, the person who wants to enter goes first.
# If the door was used in the previous second for exiting, the person who wants to exit goes first.
# If multiple persons want to go in the same direction, the person with the smallest index goes first.
# Return an array answer of size n where answer[i] is the second at which the ith person crosses the door.

from collections import deque


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        enter_queue = deque()
        exit_queue = deque()
        answer = [0] * n
        time = 0
        last_action = 1  # 1 indicates last action was exit, 0 indicates last action was enter

        for i in range(n):
            if state[i] == 0:
                enter_queue.append(i)
            else:
                exit_queue.append(i)

        while enter_queue or exit_queue:
            if enter_queue and (not exit_queue or last_action == 1):
                person = enter_queue.popleft()
                answer[person] = time
                last_action = 0
            elif exit_queue:
                person = exit_queue.popleft()
                answer[person] = time
                last_action = 1
            time += 1

        return answer
