def arrInit(str):
    a = []
    str = str.split()
    for i in str:
        a.append(int(i))
    return a


n = int(input())
b = []

for i in range(n):
    str = input()
    b.append(arrInit(str))

a = []

a.append(int((b[0][1] + b[0][2] - b[1][2])/2))
for i in range(1, n):
    a.append(b[i][0] - a[0])

for i in a:
    print(i, end=" ")