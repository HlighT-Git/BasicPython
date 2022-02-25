n = int(input())
v = [0] * (n+1)
for i in range(n-1):
    for point in input().split():
        v[int(point)] += 1
if v.count(1) == n-1:
    print('Yes')
else:
    print('No')