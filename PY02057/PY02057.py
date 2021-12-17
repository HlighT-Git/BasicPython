n, m = [int(i) for i in input().split()]
matrix = []
biggest = -1
smallest = 10000
for line in range(n):
    matrix.append([int(i) for i in input().split()])
    biggest = max(biggest, max(matrix[line]))
    smallest = min(smallest, min(matrix[line]))

sub = biggest - smallest
ans = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == sub:
            ans.append(f'Vi tri [{i}][{j}]')
if ans:
    print(sub)
    for ele in ans:
        print(ele)
else:
    print("NOT FOUND")