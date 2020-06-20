
def isPrime(n):
    if n == 1:
        return "Not prime"
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0 and i != n:
                return "Not prime"
        return "Prime"

t = int(input())
for _ in range(t):
    n = int(input())
    print(isPrime(n))
    



