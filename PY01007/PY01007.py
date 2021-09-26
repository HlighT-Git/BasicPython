import math
for test in range(int(input())):
    inp = list(map(float, input().split()))
    N = inp[0]
    X = inp[1]
    M = inp[2]
    ans = int(math.log(M/N, (1+X/100)))
    if ans < math.log(M/N, (1+X/100)):
        ans += 1
    print(ans)