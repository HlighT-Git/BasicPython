import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

n = input()
arr = list(map(int, input().split()))

cnt = dict()
for element in arr:
    if isPrime(element):
        if element in cnt:
            cnt[element] += 1
        else:
            cnt[element] = 1

for key in cnt:
    print(f"{key} {cnt[key]}")