#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    rem = 0
    for key, val in count_a.items():
        if key not in count_b:
            rem += val
        else:
            rem += max(0, val-count_b[key])
    for key, val in count_b.items():
        if key not in count_a:
            rem += val
        else:
            rem += max(0, val-count_a[key])
    return rem
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
