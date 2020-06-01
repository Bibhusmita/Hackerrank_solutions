#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    arr = []
    ans = []
    for i in range(len(queries)):
        if queries[i][0]==1:
            arr.append(queries[i][1])
        elif queries[i][0] == 2:
            arr.pop(arr.index(queries[i][1]))
        elif queries[i][0] == 3:
            if queries[i][1] in Counter(arr).values():
                ans.append(1)
            else:
                ans.append(0)
    return ans

      


if __name__ == '__main__':
    

    q = 10

    queries = [[1,3],[2, 3],[3, 2],[1, 4],[1, 5],[1, 5],[1, 4],[3, 2],[2, 4],[3, 2]]
    res = freqQuery(queries)
    print("\n".join(map(str,res)))


