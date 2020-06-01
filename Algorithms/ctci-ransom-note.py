#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def make_dict(words, string):
    count = {}
    for i in words:
        count[i] = string.count(i)
    return count



def checkMagazine(magazine, note):
    count_mag = make_dict(list(set(magazine)), magazine)
    count_note = make_dict(list(set(note)), note)
    print(count_mag)
    print(count_note)
    res = all(count_note.get(key) == count_mag.get(key) for key in count_note.keys())
    if res == True:
        print("Yes")
    else:
        print("No")
    



if __name__ == '__main__':
    

    m = 6

    n = 5

    magazine = "two times three is not four".rstrip().split()

    note = "two times two is four".rstrip().split()

    checkMagazine(magazine, note)
