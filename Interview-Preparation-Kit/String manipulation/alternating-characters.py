#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1
    return c
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result) + '\n')

