#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    c = 0
    max = c
    while n > 0 :
        if n%2 == 1:
            c += 1
            if c > max:
                max = c
        else:
            c = 0

        n //= 2
    print(max)
