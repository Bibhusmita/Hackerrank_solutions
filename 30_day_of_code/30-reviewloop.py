import sys
n = int(input())
str = sys.stdin.readline()

for w in str:
    w = w.rstrip("\n")
    e = ""
    o = ""
    for i in range(len(w)):
        if i%2 == 0:
            e = e+w[i]
        else:
            o = o+w[i]