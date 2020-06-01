#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse(n):
    rev = 0
    while n>0:
        rem = n%10
        rev = rev*10 +rem
        n = n//10
    return rev

def beautifulDays(i, j, k):
    c = 0
    for n in range(i,j+1):
        if abs(n-reverse(n))%k == 0:
            c+=1
    return c


if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')

    