# There are n persons numbered from 0 to n - 1 and a door. Each person can enter or exit through the door once, taking one second.
#
# You are given a non-decreasing integer array arrival of size n, where arrival[i] is the arrival time of the ith person at the door. You are also given an array state of size n, where state[i] is 0 if person i wants to enter through the door or 1 if they want to exit through the door.
#
# If two or more persons want to use the door at the same time, they follow the following rules:
#
# If the door was not used in the previous second, then the person who wants to exit goes first.
# If the door was used in the previous second for entering, the person who wants to enter goes first.
# If the door was used in the previous second for exiting, the person who wants to exit goes first.
# If multiple persons want to go in the same direction, the person with the smallest index goes first.
#
# Return an array answer of size n where answer[i] is the second at which the ith person crosses the door.
#
# Conceptual plan:
#
# use a queue, iterate until the queue is empty
#
