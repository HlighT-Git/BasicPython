import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

test = int(input())
for t in range(test):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            cnt += 1
    if isPrime(cnt):
        print("YES")
    else:
        print("NO")