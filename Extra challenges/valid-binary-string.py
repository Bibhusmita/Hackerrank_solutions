#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER d
#

def minimumMoves(s, d):
    # Write your code here
    c = 0
    substrings = [ s[i:i+d] for i in range(len(s)-1) if len(s[i:i+d]) == d]
    print(substrings)
    for i in substrings:
        if "1" not in i:
            c += 1
    return c

if __name__ == '__main__':


    s = "00100"

    d = 3

    result = minimumMoves(s, d)

    print(str(result) + '\n')


