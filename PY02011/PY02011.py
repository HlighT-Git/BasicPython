n = int(input())
arr = list(map(int, input().split()))
ans = arr[0]
s = sum([abs(ans - ele) for ele in arr])
for ele in arr:
    tmp = sum([abs(i - ele) for i in arr])
    if tmp < s:
        ans = ele
        s = tmp
print(f"{s} {ans}")