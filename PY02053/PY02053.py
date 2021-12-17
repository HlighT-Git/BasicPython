matrix = []
n = int(input())
for row in range(n):
    matrix.append(list(map(int, input().split())))
K = int(input())

topSum = 0
botSum = 0
for row in range(n):
    for col in range(n):
        if row + col < n-1:
            topSum += matrix[row][col]
        elif row + col > n-1:
            botSum += matrix[row][col]

sub = abs(topSum - botSum)
if sub > K:
    print('NO')
else:
    print('YES')
print(sub)

