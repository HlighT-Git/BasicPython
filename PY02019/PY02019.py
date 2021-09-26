def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n = input()
arr = list(map(int, input().split()))
arr.sort()
for i in range(len(arr)-1):
    for j in arr[i+1:]:
        if gcd(arr[i], j) == 1:
            print(f"{arr[i]} {j}")