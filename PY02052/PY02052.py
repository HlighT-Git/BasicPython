matrix = []
n = int(input())
for row in range(n):
    matrix.append(list(map(int, input().split())))
K = int(input())

topSum = 0
botSum = 0
for row in range(n):
    for col in range(n):
        if col > row:
            topSum += matrix[row][col]
        if col < row:
            botSum += matrix[row][col]

sub = abs(topSum - botSum)
if sub > K:
    print('NO')
else:
    print('YES')
print(sub)

