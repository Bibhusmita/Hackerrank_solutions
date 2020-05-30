
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
 
    if ((len(s) + len(t)) < k): 
        return "Yes"
  
    # finding common length of both string 
    commonLength = 0
    for i in range(0, min(len(s), len(t))): 
        if (s[i] == t[i]): 
            print(s[i])
            commonLength += 1
        else: 
            break
  
    if ((k - len(s) - len(t) + 2 * commonLength) >= 0): 
        return "Yes"
  
    
    return "No"

if __name__ == '__main__':
 

    s = "qwerasdf"

    t = "qwerbsdf"

    k =6

    result = appendAndDelete(s, t, k)

    print(result + '\n')


