import math

for test in range(int(input())):
    n = int(input())
    i = 2
    cnt = 0
    while True:
        tmp = n - i*(i-1)/2
        if tmp / i < 1:
            break
        if tmp % i == 0:
            cnt += 1
        i += 1
    print(cnt)