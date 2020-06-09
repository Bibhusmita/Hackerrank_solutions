if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = list(set(arr))
    a.sort(reverse=True)
    print(a[1])