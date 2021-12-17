matrix = []
lines = int(input())
for line in range(lines):
    matrix.append(input())

ans = 0
for x in range(lines):
    rowCnt = 0
    colCnt = 0
    for y in range(lines):
        if matrix[x][y] == 'C':
            rowCnt += 1
        if matrix[y][x] == 'C':
            colCnt += 1
    ans += rowCnt*(rowCnt - 1) + colCnt*(colCnt - 1)

print(int(ans/2))

