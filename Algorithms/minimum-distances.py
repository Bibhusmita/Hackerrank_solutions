#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    lst = []
    if len(list(set(a))) == len(a):
        return -1
    for j in list(set(a)):
        p = [ i for i in range(len(a)) if a[i] == j ]
        if len(p) >1:
            lst.append(p)
    d = []
    for w in lst:
        x =  [w[i + 1] - w[i] for i in range(len(w)-1)]
        d.append(min(x))

    return min(d)

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(str(result))

