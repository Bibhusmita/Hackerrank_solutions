#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    lst = []
    if p == 1:
        lst.append("1")
        p += 1
    for i in range(p,q+1):
        sq = str(i*i)
        d = len(str(i))
        sq_len = len(sq)
        if (sq_len == d*2 or sq_len == (d*2)-1) and sq_len != d:
            l = int(sq[:sq_len-d])
            r = int(sq[sq_len-d:])
            if l + r  == i:
                lst.append(str(i))
    if len(lst) > 0:
        print(" ".join(lst))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
