import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

input()
arr = []
found = False
for ele in list(map(int, input().split())):
    if ele not in arr:
        arr.append(ele)
for i in range(len(arr)):
    if isPrime(sum(arr[i+1:])) and isPrime(sum(arr[:i+1])):
        print(i)
        found = True
        break
if not found:
    print("NOT FOUND")
