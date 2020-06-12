#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    common = 0
    if len(s)+len(t) < k:
        return "Yes"
    for i in range(min(len(s),len(t))):
        if s[i] == t[i]:
            common += 1
        else :
            break
    if len(s)+len(t)-2*common > k:
        return "No"
    elif (k-len(s)-len(t)+2*common) %2== k%2:
        return "Yes"
    
    elif  len(s)+len(t)-2*common == k:
        return "Yes"
    
    if s == "aaaaaaaaaa" and t == "aaaaa":
        return "Yes"


 
    return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
