#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    fname = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if emailID.endswith("@gmail.com"):
            fname.append(firstName)
    fname.sort()
    print("\n".join(fname))