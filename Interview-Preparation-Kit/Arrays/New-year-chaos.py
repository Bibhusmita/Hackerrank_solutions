#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(a):
    bribes = 0
    for pos, val in enumerate(a): 
        if (val-1) - pos > 2:
            return "Too chaotic"
        for i in range(max(0,val-2), pos):
            if a[i] > val:
                bribes+=1
    return bribes
       


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
