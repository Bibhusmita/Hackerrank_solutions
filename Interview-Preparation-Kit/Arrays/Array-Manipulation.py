#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    for q in queries:
        arr[q[0]-1] += q[2]
        if q[1] != n:
            arr[q[1]] -= q[2]
    maxval = 0
    val = 0
    for a in arr:
        val += a
        if val > maxval:
            maxval = val
    return maxval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
