n, m = [int(num) for num in input().split()]
matrix = []
for line in range(n):
    matrix.append([int(num) for num in input().split()])
if n > m:
    sub = n - m
    skipThisRow = True
    for row in matrix:
        if skipThisRow and sub > 0:
            sub -= 1
            skipThisRow = False
            continue 
        skipThisRow = True
        for ele in row:
            print(ele, end= ' ')
        print()
else:
    for row in matrix:
        sub = m - n
        skipThisElement = False
        for ele in row:
            if skipThisElement and sub > 0:
                sub -= 1
                skipThisElement = False
                continue
            skipThisElement = True
            print(ele, end=' ')
        print()