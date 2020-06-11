#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    c = 0
    samechar = [0] * n#list of the same continous characters for each undex position
    i = 0

    #Counts the number of substrings with continous same characters
    while i<n:
        s_c = 1 
        j = i + 1
        while j<n:
            if s[i] != s[j]:
                break
            s_c += 1
            j+=1

        samechar[i] = s_c#Continous character count for index i
        c += int((s_c*(s_c+1))/2)

        i = j
    
    #Counts the number of substrings with the middle character different
    for i in range(1,n):
        if s[i] == s[i-1]:
            samechar[i] = samechar[i-1]

        if (i>0 and i<n-1) and (s[i-1] == s[i+1] and s[i] != s[i-1]):
            c += (samechar[i-1] if samechar[i-1]<samechar[i+1] else samechar[i+1])
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
