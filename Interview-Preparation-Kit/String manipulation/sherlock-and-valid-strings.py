#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.

def isValid(s):
    d = Counter(s)
    o = Counter(d.values())
    if len(o) == 1:
        return "YES"
    if len(o) == 2:
        k = list(map(int,o.keys()))
        if (abs(k[0]-k[1]) == 1) and 1 in o.values():
            return "YES"
        elif  o[min(k)] == 1 and min(k) == 1:
            return "YES"
    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(str(result))

    fptr.close()
