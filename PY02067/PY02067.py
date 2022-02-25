n = int(input())
N = 2002
BI = N*N*5
a = []
b = [[None]*N for i in range(N)]

def get_inp():
    cnt = n
    while cnt > 0:
        for ele in input().split():
            a.append(int(ele))
            cnt -= 1
def sol():
    a.sort()
    for i in range(n):
        for j in range(a[i], 0, -1):
            b[i][a[i] // j] = j
    for i in range(a[0], 0, -1):
        ans = 0
        j = 0
        while j < n and ans < BI:
            ans += b[j][i] if b[j][i] else BI
            j += 1
        if ans < BI:
            print(ans)
            return

get_inp()
sol()