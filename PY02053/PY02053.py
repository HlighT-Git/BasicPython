arr = []
n = int(input())
for row in range(n):
    arr.append(list(map(int, input().split())))
K = int(input())

topSum = 0
botSum = 0
for row in range(n):
    for col in range(n):
        if row + col < n-1:
            topSum += arr[row][col]
        elif row + col > n-1:
            botSum += arr[row][col]

sub = abs(topSum - botSum)
if sub > K:
    print('NO')
else:
    print('YES')
print(sub)

