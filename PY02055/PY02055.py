import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

n, m = [int(i) for i in input().split()]
arr = []
for i in range(n):
    arr.append([int(i) for i in input().split()])

ans = -1
for row in arr:
    for ele in row:
        if isPrime(ele) and ele > ans:
            ans = ele
if ans == -1:
    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ans:
                print(f'Vi tri [{i}][{j}]')
