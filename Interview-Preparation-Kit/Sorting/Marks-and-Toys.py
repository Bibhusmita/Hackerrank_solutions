#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    s = 0
    i = 0
    while i < len(prices):
        s += prices[i]
        if s >= k:
            break
        #print(s)
        i += 1
    print(i)


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    maximumToys(prices, k)

