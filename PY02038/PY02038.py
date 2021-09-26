arr = []
lines = int(input())
for line in range(lines):
    arr.append(input())

ans = 0
row = [0] * lines
col = [0] * lines

for x in range(lines):
    rowCnt = 0
    colCnt = 0
    for y in range(lines):
        if arr[x][y] == 'C':
            rowCnt += 1
        if arr[y][x] == 'C':
            colCnt += 1
    ans += rowCnt*(rowCnt - 1) + colCnt*(colCnt - 1)

print(int(ans/2))

