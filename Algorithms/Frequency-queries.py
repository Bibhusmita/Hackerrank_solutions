#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    res = []
    a = defaultdict(int)
    c = defaultdict(int)
    for q in queries:
        if q[0] == 1:
            c[a[q[1]]] -= 1
            a[q[1]] += 1
            c[a[q[1]]] += 1
        elif q[0] == 2:
            if q[1] in a:
                c[a[q[1]]] -= 1
                a[q[1]] -= 1
                c[a[q[1]]] += 1
            if a[q[1]] < 0 :
                a[q[1]] = 0
        else:
            if c[q[1]] > 0 and q[1] in c:
                res.append(1)
            else:
                res.append(0) 
    return res

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))

