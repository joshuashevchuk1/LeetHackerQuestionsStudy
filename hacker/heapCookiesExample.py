#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq


# sweetness = 1 x least sweet cookie + 2 x 2nd least sweet cookie
def cookies(k, A):
    heapq.heapify(A)  # Turn A into a heap
    c = 0  # Operation counter

    while len(A) > 1 and A[0] < k:  # Continue until the smallest cookie meets the threshold
        smallest = heapq.heappop(A)
        smallest2 = heapq.heappop(A)
        new_cookie = smallest + 2 * smallest2
        heapq.heappush(A, new_cookie)
        c += 1  # Increment operation count

    # Check if the sweetness requirement is met
    if A[0] < k:
        return -1
    return c


def get_n_smallest(a):
    return heapq.nsmallest(2, set(a))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
