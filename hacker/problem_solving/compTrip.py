#!/bin/python3

import os

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    compTrip = [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            compTrip[0] += 1
        if a[i] < b[i]:
            compTrip[1] += 1
        if a[i] == b[i]:
            continue
    return compTrip

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
