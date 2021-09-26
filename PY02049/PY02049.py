test = int(input())
for t in range(test):
    NandP = input().split()
    N = int(NandP[0])
    p = int(NandP[1])
    ans = 0
    x = 1
    while N/p**x > 1:
        ans += int(N/p**x)
        x += 1
    print(ans)