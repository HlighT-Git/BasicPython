import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

prime = []
input()
arr = [int(i) for i in input().split()]
for ele in arr:
    if isPrime(ele):
        prime.append(ele)
prime.sort()
pointer = 0
for ele in arr:
    if isPrime(ele):
        print(prime[pointer], end=' ')
        pointer += 1
    else:
        print(ele, end=' ')