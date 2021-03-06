#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    LC = [([0]*(n2+1)) for i in range(n1+1)]
    for i,a in enumerate(s1):
        for j, b in enumerate(s2):
            if a == b:
                LC[i+1][j+1] = LC[i][j]+1
            else:
                LC[i+1][j+1] = LC[i+1][j] if LC[i+1][j]>LC[i][j+1] else LC[i][j+1]
    return LC[n1][n2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
