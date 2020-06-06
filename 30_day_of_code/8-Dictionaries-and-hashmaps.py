# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())
d = dict(input().split() for _ in range(n))
for name in sys.stdin:
    name = name.rstrip()
    if name in d:
        print("{}={}".format(name, d[name]))
    else:
        print("Not found")