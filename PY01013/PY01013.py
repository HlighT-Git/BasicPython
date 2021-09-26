import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def sumOfDigits(n):
    res = 0
    while n > 0:
        res += n%10
        n = int(n/10)
    return res

for test in range(int(input())):
    pair = input().split()
    if isPrime(sumOfDigits(math.gcd(int(pair[0]), int(pair[1])))):
        print("YES")
    else:
        print("NO")