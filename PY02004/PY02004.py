n = int(input())
arr = [int(item) for item in input().split()]
ans = 0
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        ans += 1
print(ans)