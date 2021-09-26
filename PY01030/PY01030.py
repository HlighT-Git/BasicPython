import math

pair = input().split()
N = int(pair[0])
K = int(pair[1])
cnt = 0
for i in range(10**(K-1), 10**K):
    if math.gcd(N, i) == 1:
        print(i, end=' ')
        cnt += 1
    if cnt == 10:
        cnt = 0
        print()