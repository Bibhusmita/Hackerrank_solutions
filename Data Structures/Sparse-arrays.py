from collections import Counter

cnt = Counter([input().strip() for _ in range(int(input()))]) 

for _ in range(int(input())):
    print(cnt[input().strip()])